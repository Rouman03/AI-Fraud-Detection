# AI Fraud Detection System

An end-to-end Machine Learning based Fraud Detection System built using Python, Scikit-learn, FastAPI, Streamlit, Docker, and SHAP Explainability.

## Project Overview

This project predicts whether a financial transaction is fraudulent or legitimate using Machine Learning classification models. The system includes:

- Data preprocessing and feature engineering
- Exploratory Data Analysis (EDA)
- Fraud detection model training
- Model evaluation
- SHAP explainability
- FastAPI backend API
- Streamlit interactive dashboard
- Docker containerization
- Monitoring setup

---

# Project Structure

```text
Fraud_Detection/
│
├── app/
│   ├── fastapi_app.py
│   └── streamlit_app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── deployment/
│   ├── Dockerfile
│   ├── docker_compose.yml
│   └── requirements.txt
│
├── models/
│   ├── logistic_regression.pkl
│   ├── random_forest.pkl
│   └── scaler.pkl
│
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_visualization.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_model_evaluation.ipynb
│   └── 06_shap_explainability.ipynb
│
├── reports/
│   ├── figures/
│   └── model_report.pdf
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SHAP
- FastAPI
- Streamlit
- Docker
- Joblib

---

# Features

- Fraud prediction using Random Forest Classifier
- Interactive Streamlit Dashboard
- REST API using FastAPI
- SHAP explainability visualization
- Docker deployment support
- Model evaluation reports
- Confusion matrix visualization
- Fraud probability scoring

---

# Dataset

The project uses a financial transaction dataset containing anonymized transaction features such as:

- Time
- Amount
- V1 to V28 transformed features
- Class label:
  - 0 → Legitimate Transaction
  - 1 → Fraudulent Transaction

---

# Machine Learning Workflow

## 1. Data Cleaning

- Removed missing values
- Checked duplicates
- Data preprocessing

## 2. Exploratory Data Analysis

- Fraud distribution analysis
- Transaction amount visualization
- Correlation heatmaps

## 3. Feature Engineering

- Feature scaling using StandardScaler
- Data balancing using SMOTE

## 4. Model Training

Models trained:

- Logistic Regression
- Random Forest Classifier

## 5. Model Evaluation

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

## 6. Explainability

- SHAP summary plots
- Feature importance visualization

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run FastAPI Backend

```bash
uvicorn app.fastapi_app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Run Streamlit Dashboard

```bash
streamlit run app/streamlit_app.py
```

Dashboard runs on:

```text
http://localhost:8501
```

---

# Docker Deployment

## Build Docker Container

```bash
docker compose -f deployment/docker_compose.yml build --no-cache
```

## Run Docker Container

```bash
docker compose -f deployment/docker_compose.yml up
```

---

# Model Outputs

Generated outputs include:

- Trained ML models (.pkl)
- SHAP explainability plots
- Confusion matrix visualizations
- PDF model evaluation report

---

# Monitoring

Basic monitoring can be added using:

- Logging
- Prediction tracking
- API monitoring
- Container monitoring using Docker

Future improvements:

- Prometheus integration
- Grafana dashboards
- Real-time fraud alerts

---

# Future Enhancements

- Deep Learning based fraud detection
- Real-time streaming transactions
- Cloud deployment
- User authentication
- Advanced monitoring dashboard
- Automated retraining pipeline

---

# Author

Rouman Syed

Internship Project – AI Fraud Detection System
