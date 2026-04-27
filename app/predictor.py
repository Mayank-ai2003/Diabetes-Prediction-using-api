from app.model_loader import session_xgb,session_rfc, input_name_xgb, input_name_rfc
from app.config import THRESHOLD_XGB, THRESHOLD_RFC, COLUMNS
from app.preprocessing import preprocess


def predict_diabetes(data):
    try:
        values = []
        for col in COLUMNS:
            if col not in data:
                raise ValueError(f"Missing column: {col}")
            values.append(data[col])

        arr = preprocess(values)

        output = session_rfc.run(None, {input_name_rfc: arr})

        outputs_info = session_rfc.get_outputs()

        if "prob" in outputs_info[1].name.lower():
            prob = float(output[1][0][1])
            label = int(output[0][0])
        else:
            prob = float(output[0][0][1])
            label = int(output[1][0])

        risk = "High Risk" if prob > THRESHOLD_RFC else "Low Risk"

        return {
            "prediction": label,
            "probability": prob,
            "risk": risk
        }

    except Exception as e:
        return {"error": str(e)}










# def predict_diabetes(data):
#     values = [data[col] for col in COLUMNS]

#     arr = preprocess(values)

#     output = session_rfc.run(None, {input_name_rfc: arr})

#     label = int(output[0][0])
#     prob = float(output[1][0][1])

#     risk = "High Risk" if prob > THRESHOLD_RFC else "Low Risk"

#     return {
#         "prediction": label,
#         "probability": prob,
#         "risk": risk
#     }






# import numpy as np
# from app.model_loader import session_xgb,session_rfc, input_name_xgb, input_name_rfc
# from app.config import THRESHOLD_XGB, THRESHOLD_RFC, COLUMNS

# def predict_diabetes(data):

#     values = [data[col] for col in COLUMNS]
#     arr = np.array([values], dtype=np.float32)

#     output = session_rfc.run(None, {input_name_rfc: arr})
    
#     pred = output[0][0]
#     prob = output[1][0][1]
#     risk = "High Risk" if prob > THRESHOLD_RFC else "Low Risk"

#     return {
#         "prediction":pred,
#         "prediction probability":float(prob),
#         "Risk":risk,
#     }
    
#     # return JSONResponse(status_code=200, content={
#     #     "prediction":pred,
#     #     "prediction probability":prob,
#     #     "Risk":risk,
#     # })