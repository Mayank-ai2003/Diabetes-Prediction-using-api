from pydantic import BaseModel, Field
from typing import Annotated


class UserInput(BaseModel):
    Pregnancies: Annotated[int, Field(..., lt=17)]
    Glucose: Annotated[int, Field(..., gt=0, lt=200)]
    BloodPressure: Annotated[int, Field(..., gt=0, lt=400)]
    SkinThickness: Annotated[int, Field(..., gt=0, lt=400)]
    Insulin: Annotated[int, Field(..., gt=0, lt=400)]
    BMI: Annotated[float, Field(..., gt=0, lt=50)]
    DiabetesPedigreeFunction: Annotated[int, Field(...)]
    Age: Annotated[int, Field(..., gt=0, lt=100)]


# class UserInput(BaseModel):
#     PendingDeprecationWarningregnencies: Annotated[int, Field(..., lt=17,description="Number of times the patient has been pregnant")]
#     Glucose: Annotated[int, Field(..., gt=0, lt=200, description="")]
#     BloodPressure: Annotated[int, Field(..., gt=0, lt=400, description="")]
#     SkinThickness: Annotated[int, Field(..., gt=0, lt=400, description="")]
#     Insulin: Annotated[int, Field(..., gt=0, lt=400, description="")]
#     BMI: Annotated[float, Field(..., gt=0, lt=400, description="")]
#     DiabetesPedigreeFunction: Annotated[float, Field(..., description="")]
#     Age: Annotated[int, Field(..., gt=0, lt=400, description="")]

    # class Config:
    #     # schema_extra = {  #v1
    #     json_schema_extra  = {   #v2
    #     "example": {
    #         "Pregnancies": 2,
    #         "Glucose": 120,
    #         "BloodPressure": 70,
    #         "SkinThickness": 25,
    #         "Insulin": 80,
    #         "BMI": 28.5,
    #         "DiabetesPedigreeFunction": 0.5,
    #         "Age": 35
    #     }
    # }