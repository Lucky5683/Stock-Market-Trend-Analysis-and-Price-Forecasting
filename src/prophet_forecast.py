import pandas as pd
import numpy as np

from prophet import Prophet
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

import matplotlib.pyplot as plt

# ----------------------------------
# LOAD DATA
# ----------------------------------

df = pd.read_csv(
    "data/processed/reliance_processed.csv"
)

df = df[
    ["Date", "Close"]
]

df.columns = [
    "ds",
    "y"
]

# ----------------------------------
# TRAIN TEST SPLIT
# ----------------------------------

train_size = int(
    len(df) * 0.8
)

train = df[:train_size]
test = df[train_size:]

# ----------------------------------
# TRAIN MODEL
# ----------------------------------

model = Prophet(
    daily_seasonality=True,
    yearly_seasonality=True
)

model.fit(train)

# ----------------------------------
# EVALUATION
# ----------------------------------

future_test = model.make_future_dataframe(
    periods=len(test)
)

forecast_test = model.predict(
    future_test
)

predictions = (
    forecast_test["yhat"]
    .tail(len(test))
)

mae = mean_absolute_error(
    test["y"],
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        test["y"],
        predictions
    )
)

mape = (
    np.mean(
        np.abs(
            (test["y"] - predictions)
            / test["y"]
        )
    )
) * 100

print("\nPROPHET MODEL REPORT")
print("=" * 50)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"MAPE : {mape:.2f}%")

# ----------------------------------
# TRAIN ON FULL DATA
# ----------------------------------

final_model = Prophet(
    daily_seasonality=True,
    yearly_seasonality=True
)

final_model.fit(df)

future = (
    final_model
    .make_future_dataframe(
        periods=30
    )
)

forecast = (
    final_model
    .predict(future)
)

# ----------------------------------
# SAVE FORECAST
# ----------------------------------

forecast[
    [
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]
].tail(30).to_csv(
    "reports/prophet_forecast.csv",
    index=False
)

# ----------------------------------
# FORECAST VISUALIZATION
# ----------------------------------

fig = final_model.plot(
    forecast
)

plt.title(
    "Prophet Forecast"
)

plt.show()

# ----------------------------------
# COMPONENTS
# ----------------------------------

fig2 = (
    final_model
    .plot_components(
        forecast
    )
)

plt.show()

forecast[
    [
        "ds",
        "yhat",
        "yhat_lower",
        "yhat_upper"
    ]
].tail(30).to_csv(
    "reports/prophet_forecast.csv",
    index=False
)