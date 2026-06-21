import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Dense,
    LSTM
)

# =====================================================
# LOAD DATA
# =====================================================

print("\nLoading dataset...")

df = pd.read_csv(
    "data/processed/reliance_processed.csv"
)

data = df["Close"].values.reshape(-1, 1)

# =====================================================
# SCALING
# =====================================================

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(
    data
)

# =====================================================
# CREATE SEQUENCES
# =====================================================

sequence_length = 60

X = []
y = []

for i in range(
    sequence_length,
    len(scaled_data)
):

    X.append(
        scaled_data[
            i-sequence_length:i,
            0
        ]
    )

    y.append(
        scaled_data[i, 0]
    )

X = np.array(X)
y = np.array(y)

X = X.reshape(
    X.shape[0],
    X.shape[1],
    1
)

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

train_size = int(
    len(X) * 0.8
)

X_train = X[:train_size]
X_test = X[train_size:]

y_train = y[:train_size]
y_test = y[train_size:]

# =====================================================
# BUILD MODEL
# =====================================================

model = Sequential()

model.add(
    LSTM(
        50,
        return_sequences=True,
        input_shape=(60,1)
    )
)

model.add(
    LSTM(50)
)

model.add(
    Dense(1)
)

model.compile(
    optimizer="adam",
    loss="mean_squared_error"
)

# =====================================================
# TRAIN MODEL
# =====================================================

print("\nTraining LSTM...")

model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=32,
    verbose=1
)

# =====================================================
# PREDICTIONS
# =====================================================

predictions = model.predict(
    X_test
)

predictions = scaler.inverse_transform(
    predictions
)

actual = scaler.inverse_transform(
    y_test.reshape(-1,1)
)

# =====================================================
# EVALUATION
# =====================================================

mae = mean_absolute_error(
    actual,
    predictions
)

rmse = np.sqrt(
    mean_squared_error(
        actual,
        predictions
    )
)

mape = (
    np.mean(
        np.abs(
            (actual - predictions)
            / actual
        )
    )
) * 100

print("\nLSTM EVALUATION")
print("=" * 60)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"MAPE : {mape:.2f}%")

# =====================================================
# FUTURE FORECAST
# =====================================================

future_input = scaled_data[-sequence_length:]

future_predictions = []

current_batch = future_input.reshape(
    1,
    sequence_length,
    1
)

for _ in range(30):

    next_pred = model.predict(
        current_batch,
        verbose=0
    )

    future_predictions.append(
        next_pred[0][0]
    )

    current_batch = np.concatenate(
        (
            current_batch[:, 1:, :],
            next_pred.reshape(1, 1, 1)
        ),
        axis=1
    )

future_predictions = np.array(
    future_predictions
).reshape(-1, 1)

future_predictions = scaler.inverse_transform(
    future_predictions
)

forecast_df = pd.DataFrame({
    "Forecast": future_predictions.flatten()
})

forecast_df.to_csv(
    "reports/lstm_forecast.csv",
    index=False
)

print("\nForecast saved successfully")
print("reports/lstm_forecast.csv")

# =====================================================
# SAVE FORECAST
# =====================================================

forecast_df = pd.DataFrame({
    "Forecast":
    future_predictions.flatten()
})

forecast_df.to_csv(
    "reports/lstm_forecast.csv",
    index=False
)

print(
    "\nForecast saved:"
)

print(
    "reports/lstm_forecast.csv"
)