import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Technical Analysis",
    layout="wide"
)

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(
    "data/processed/reliance_features.csv"
)

st.title("Technical Analysis")

st.markdown(
    """
    Technical indicators derived from historical
    market data.
    """
)

# =====================================================
# PRICE + MOVING AVERAGES
# =====================================================

st.subheader(
    "Price Trend and Moving Averages"
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Close"],
        name="Close Price"
    )
)

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["MA20"],
        name="MA20"
    )
)

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["MA50"],
        name="MA50"
    )
)

fig.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["MA200"],
        name="MA200"
    )
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# BOLLINGER BANDS
# =====================================================

st.subheader(
    "Bollinger Bands"
)

fig_bb = go.Figure()

fig_bb.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Close"],
        name="Close"
    )
)

fig_bb.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["BB_Upper"],
        name="Upper Band"
    )
)

fig_bb.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["BB_Middle"],
        name="Middle Band"
    )
)

fig_bb.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["BB_Lower"],
        name="Lower Band"
    )
)

fig_bb.update_layout(
    height=500
)

st.plotly_chart(
    fig_bb,
    use_container_width=True
)

# =====================================================
# RSI
# =====================================================

st.subheader(
    "Relative Strength Index (RSI)"
)

fig_rsi = go.Figure()

fig_rsi.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["RSI"],
        name="RSI"
    )
)

fig_rsi.add_hline(
    y=70,
    line_dash="dash"
)

fig_rsi.add_hline(
    y=30,
    line_dash="dash"
)

fig_rsi.update_layout(
    height=400
)

st.plotly_chart(
    fig_rsi,
    use_container_width=True
)

# =====================================================
# MACD
# =====================================================

st.subheader(
    "MACD"
)

fig_macd = go.Figure()

fig_macd.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["MACD"],
        name="MACD"
    )
)

fig_macd.add_trace(
    go.Scatter(
        x=df["Date"],
        y=df["Signal_Line"],
        name="Signal Line"
    )
)

fig_macd.update_layout(
    height=400
)

st.plotly_chart(
    fig_macd,
    use_container_width=True
)

# =====================================================
# MACD HISTOGRAM
# =====================================================

st.subheader(
    "MACD Histogram"
)

fig_hist = go.Figure()

fig_hist.add_trace(
    go.Bar(
        x=df["Date"],
        y=df["MACD_Histogram"],
        name="Histogram"
    )
)

fig_hist.update_layout(
    height=400
)

st.plotly_chart(
    fig_hist,
    use_container_width=True
)

# =====================================================
# MARKET SUMMARY
# =====================================================

latest = df.iloc[-1]

st.subheader(
    "Current Technical State"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "RSI",
        f"{latest['RSI']:.2f}"
    )

with col2:
    st.metric(
        "Trend Score",
        f"{latest['Trend_Score']}/100"
    )

with col3:
    st.metric(
        "Signal",
        latest["Recommendation"]
    )