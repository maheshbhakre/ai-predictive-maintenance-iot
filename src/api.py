from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Safe path for Render / local
MODEL_PATH = os.path.join("models", "model.pkl")
model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return "AI Predictive Maintenance API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
        data["temperature"],
        data["vibration"],
        data["current"]
    ]])

    prediction = model.predict(features)[0]

    return jsonify({
        "prediction": int(prediction)
    })

# IMPORTANT for deployment
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)