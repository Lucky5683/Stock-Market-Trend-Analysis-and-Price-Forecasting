# Stock Market Intelligence Platform

A comprehensive stock market analytics and forecasting platform built using Python, Machine Learning, Deep Learning, and Streamlit.

The project performs end-to-end financial data analysis including:

* Historical stock data collection
* Data validation and preprocessing
* Technical indicator generation
* Risk analytics
* Time-series forecasting
* Interactive dashboard visualization

---

## Project Overview

This platform analyzes historical stock market data from Yahoo Finance and generates actionable insights through technical indicators, risk metrics, and forecasting models.

The project compares multiple forecasting approaches and identifies the most accurate model using evaluation metrics such as MAE, RMSE, and MAPE.

---

## Features

### Data Pipeline

* Automated stock data collection using Yahoo Finance
* Data validation
* Data preprocessing
* Missing value handling
* Duplicate detection

### Technical Analysis

* Moving Averages (20, 50, 200 Day)
* RSI (Relative Strength Index)
* MACD
* Bollinger Bands
* Daily Returns
* Volatility Analysis

### Market Intelligence

* Trend Score Engine
* Market Regime Detection
* Investment Recommendation Engine

### Risk Analytics

* Annualized Return
* Annualized Volatility
* Sharpe Ratio
* Maximum Drawdown
* Value at Risk (VaR)

### Forecasting Models

* ARIMA
* Prophet
* LSTM Neural Network

### Interactive Dashboard

* Overview Dashboard
* Technical Analysis Dashboard
* Forecasting Dashboard
* Risk Analysis Dashboard

---

## Project Structure

```text
Stock-Market-Forecasting/

├── dashboard/
│   ├── app.py
│   └── pages/
│       ├── 1_Overview.py
│       ├── 2_Technical_Analysis.py
│       ├── 3_Forecasting.py
│       └── 4_Risk_Analysis.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│   ├── model_comparison.csv
│   ├── risk_report.csv
│   ├── arima_forecast.csv
│   ├── prophet_forecast.csv
│   └── lstm_forecast.csv
│
├── src/
│   ├── data_fetch.py
│   ├── data_validator.py
│   ├── data_process.py
│   ├── feature_engineering.py
│   ├── eda_analysis.py
│   ├── risk_analysis.py
│   ├── arima_complete.py
│   ├── prophet_complete.py
│   └── lstm_forecast.py
│
├── requirements.txt
└── README.md
```

---

## Forecasting Performance

| Model   |    MAE |   RMSE |   MAPE |
| ------- | -----: | -----: | -----: |
| LSTM    |  36.14 |  43.98 |  2.53% |
| ARIMA   | 137.50 | 157.15 |  9.48% |
| Prophet | 246.79 | 274.10 | 17.08% |

### Best Performing Model

LSTM Neural Network

MAPE: 2.53%

---

## Risk Analysis Results

| Metric                |   Value |
| --------------------- | ------: |
| Annualized Return     |  16.30% |
| Annualized Volatility |  29.73% |
| Sharpe Ratio          |   0.346 |
| Maximum Drawdown      | -44.08% |
| VaR (95%)             |  -2.41% |
| Risk Score            |  45/100 |

Risk Category: High Risk

---

## Installation

```bash
git clone <repository-url>

cd Stock-Market-Forecasting

pip install -r requirements.txt
```

---

## Run Data Pipeline

```bash
python src/data_fetch.py

python src/data_validator.py

python src/data_process.py

python src/feature_engineering.py

python src/eda_analysis.py

python src/risk_analysis.py

python src/arima_complete.py

python src/prophet_complete.py

python src/lstm_forecast.py
```

---

## Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* TensorFlow
* Prophet
* Statsmodels
* Streamlit
* Plotly
* Yahoo Finance API

---

## Future Improvements

* Multi-stock support
* Real-time market data
* Portfolio optimization
* Sentiment analysis
* Transformer-based forecasting models
* Cloud deployment

---

## Author

Dinesh Kumar

B.Tech – Artificial Intelligence & Data Science

Apollo University
