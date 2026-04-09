from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("models/model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([
        [data["temperature"], data["vibration"], data["current"]]
    ])

    prediction = model.predict(features)

    result = "Failure" if prediction[0] == 1 else "Normal"

    return jsonify({"Prediction": result})

app.run(debug=True)