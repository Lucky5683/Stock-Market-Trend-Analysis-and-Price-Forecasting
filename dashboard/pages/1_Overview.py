import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Overview",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(
    "data/processed/reliance_features.csv"
)

results = pd.read_csv(
    "reports/model_comparison.csv"
)

latest = df.iloc[-1]

best_model = (
    results
    .sort_values("MAPE")
    .iloc[0]
)

# =====================================================
# TITLE
# =====================================================

st.title("Overview")

st.markdown(
    """
    Executive summary of market conditions,
    forecasting performance and technical indicators.
    """
)

# =====================================================
# KPI SECTION
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Closing Price",
        f"₹{latest['Close']:.2f}"
    )

with col2:
    st.metric(
        "RSI",
        f"{latest['RSI']:.2f}"
    )

with col3:
    st.metric(
        "Trend Score",
        f"{latest['Trend_Score']}/100"
    )

with col4:
    st.metric(
        "Volatility",
        f"{latest['Volatility_20']:.4f}"
    )

st.divider()

# =====================================================
# MARKET STATUS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Market Regime",
        latest["Market_Regime"]
    )

with col2:
    st.metric(
        "Investment Signal",
        latest["Recommendation"]
    )

with col3:
    st.metric(
        "Best Model",
        best_model["Model"]
    )

st.divider()

# =====================================================
# PRICE CHART
# =====================================================

st.subheader(
    "Closing Price Trend"
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Close"],
        mode="lines",
        name="Close Price"
    )
)

fig.update_layout(
    height=500,
    xaxis_title="Date",
    yaxis_title="Price"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# MODEL PERFORMANCE
# =====================================================

st.subheader(
    "Forecasting Performance"
)

st.dataframe(
    results,
    use_container_width=True
)

st.divider()

# =====================================================
# DATASET INFORMATION
# =====================================================

st.subheader(
    "Dataset Information"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Rows",
        len(df)
    )

with col2:
    st.metric(
        "Columns",
        len(df.columns)
    )

with col3:
    st.metric(
        "Features",
        21
    )

st.write(
    f"Date Range: {df['Date'].min()} to {df['Date'].max()}"
)