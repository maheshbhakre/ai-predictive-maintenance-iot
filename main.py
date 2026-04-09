import requests
import time
import random

while True:
    temp = random.randint(30, 80)
    vib = round(random.uniform(0.2, 2.0), 2)
    curr = random.randint(5, 15)

    data = {
        "temperature": temp,
        "vibration": vib,
        "current": curr
    }

    res = requests.post("http://127.0.0.1:5000/predict", json=data)

    print("Sensor:", data)
    print("Prediction:", res.json())

    time.sleep(5)