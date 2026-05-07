from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np


model = joblib.load("../models/random_forest.pkl")


app = FastAPI(
    title="AI Fraud Detection API",
    description="Real-Time Fraud Risk Analysis",
    version="3.0"
)


class Transaction(BaseModel):
    Time: float
    Amount: float
    Risk_Level: int
    Transaction_Velocity: int
    International: int


@app.get("/")
def home():

    return {
        "message": "AI Fraud Detection API Running Successfully"
    }


@app.post("/predict")
def predict(transaction: Transaction):

    
    features = np.zeros((1, 30))

    
    features[0][0] = transaction.Time
    features[0][-1] = transaction.Amount

    
    features[0][14] = -transaction.Risk_Level
    features[0][17] = -transaction.Transaction_Velocity
    features[0][12] = -transaction.International * 5

    
    prediction = int(model.predict(features)[0])

    
    base_probability = float(
        model.predict_proba(features)[0][1]
    )

    
    boost = (
        (transaction.Risk_Level * 0.03)
        + (transaction.Transaction_Velocity * 0.02)
        + (transaction.International * 0.15)
    )

    
    if transaction.Amount > 5000:
        boost += 0.20

    fraud_probability = min(
        base_probability + boost,
        1.0
    )

    
    if fraud_probability >= 0.7:

        risk_category = "HIGH RISK"

    elif fraud_probability >= 0.3:

        risk_category = "MEDIUM RISK"

    else:

        risk_category = "LOW RISK"

   
    insights = []

    if transaction.Amount > 5000:

        insights.append(
            "Large transaction amount detected"
        )

    if transaction.International == 1:

        insights.append(
            "International transaction detected"
        )

    if transaction.Transaction_Velocity > 7:

        insights.append(
            "High transaction velocity detected"
        )

    if transaction.Risk_Level > 7:

        insights.append(
            "High anomaly behavior detected"
        )

    if fraud_probability > 0.8:

        insights.append(
            "Transaction strongly resembles known fraud patterns"
        )

    
    if fraud_probability >= 0.5:
        prediction = 1
    else:
        prediction = 0

    
    return {

        "prediction": prediction,

        "fraud_probability": round(
            fraud_probability * 100,
            2
        ),

        "risk_category": risk_category,

        "insights": insights
    }