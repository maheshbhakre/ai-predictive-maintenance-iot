# 🤖 AI-Powered Predictive Maintenance System for IoT Devices

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.4-green?style=flat-square)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2-orange?style=flat-square)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

This project implements an **AI-powered predictive maintenance system** using simulated IoT sensor data.
It predicts machine failures **before they occur**, enabling proactive maintenance and reducing downtime.

Instead of relying on physical hardware, this project uses:

* 📊 **Simulated sensor data**
* 🤖 **Machine Learning models**
* 🌐 **Flask API for real-time prediction**

---

## 🛠 Problem Statement

Traditional maintenance systems are:

* Reactive (fix after failure)
* Expensive
* Inefficient

This project solves:

* Early failure detection
* Reduced downtime
* Cost optimization
* Intelligent decision-making using AI

---

## 🏭 Industry Relevance

Predictive maintenance is widely used in:

| Industry      | Application                |
| ------------- | -------------------------- |
| Manufacturing | Detect overheating motors  |
| Factories     | Monitor conveyor systems   |
| Power Plants  | Predict turbine failures   |
| Automotive    | Engine fault prediction    |
| Aviation      | Aircraft health monitoring |

### 📊 Real Impact

* 🔻 5–10% reduction in maintenance cost
* ⏱ 15% less unplanned downtime
* 📈 5–20% productivity increase

Used by companies like: **Siemens, GE, IBM, Tesla, Bosch**

---

## ⚙ Tech Stack

* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-learn (Random Forest)
* **API:** Flask
* **Visualization:** Matplotlib, Seaborn
* **Model Storage:** Joblib

---

## 📊 Dataset

This project uses:

* Simulated IoT sensor data (CSV format)

### Features:

* Temperature
* Vibration
* Current

### Target:

* `failure` (0 = Normal, 1 = Failure)

---

## 🏗 Architecture

### 🔄 Workflow

```
Sensor Simulation → Data Preprocessing → Feature Engineering → ML Model (Random Forest)
→ Prediction (Failure / Normal) → Alert System → Visualization
```

### 🔧 Modules

* `sensor_sim.py` → Generates IoT sensor data
* `train_model.py` → Trains ML model
* `api.py` → Provides real-time predictions
* `main.py` → Runs simulation & connects all components

---

## 📁 Folder Structure

```
AI-Predictive-Maintenance-IoT/
├── data/
│ └── data.csv
├── models/
│ └── model.pkl
├── src/
│ ├── train_model.py
│ └── api.py
├── images/
│ ├── training.png
│ ├── api.png
│ ├── prediction.png
│ ├── structure.png
│ └── model.png
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙ Installation & Setup

### ✅ Requirements

* Python 3.10+

### 🔧 Steps

```bash
# Clone repository
git clone https://github.com/maheshbhakre/AI-Predictive-Maintenance-IoT.git
cd AI-Predictive-Maintenance-IoT

# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🖥 Usage

### 1️⃣ Train Model

```bash
python src/train_model.py
```

### 2️⃣ Start API

```bash
python src/api.py
```

### 3️⃣ Run Simulation

```bash
python main.py
```

---

## 📊 Results

* Real-time sensor simulation
* AI-based failure prediction
* Automated decision logic

### Metrics:

* Accuracy
* Precision
* Recall

---

## 📸 Screenshots / Outputs

### 🔹 Model Training
![Training](images/training.png)

### 🔹 API Running
![API](images/api.png)

### 🔹 Prediction Output
![Prediction](images/prediction.png)

### 🔹 Project Structure
![Structure](images/structure.png)

### 🔹 Model File
![Model](images/model.png)
---

## 🧠 Learning Outcomes

* IoT data simulation
* Machine learning pipeline
* Model training & evaluation
* API development using Flask
* Real-time prediction systems

---

## 🚀 Future Improvements

* LSTM for time-series prediction
* Real IoT hardware integration
* Cloud deployment (AWS / Azure IoT)
* Real-time dashboard

---

## 👨‍💻 Author

Student Project – Built for:

* 💼 Placements
* 🎯 Internships
* 📊 Portfolio

---

## ⭐ Support

If you find this useful:

* Star ⭐ the repo
* Fork 🍴 for your own version

---
