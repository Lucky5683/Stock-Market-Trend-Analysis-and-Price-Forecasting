import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Risk Analysis",
    layout="wide"
)

st.title("Risk Analysis")

risk = pd.read_csv(
    "reports/risk_report.csv"
)

metrics = dict(
    zip(
        risk["Metric"],
        risk["Value"]
    )
)

# =====================================
# KPI SECTION
# =====================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Annual Return",
    f"{metrics['Annualized Return']:.2%}"
)

col2.metric(
    "Volatility",
    f"{metrics['Annualized Volatility']:.2%}"
)

col3.metric(
    "Sharpe Ratio",
    f"{metrics['Sharpe Ratio']:.2f}"
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Max Drawdown",
    f"{metrics['Maximum Drawdown']:.2%}"
)

col5.metric(
    "VaR (95%)",
    f"{metrics['Value at Risk (95%)']:.2%}"
)

col6.metric(
    "Risk Score",
    f"{metrics['Risk Score']:.0f}/100"
)

st.divider()

# =====================================
# RISK CLASSIFICATION
# =====================================

risk_score = metrics["Risk Score"]

if risk_score >= 80:
    risk_category = "Low Risk"

elif risk_score >= 60:
    risk_category = "Moderate Risk"

elif risk_score >= 40:
    risk_category = "High Risk"

else:
    risk_category = "Very High Risk"

st.subheader(
    "Risk Classification"
)

st.write(
    f"Current Classification: **{risk_category}**"
)

st.divider()

# =====================================
# VISUALIZATION
# =====================================

plot_df = pd.DataFrame({
    "Metric": [
        "Volatility",
        "Sharpe Ratio",
        "Risk Score"
    ],
    "Value": [
        metrics["Annualized Volatility"],
        metrics["Sharpe Ratio"],
        metrics["Risk Score"]
    ]
})

fig = px.bar(
    plot_df,
    x="Metric",
    y="Value",
    title="Risk Metrics Overview"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =====================================
# INTERPRETATION
# =====================================

st.subheader(
    "Interpretation"
)

st.write(
    """
    The stock demonstrates moderate-to-high
    volatility with a historical maximum drawdown
    exceeding 40%.

    The Sharpe Ratio indicates that returns have
    not been exceptionally high relative to the
    risk undertaken.

    Based on the composite risk score, the stock
    falls into the High Risk category.
    """
)