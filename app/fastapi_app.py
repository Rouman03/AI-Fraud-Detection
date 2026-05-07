from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# -----------------------------
# LOAD MODEL
# -----------------------------
model = joblib.load("../models/random_forest.pkl")

# -----------------------------
# FASTAPI APP
# -----------------------------
app = FastAPI(
    title="AI Fraud Detection API",
    description="Real-Time Fraud Risk Analysis",
    version="3.0"
)

# -----------------------------
# INPUT SCHEMA
# -----------------------------
class Transaction(BaseModel):
    Time: float
    Amount: float
    Risk_Level: int
    Transaction_Velocity: int
    International: int

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.get("/")
def home():

    return {
        "message": "AI Fraud Detection API Running Successfully"
    }

# -----------------------------
# PREDICTION ROUTE
# -----------------------------
@app.post("/predict")
def predict(transaction: Transaction):

    # Create base feature array
    features = np.zeros((1, 30))

    # Real dataset features
    features[0][0] = transaction.Time
    features[0][-1] = transaction.Amount

    # Simulated PCA anomaly behavior
    features[0][14] = -transaction.Risk_Level
    features[0][17] = -transaction.Transaction_Velocity
    features[0][12] = -transaction.International * 5

    # Base model prediction
    prediction = int(model.predict(features)[0])

    # Base probability from model
    base_probability = float(
        model.predict_proba(features)[0][1]
    )

    # -----------------------------
    # DYNAMIC FRAUD BOOSTING
    # -----------------------------
    boost = (
        (transaction.Risk_Level * 0.03)
        + (transaction.Transaction_Velocity * 0.02)
        + (transaction.International * 0.15)
    )

    # Extra boost for huge transactions
    if transaction.Amount > 5000:
        boost += 0.20

    # Final fraud probability
    fraud_probability = min(
        base_probability + boost,
        1.0
    )

    # -----------------------------
    # RISK CATEGORY
    # -----------------------------
    if fraud_probability >= 0.7:

        risk_category = "HIGH RISK"

    elif fraud_probability >= 0.3:

        risk_category = "MEDIUM RISK"

    else:

        risk_category = "LOW RISK"

    # -----------------------------
    # AI INSIGHTS
    # -----------------------------
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

    # -----------------------------
    # FINAL PREDICTION OVERRIDE
    # -----------------------------
    if fraud_probability >= 0.5:
        prediction = 1
    else:
        prediction = 0

    # -----------------------------
    # RETURN RESPONSE
    # -----------------------------
    return {

        "prediction": prediction,

        "fraud_probability": round(
            fraud_probability * 100,
            2
        ),

        "risk_category": risk_category,

        "insights": insights
    }