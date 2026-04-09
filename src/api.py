from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("models/model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    features = np.array([
        [data["temperature"], data["vibration"], data["current"]]
    ])

    prediction = model.predict(features)

    result = "Machine failure predicted!" if prediction[0] == 1 else "Machine is running normally."

    return jsonify({"Prediction": result})

if __name__ == '__main__':
    app.run(debug=True)