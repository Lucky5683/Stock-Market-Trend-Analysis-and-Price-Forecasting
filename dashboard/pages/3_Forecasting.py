import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(
    page_title="Forecasting",
    layout="wide"
)

st.title("Forecasting")

# =====================================================
# LOAD DATA
# =====================================================

results = pd.read_csv(
    "reports/model_comparison.csv"
)

arima = pd.read_csv(
    "reports/arima_forecast.csv"
)

prophet = pd.read_csv(
    "reports/prophet_forecast.csv"
)

lstm = pd.read_csv(
    "reports/lstm_forecast.csv"
)

# =====================================================
# MODEL PERFORMANCE
# =====================================================

st.subheader(
    "Model Performance Comparison"
)

st.dataframe(
    results,
    use_container_width=True
)

best_model = (
    results
    .sort_values("MAPE")
    .iloc[0]
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Best Model",
        best_model["Model"]
    )

with col2:
    st.metric(
        "MAPE",
        f"{best_model['MAPE']:.2f}%"
    )

with col3:
    st.metric(
        "RMSE",
        f"{best_model['RMSE']:.2f}"
    )

# =====================================================
# MAPE COMPARISON
# =====================================================

st.subheader(
    "Forecast Error Comparison"
)

fig_bar = px.bar(
    results,
    x="Model",
    y="MAPE",
    title="MAPE by Model"
)

st.plotly_chart(
    fig_bar,
    use_container_width=True
)

# =====================================================
# ARIMA FORECAST
# =====================================================

st.subheader(
    "ARIMA Forecast"
)

fig_arima = go.Figure()

fig_arima.add_trace(
    go.Scatter(
        y=arima["Forecast"],
        mode="lines",
        name="ARIMA"
    )
)

fig_arima.update_layout(
    height=400
)

st.plotly_chart(
    fig_arima,
    use_container_width=True
)

# =====================================================
# PROPHET FORECAST
# =====================================================

st.subheader(
    "Prophet Forecast"
)

fig_prophet = go.Figure()

fig_prophet.add_trace(
    go.Scatter(
        y=prophet["yhat"],
        mode="lines",
        name="Prophet"
    )
)

fig_prophet.update_layout(
    height=400
)

st.plotly_chart(
    fig_prophet,
    use_container_width=True
)

# =====================================================
# LSTM FORECAST
# =====================================================

st.subheader(
    "LSTM Forecast"
)

fig_lstm = go.Figure()

fig_lstm.add_trace(
    go.Scatter(
        y=lstm["Forecast"],
        mode="lines",
        name="LSTM"
    )
)

fig_lstm.update_layout(
    height=400
)

st.plotly_chart(
    fig_lstm,
    use_container_width=True
)

# =====================================================
# INTERPRETATION
# =====================================================

st.subheader(
    "Forecast Interpretation"
)

st.write(
    """
    LSTM achieved the strongest predictive
    performance among all evaluated models.

    ARIMA captured long-term trend behaviour
    but produced higher forecast error.

    Prophet delivered the weakest performance
    on this dataset.

    Based on model evaluation metrics,
    LSTM is the recommended forecasting model
    for this stock.
    """
)