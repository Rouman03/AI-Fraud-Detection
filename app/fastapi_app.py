from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model
model = joblib.load("models/random_forest.pkl")

app = FastAPI()

# Input schema
class Transaction(BaseModel):
    Time: float
    Amount: float

# Home route
@app.get("/")
def home():
    return {"message": "Fraud Detection API Running Successfully"}

# Prediction route
@app.post("/predict")
def predict(transaction: Transaction):

    # Create full feature array
    features = np.zeros((1, 30))

    # Add values
    features[0][0] = transaction.Time
    features[0][-1] = transaction.Amount

    # Predict
    prediction = int(model.predict(features)[0])

    # Probability
    probability = float(model.predict_proba(features)[0][1])

    return {
        "prediction": prediction,
        "fraud_probability": probability
    }