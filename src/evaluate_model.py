import pandas as pd
import joblib
import json
import os

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/data.csv")

X = data[["temperature", "vibration", "current"]]
y = data["failure"]

# Load trained model
model = joblib.load("models/model.pkl")

# Predictions
y_pred = model.predict(X)

# Metrics
accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)
recall = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

print("\n📊 MODEL METRICS")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

# Save metrics
metrics = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1_score": float(f1)
}

with open("models/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("\n✅ metrics.json saved")

# Confusion Matrix
cm = confusion_matrix(y, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

# Save image
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/confusion_matrix.png")

print("✅ confusion_matrix.png saved")