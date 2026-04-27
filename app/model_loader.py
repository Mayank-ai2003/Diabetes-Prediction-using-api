import os
import onnxruntime as rt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_model(model_name):
    path = os.path.join(BASE_DIR, "models", model_name)

    print(f"Loading model from: {path}")  # DEBUG

    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Model not found at {path}")

    return rt.InferenceSession(path, providers=["CPUExecutionProvider"])



session_rfc = load_model("diabetes_rfc.onnx")
input_name_rfc = session_rfc.get_inputs()[0].name

session_xgb = load_model("diabetes_xgb.onnx")
input_name_xgb = session_rfc.get_inputs()[0].name



# import onnxruntime as rt

# session_xgb = rt.InferenceSession("models/diabetes_xgb.onnx")
# input_name_xgb = session_xgb.get_inputs()[0].name

# session_rfc = rt.InferenceSession("model/diabetes_rfc.onnx")
# input_name_rfc = session_rfc.get_inputs()[0].name