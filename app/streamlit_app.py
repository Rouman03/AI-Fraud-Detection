import streamlit as st
import requests
import plotly.graph_objects as go


st.set_page_config(
    page_title="AI Fraud Intelligence System",
    page_icon="🚨",
    layout="wide"
)


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
    background-color: #111827;
}

.stButton>button {
    background-color: #dc2626;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 12px 20px;
    font-size: 16px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


if "time" not in st.session_state:
    st.session_state.time = 12

if "amount" not in st.session_state:
    st.session_state.amount = 500

if "risk_level" not in st.session_state:
    st.session_state.risk_level = 3

if "velocity" not in st.session_state:
    st.session_state.velocity = 2

if "international" not in st.session_state:
    st.session_state.international = 0


def load_high_risk():

    st.session_state.time = 2
    st.session_state.amount = 9500
    st.session_state.risk_level = 10
    st.session_state.velocity = 10
    st.session_state.international = 1


st.sidebar.title("Transaction Controls")

time = st.sidebar.slider(
    "Transaction Hour",
    min_value=0,
    max_value=24,
    step=1,
    key="time"
)

amount = st.sidebar.slider(
    "Transaction Amount",
    min_value=1,
    max_value=10000,
    step=100,
    key="amount"
)

risk_level = st.sidebar.slider(
    "Anomaly Risk Level",
    min_value=1,
    max_value=10,
    step=1,
    key="risk_level"
)

velocity = st.sidebar.slider(
    "Transaction Velocity",
    min_value=1,
    max_value=10,
    step=1,
    key="velocity"
)

international = st.sidebar.selectbox(
    "International Transaction",
    [0, 1],
    key="international"
)

st.sidebar.button(
    "Load High-Risk Example",
    on_click=load_high_risk
)


st.title("AI Fraud Intelligence System")

st.write("""
Real-time fraud risk analysis using:
- Random Forest Classification
- Behavioral anomaly simulation
- Fraud probability scoring
- Risk intelligence insights
""")


if st.button("Analyze Transaction"):

    payload = {
        "Time": float(time),
        "Amount": float(amount),
        "Risk_Level": int(risk_level),
        "Transaction_Velocity": int(velocity),
        "International": int(international)
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload
        )

        result = response.json()

        fraud_probability = result[
            "fraud_probability"
        ]

        risk_category = result[
            "risk_category"
        ]

        insights = result[
            "insights"
        ]

        
        st.subheader("Fraud Analysis Result")

        if risk_category == "HIGH RISK":

            st.error(
                f"⚠️ {risk_category}"
            )

        elif risk_category == "MEDIUM RISK":

            st.warning(
                f"⚠️ {risk_category}"
            )

        else:

            st.success(
                f"✅ {risk_category}"
            )

        
        st.metric(
            "Fraud Probability",
            f"{fraud_probability}%"
        )

        
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=fraud_probability,

            title={
                'text': "Fraud Risk Score"
            },

            gauge={
                'axis': {
                    'range': [0, 100]
                },

                'bar': {
                    'color': "red"
                }
            }
        ))

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        
        st.subheader(
            "AI Risk Insights"
        )

        if insights:

            for insight in insights:

                st.write(
                    f"- {insight}"
                )

        else:

            st.write(
                "- No major anomalies detected"
            )

    except Exception as e:

        st.error(
            f"API Connection Error: {e}"
        )


st.markdown("---")

st.caption(
    "Built using Streamlit, FastAPI, Random Forest, and Fraud Probability Analysis"
)