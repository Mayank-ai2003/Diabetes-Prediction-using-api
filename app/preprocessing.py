# import numpy as np
# import json

# with open("models/imputer_rfc.json") as f:
#     IMPUTER = json.load(f)

# with open("models/scaler_rfc.json") as f:
#     SCALER = json.load(f)



import os
import json
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(filename):
    path = os.path.join(BASE_DIR, "models", filename)
    with open(path) as f:
        return json.load(f)

IMPUTER = load_json("imputer_rfc.json")
SCALER = load_json("scaler_rfc.json")



def preprocess(data):
    arr = np.array(data, dtype=np.float32)

    # Imputation
    for i in range(len(arr)):
        # if np.isnan(arr[i]):
        # if np.isnan(arr[i]) or arr[i] is None:
        if arr[i] is None or (isinstance(arr[i], float) and np.isnan(arr[i])):
            arr[i] = IMPUTER["statistics"][i]

    # Scaling
    # arr = (arr - SCALER["center"]) / SCALER["scale"]

    center = np.array(SCALER["center"], dtype=np.float32)
    scale = np.array(SCALER["scale"], dtype=np.float32)

    arr = (arr - center) / scale

    return arr.reshape(1, -1)