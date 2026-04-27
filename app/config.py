# import json

# with open("models/columns.json") as f:
#     COLUMNS = json.load(f)

# with open("models/threshold.json") as f:
#     THRESHOLD_XGB = json.load(f)["threshold"]

# with open("models/thresshold_rfc.json") as f:
#     THRESHOLD_RFC = json.load(f)["threshold"]

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_json(filename):
    path = os.path.join(BASE_DIR, "models", filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ File not found: {path}")

    with open(path) as f:
        return json.load(f)

COLUMNS = load_json("columns.json")
THRESHOLD_RFC = load_json("thresshold_rfc.json")["threshold"]
THRESHOLD_XGB = load_json("threshold.json")["threshold"]