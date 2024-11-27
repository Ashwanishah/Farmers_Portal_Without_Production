from flask import Flask,url_for,render_template

from forms import InputForm
import pandas as pd
import joblib

app=Flask(__name__)
app.config["SECRET_KEY"]="secret_key"

model=joblib.load("Binary_Classification_of_smoke_status/model.joblib")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",title="Home")


@app.route("/predict",methods=["GET","POST"])
def predict():
    form=InputForm()
    if form.validate_on_submit():
        x_new=pd.DataFrame(dict(
            age=[form.age.data],
            height_cm =[form.height_cm.data],
            weight_kg=[form.weight_kg.data],
            waist_cm=[form.waist_cm.data],
            eyesight_left=[form.eyesight_left.data],
            eyesight_right=[form.eyesight_right.data],
            hearing_left=[form.hearing_left.data],
            hearing_right=[form.hearing_right.data],
            systolic=[form.systolic.data],
            relaxation=[form.relaxation.data],
            fasting_blood_sugar=[form.fasting_blood_sugar.data],
            Cholesterol=[form.Cholesterol.data],
            triglyceride=[form.triglyceride.data],
            HDL=[form.HDL.data],
            LDL=[form.LDL.data],
            hemoglobin=[form.hemoglobin.data],
            Urine_protein=[form.Urine_protein.data],
            serum_creatinine=[form.serum_creatinine.data],
            AST=[form.AST.data],
            ALT=[form.ALT.data],
            Gtp=[form.Gtp.data],
            dental_caries=[form.dental_caries.data],
        ))
        prediction=model.predict(x_new)
        message=f"THE PREDICTED VALUE IS {prediction:}"
    else:
        message="INVLAID INPUT"
    return render_template("predict.html",title="Predict",form=form,output=message)

if __name__=="__main__":
    app.run(debug=True)