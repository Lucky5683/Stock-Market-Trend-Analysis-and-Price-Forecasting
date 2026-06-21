import streamlit as st

st.set_page_config(
    page_title="Stock Market Intelligence Platform",
    layout="wide"
)

st.title(
    "Stock Market Intelligence Platform"
)

st.markdown("""
### Forecasting, Technical Analysis and Risk Analytics

This platform provides:

- Historical market analysis
- Technical indicator evaluation
- Risk assessment
- Time-series forecasting
- Model comparison

---

### Forecasting Models

| Model | MAPE |
|--------|--------:|
| Prophet | 17.08% |
| ARIMA | 9.48% |
| LSTM | 6.73% |

**Best Performing Model:** LSTM

---

Navigate using the sidebar.
""")