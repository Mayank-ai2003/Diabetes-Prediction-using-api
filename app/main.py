from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.schema import UserInput
from app.predictor import predict_diabetes

app = FastAPI(
    title="Diabetes Prediction API",
    desciption="ML-powered diabetes risk prediction system",
    version="1.0"
)

@app.get('/home')
def home():
    return {"message" : "Diabetes prediction API is running....."}

@app.post('/predict')
def predict(input_data: UserInput):

    result = predict_diabetes(input_data.dict())
    return JSONResponse(status_code=200, content=result)


# Diabetes_api_ONNX -----> integrated terminal then run/
# uvicorn app.main:app --reload

# file_name ---> testing3_with_ONNX

# {
#   "Pregnancies": 0,
#   "Glucose": 130,
#   "BloodPressure": 120,
#   "SkinThickness": 100,
#   "Insulin": 100,
#   "BMI": 30,
#   "DiabetesPedigreeFunction": 1,
#   "Age": 32
# }