import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
import json

from src import config

# Load data
data = pd.read_csv(config.DATA_PATH)

X = data[['temperature', 'vibration', 'current']]
y = data['failure']

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=config.TEST_SIZE,
    random_state=config.RANDOM_STATE
)

# model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# cross validation (INDUSTRY PART)
cv_scores = cross_val_score(model, X, y, cv=5)

print("Accuracy:", accuracy)
print("CV Mean:", cv_scores.mean())

# save model
joblib.dump(model, config.MODEL_PATH)

# save metrics
metrics = {
    "accuracy": float(accuracy),
    "cv_mean": float(cv_scores.mean())
}

with open("models/metrics.json", "w") as f:
    json.dump(metrics, f)

print("Model saved + metrics stored")