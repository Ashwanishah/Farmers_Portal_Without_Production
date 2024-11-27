from forms.forms_fertilizer import InputFormFertilizer
from forms.forms_crop import InputFormCrop
from forms.forms_presdicities import InputFormPresdicities
import pandas as pd
import joblib
import os
import pickle
import numpy as np
import cv2
from flask import Flask, render_template, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image

app=Flask(__name__)
app.config["SECRET_KEY"]="secret_key"

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

model_disease = joblib.load('Plant_disease/model.pkl')

model=joblib.load("Fertilizer Prediction/model.joblib")
model_crop=joblib.load("Crop_Recommendation_system/model.joblib")
model_presticides=joblib.load("Presdicites/model.joblib")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(img_path,target_size=(128,128,3)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0 
    return img_array

@app.route("/")
def next():
    return render_template('next.html')
@app.route("/home")
def home():
    return render_template("home.html",title="Home")


@app.route("/prediction_smoke",methods=["GET","POST"])
def Predict_Smoke():
    form=InputFormFertilizer()
    if form.validate_on_submit():
        x_new=pd.DataFrame(dict(
            Temparature=[form.Temparature.data],
            Humidity =[form.Humidity.data],
            Moisture=[form.Moisture.data],
            Soil_Type=[form.Soil_Type.data],
            Crop_Type=[form.Crop_Type.data],
            Nitrogen=[form.Nitrogen.data],
            Potassium=[form.Potassium.data],
            Phosphorous=[form.Phosphorous.data],
        ))
        prediction=model.predict(x_new)
        message=f"THE PREDICTED VALUE IS {prediction:}"
    else:
        message="INVLAID INPUT"
    return render_template("prediction_fertilizer.html",title="Predict",form=form,output=message)

@app.route("/prediction_presdicities",methods=["GET","POST"])
def Predict_Presdicities():
    form=InputFormPresdicities()
    if form.validate_on_submit():
        x_new=pd.DataFrame(dict(
            Estimated_Insects_Count=[form.Estimated_Insects_Count.data],
            Crop_Type =[form.Crop_Type.data],
            Soil_Type=[form.Soil_Type.data],
            Pesticide_Use_Category=[form.Pesticide_Use_Category.data],
            Number_Doses_Week=[form.Number_Doses_Week.data],
            Number_Weeks_Used=[form.Number_Weeks_Used.data],
            Number_Weeks_Quit=[form.Number_Weeks_Quit.data],
            Season=[form.Season.data],
        ))
        prediction = model_presticides.predict(x_new)
        output_mapping={
            0:"ALIVE",
            1:"DAMAGED DUE TO OTEHR CAUSES",
            2:"DAMAGED DUE TO PESTI"
        }
        mapped_prediction = output_mapping.get(prediction[0], "Unknown")
        message = f"THE PREDICTED VALUE IS {mapped_prediction}"
    else:
        message="INVALID INPUT"
    return render_template("prediction_presdicities.html",title="Predict",form=form,output=message)


@app.route("/prediction_crop",methods=["GET","POST"])
def Predict_Crop():
    form=InputFormCrop()
    if form.validate_on_submit():
        x_new=pd.DataFrame(dict(
            N=[form.N.data],
            P=[form.P.data],
            K=[form.K.data],
            temperature=[form.temperature.data],
            humidity=[form.humidity.data],
            ph=[form.ph.data],
            rainfall=[form.rainfall.data],
        ))
        prediction=model_crop.predict(x_new)
        message=f"THE PREDICTED VALUE IS {prediction:}"
    else:
        message="INVLAID INPUT"
    return render_template("prediction_crop.html",title="Predict",form=form,output=message)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>', methods=['GET'])
def upload_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/prediction_plant',methods=['POST'])
def prediction_plant():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        img_array = preprocess_image(filepath)
        
        predictions = model_disease.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1) 
        
        class_names =['Apple___Apple_scab', 'Apple___Black_rot', 
            'Apple___Cedar_apple_rust', 'Apple___healthy', 
            'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew',
             'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
            'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
            'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
            'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
             'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 
            'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 
             'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
            'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 
            'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']
        
        predicted_label = class_names[predicted_class[0]]
        
        image_url = url_for('upload_image', filename=filename)
        return render_template('result.html', prediction=predicted_label, image_url=image_url)
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)