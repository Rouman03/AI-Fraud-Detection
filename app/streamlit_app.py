import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="AI Fraud Detection Dashboard",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #050816;
    color: white;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #1c1f2e;
}

.stButton>button {
    background-color: #262730;
    color: white;
    border-radius: 10px;
    border: 1px solid #444;
    padding: 10px 20px;
}

.stNumberInput input {
    background-color: #0f172a;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Transaction Input")

time = st.sidebar.number_input(
    "Transaction Time",
    min_value=0.0,
    value=5.0
)

amount = st.sidebar.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=210.0
)

# Main title
st.title("AI Fraud Detection Dashboard")

st.write(
    "This system predicts whether a transaction is fraudulent using Machine Learning and Random Forest classification."
)

# Predict button
if st.sidebar.button("Predict Transaction"):

    payload = {
        "Time": time,
        "Amount": amount
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        prediction = result["prediction"]
        probability = result["fraud_probability"]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("Fraudulent Transaction Detected")
        else:
            st.success("Legitimate Transaction")

        st.write(f"Fraud Probability: {probability:.4f}")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")

st.markdown("---")

st.caption(
    "Built using Streamlit, Scikit-learn, FastAPI, SHAP, and Random Forest"
)