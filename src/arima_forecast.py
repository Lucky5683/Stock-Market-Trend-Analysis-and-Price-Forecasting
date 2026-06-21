import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv(
    "data/processed/reliance_processed.csv"
)

data = df["Close"]

# ----------------------------------
# TRAIN TEST SPLIT
# ----------------------------------

train_size = int(
    len(data) * 0.8
)

train = data[:train_size]
test = data[train_size:]

# ----------------------------------
# TRAIN MODEL
# ----------------------------------

model = ARIMA(
    train,
    order=(5,1,0)
)

model_fit = model.fit()

# ----------------------------------
# EVALUATION
# ----------------------------------

predictions = model_fit.forecast(
    steps=len(test)
)

mae = mean_absolute_error(
    test,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        test,
        predictions
    )
)

mape = (
    np.mean(
        np.abs(
            (test - predictions)
            / test
        )
    )
) * 100

print("\nARIMA MODEL REPORT")
print("=" * 50)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"MAPE : {mape:.2f}%")

# ----------------------------------
# FUTURE FORECAST
# ----------------------------------

full_model = ARIMA(
    data,
    order=(5,1,0)
)

full_fit = full_model.fit()

future_forecast = full_fit.forecast(
    steps=30
)

print("\nNext 30-Day Forecast")
print("=" * 50)
print(future_forecast)

# ----------------------------------
# SAVE FORECAST
# ----------------------------------

forecast_df = pd.DataFrame({
    "Forecast": future_forecast
})

forecast_df.to_csv(
    "reports/arima_forecast.csv",
    index=False
)

# ----------------------------------
# PLOT
# ----------------------------------

plt.figure(figsize=(14,7))

plt.plot(
    data,
    label="Historical"
)

plt.plot(
    range(
        len(data),
        len(data)+30
    ),
    future_forecast,
    label="30-Day Forecast"
)

plt.title(
    "ARIMA Stock Forecast"
)

plt.xlabel("Trading Days")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.show()

forecast_df = pd.DataFrame({
    "Forecast": future_forecast
})

forecast_df.to_csv(
    "reports/arima_forecast.csv",
    index=False
)