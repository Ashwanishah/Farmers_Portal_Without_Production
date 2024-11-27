from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (IntegerField,SelectField,DateField,SubmitField)
from wtforms.validators import DataRequired,NumberRange

train=pd.read_csv("Presdicites/DATASET/train.csv")
X_data=train.drop(["Crop_Damage"],axis=1)

class InputFormPresdicities(FlaskForm):
    Estimated_Insects_Count=IntegerField(
        label="Estimated_Insects_Count",
        validators=[DataRequired(),NumberRange(min=150,max=4097)]
    )
    Crop_Type=SelectField(
        label="Crop_Type",
        choices=X_data["Crop_Type"].unique().tolist(),
        validators=[DataRequired()]
    )
    Soil_Type=SelectField(
        label="Soil_Type",
        choices=X_data["Soil_Type"].unique().tolist(),
        validators=[DataRequired()]
    )
      # Sample mapping dictionary
    mapping = {1:"Never",
               2:"Previously used",
               3:"Currently using"
               }
    Pesticide_Use_Category = SelectField(
        label="Pesticide_Use_Category",
        choices=[(key, value) for key, value in mapping.items()],
        validators=[DataRequired()]
    )
    Number_Doses_Week=IntegerField(
        label="Number_Doses_Week",
        validators=[DataRequired(),NumberRange(min=0,max=95)]
    )
    Number_Weeks_Used=IntegerField(
        label="Number_Weeks_Used",
        validators=[DataRequired(),NumberRange(min=0,max=67)]
    )
    Number_Weeks_Quit=IntegerField(
        label="Number_Weeks_Quit",
        validators=[DataRequired(),NumberRange(min=0,max=50)]
    )
    Season=SelectField(
        label="Season",
        choices=X_data["Season"].unique().tolist(),
        validators=[DataRequired()]
    )
    submit=SubmitField("Predict")