from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

print("API STARTING...")

app = Flask(__name__)

# Safe model path
model_path = os.path.join(os.getcwd(), "models", "model.pkl")

if not os.path.exists(model_path):
    print("Model not found. Train first!")
    exit()

model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        features = np.array([[data["temperature"], data["vibration"], data["current"]]])

        prediction = model.predict(features)[0]

        return jsonify({
            "prediction": "FAILURE" if prediction == 1 else "NORMAL"
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print("Flask running on http://127.0.0.1:5000")
    app.run(debug=True)