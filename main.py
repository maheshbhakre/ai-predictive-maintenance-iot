import requests
import random
import time
from src.logger import log_prediction

while True:
    sensor_data = {
        "temperature": random.randint(30, 80),
        "vibration": round(random.uniform(0.2, 2.0), 2),
        "current": random.randint(5, 15)
    }

    print("\nSensor Data:")
    print(sensor_data)

    response = requests.post("http://127.0.0.1:5000/predict", json=sensor_data)

    result = response.json()

    if result["prediction"] == 1:
        print("AI Prediction: Machine failure predicted!")
    else:
        print("AI Prediction: Machine is running normally.")

    log_prediction(sensor_data, result["prediction"])

    time.sleep(2)
    