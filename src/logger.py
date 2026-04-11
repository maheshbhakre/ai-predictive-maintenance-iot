# src/logger.py

import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/predictions.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_prediction(data, prediction):
    logging.info(f"{data} -> {prediction}")