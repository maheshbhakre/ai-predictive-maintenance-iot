# src/train_model.py

import pandas as pd
import joblib
import json
import os

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# 1. Load Data
# -------------------------
data = pd.read_csv("data/data.csv")

X = data[["temperature", "vibration", "current"]]
y = data["failure"]

# -------------------------
# 2. Train-Test Split (IMPORTANT)
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# 3. Model Training
# -------------------------
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# -------------------------
# 4. Prediction
# -------------------------
y_pred = model.predict(X_test)

# -------------------------
# 5. Metrics
# -------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n📊 MODEL PERFORMANCE")
print(f"Accuracy : {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall   : {recall:.4f}")
print(f"F1 Score : {f1:.4f}")

# -------------------------
# 6. Cross Validation (REAL PROOF)
# -------------------------
cv_scores = cross_val_score(model, X, y, cv=5)

print(f"Cross Validation Mean: {cv_scores.mean():.4f}")

# -------------------------
# 7. Save Metrics
# -------------------------
metrics = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1_score": float(f1),
    "cv_mean": float(cv_scores.mean())
}

os.makedirs("models", exist_ok=True)

with open("models/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print("✅ metrics.json saved")

# -------------------------
# 8. Confusion Matrix (Better Visualization)
# -------------------------
cm = confusion_matrix(y_test, y_pred)

plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

os.makedirs("images", exist_ok=True)
plt.savefig("images/confusion_matrix.png")
plt.close()

print("✅ confusion_matrix.png saved")

# -------------------------
# 9. Save Model
# -------------------------
joblib.dump(model, "models/model.pkl")

print("✅ Model saved successfully")