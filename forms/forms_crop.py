from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (SelectField,DateField,SubmitField,IntegerField)
from wtforms.validators import DataRequired,NumberRange

train=pd.read_csv("Crop_Recommendation_system/Dataset/Crop_recommendation.csv")
X_data=train.drop(["label"],axis=1)

class InputFormCrop(FlaskForm):
    N=IntegerField(
        label="N",
        validators=[DataRequired(),NumberRange(min=0,max=140)]
    )
    P=IntegerField(
        label="P",
        validators=[DataRequired(),NumberRange(min=5,max=145)]
    )
    K=IntegerField(
        label="K",
        validators=[DataRequired(),NumberRange(min=5,max=205)]
    )
    temperature=IntegerField(
        label="temperature",
        validators=[DataRequired(),NumberRange(min=9,max=44)]
    )
    humidity=IntegerField(
        label="humidity",
        validators=[DataRequired(),NumberRange(min=14,max=100)]
    )
    ph=IntegerField(
        label="ph",
        validators=[DataRequired(),NumberRange(min=3,max=10)]
    )
    rainfall=IntegerField(
        label="rainfall",
        validators=[DataRequired(),NumberRange(min=20,max=300)]
    )
    submit=SubmitField("Predict")