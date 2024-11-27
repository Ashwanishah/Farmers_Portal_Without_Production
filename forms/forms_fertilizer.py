from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (IntegerField,SelectField,DateField,SubmitField)
from wtforms.validators import DataRequired,NumberRange

train=pd.read_csv("Fertilizer Prediction\Fertilizer Prediction.csv")
X_data=train.drop(["Fertilizer_Name"],axis=1)

class InputFormFertilizer(FlaskForm):
    Temparature=IntegerField(
        label="Temparature",
        validators=[DataRequired(),NumberRange(min=25,max=38)]
    )
    Humidity=IntegerField(
        label="Humidity",
        validators=[DataRequired(),NumberRange(min=50,max=72)]
    )
    Moisture=IntegerField(
        label="Moisture",
        validators=[DataRequired(),NumberRange(min=25,max=65)]
    )
    Soil_Type=SelectField(
        label="Soil_Type",
        choices=X_data["Soil_Type"].unique().tolist(),
        validators=[DataRequired()]
    )
    Crop_Type=SelectField(
        label="Crop_Type",
        choices=X_data["Crop_Type"].unique().tolist(),
        validators=[DataRequired()]
    )
    Nitrogen=IntegerField(
        label="Nitrogen",
        validators=[DataRequired(),NumberRange(min=4,max=42)]
    )
    Potassium=IntegerField(
        label="Potassium",
        validators=[DataRequired(),NumberRange(min=0,max=19)]
    )
    Phosphorous=IntegerField(
        label="Phosphorous",
        validators=[DataRequired(),NumberRange(min=0,max=42)]
    )
    submit=SubmitField("Predict")