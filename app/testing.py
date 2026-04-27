# import pandas as pd

# from fastapi import FastAPI,HTTPException
# from fastapi.responses import JSONResponse

# from pydantic import BaseModel, Field, compute_field
# from typing import Literal,Annotated

# import joblib

# # ----------------------- importing model, columns and thresshold frequency

# with open(r'E:\MultipleDiseasePrediction[Human]\Diabetes\diabetes\Early_prediction\Final_model\diabetes_model_xgb.pkl','r') as f:
#     model = joblib.load(f)

# with open(r'','r') as col:
#     DIABETES_COLUMNS = joblib.load(col)

# with open(r'','r') as thresshold:
#     DIABETES_THRESSHOLD = joblib.load(thresshold)


# app = FastAPI()

# # class UserDetail():

# # ------------------------ pydanctic model to validate the input data

# class UserInput(BaseModel):
#     pregnencies: Annotated[int, Field(..., lt=17,description="Number of times the patient has been pregnant")]
#     glucose: Annotated[int, Field(..., gt=0, lt=200, description="")]
#     blood_pressure: Annotated[int, Field(..., gt=0, lt=400, description="")]
#     skin_thickness: Annotated[int, Field(..., gt=0, lt=400, description="")]
#     insulin: Annotated[int, Field(..., gt=0, lt=400, description="")]
#     bmi: Annotated[float, Field(..., gt=0, lt=400, description="")]
#     DiabetesPedigreeFunction: Annotated[float, Field(..., description="")]
#     age: Annotated[int, Field(..., gt=0, lt=400, description="")]


# # ------------------------ prediction router

# @app.post("/predict")
# def predict_diabetes(data: UserInput):

#     data = pd.DataFreame([data], columns=DIABETES_COLUMNS)
    
#     pred = model.predict(data)
#     prob = model.predict_proba(data)[0][1]
#     risk = "High Risk" if prob > DIABETES_THRESSHOLD else "Low Risk"

#     return JSONResponse(status_code=200, content={
#         "prediction":pred,
#         "prediction probability":prob,
#         "Risk":risk,
#     })