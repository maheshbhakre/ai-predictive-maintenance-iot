import requests
import time
import random

API_URL = "http://127.0.0.1:5000/predict"

def generate_sensor_data():
    temperature = random.randint(30, 80)
    vibration = round(random.uniform(0.2, 2.0), 2)
    current = random.randint(5, 15)

    return temperature, vibration, current

while True:
    temp, vib, curr = generate_sensor_data()

    payload = {
        "temperature": temp,
        "vibration": vib,
        "current": curr
    }

    response = requests.post(API_URL, json=payload)

    print("\nSensor Data:")
    print(f"Temp={temp}, Vibration={vib}, Current={curr}")

    if response.status_code == 200:
        print("AI Prediction:", response.json()["Prediction"])
    else:
        print("API Error")

    time.sleep(5)