import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(
    "data/processed/reliance_features.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

print("\nEXPLORATORY DATA ANALYSIS REPORT")
print("=" * 60)

# =====================================================
# BASIC STATISTICS
# =====================================================

print("\nDATASET INFO")
print("-" * 40)

print(f"Rows      : {len(df)}")
print(f"Columns   : {len(df.columns)}")

print("\nDate Range")
print(f"Start Date : {df['Date'].min()}")
print(f"End Date   : {df['Date'].max()}")

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistical Summary")
print(
    df[
        [
            "Close",
            "Volume"
        ]
    ].describe()
)

# =====================================================
# PRICE + MOVING AVERAGES
# =====================================================

plt.figure(figsize=(14,7))

plt.plot(
    df["Date"],
    df["Close"],
    label="Close Price"
)

plt.plot(
    df["Date"],
    df["MA20"],
    label="MA20"
)

plt.plot(
    df["Date"],
    df["MA50"],
    label="MA50"
)

plt.plot(
    df["Date"],
    df["MA200"],
    label="MA200"
)

plt.title(
    "Price Trend with Moving Averages"
)

plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.show()

# =====================================================
# RSI
# =====================================================

plt.figure(figsize=(14,5))

plt.plot(
    df["Date"],
    df["RSI"],
    label="RSI"
)

plt.axhline(
    y=70,
    linestyle="--"
)

plt.axhline(
    y=30,
    linestyle="--"
)

plt.title("RSI Indicator")

plt.xlabel("Date")
plt.ylabel("RSI")

plt.grid(True)

plt.show()

# =====================================================
# MACD
# =====================================================

plt.figure(figsize=(14,5))

plt.plot(
    df["Date"],
    df["MACD"],
    label="MACD"
)

plt.plot(
    df["Date"],
    df["Signal_Line"],
    label="Signal Line"
)

plt.title("MACD")

plt.xlabel("Date")
plt.ylabel("Value")

plt.legend()
plt.grid(True)

plt.show()

# =====================================================
# VOLATILITY
# =====================================================

plt.figure(figsize=(14,5))

plt.plot(
    df["Date"],
    df["Volatility_20"]
)

plt.title(
    "20-Day Rolling Volatility"
)

plt.xlabel("Date")
plt.ylabel("Volatility")

plt.grid(True)

plt.show()

# =====================================================
# BOLLINGER BANDS
# =====================================================

plt.figure(figsize=(14,7))

plt.plot(
    df["Date"],
    df["Close"],
    label="Close"
)

plt.plot(
    df["Date"],
    df["BB_Upper"],
    label="Upper Band"
)

plt.plot(
    df["Date"],
    df["BB_Middle"],
    label="Middle Band"
)

plt.plot(
    df["Date"],
    df["BB_Lower"],
    label="Lower Band"
)

plt.title(
    "Bollinger Bands"
)

plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()
plt.grid(True)

plt.show()

# =====================================================
# FINAL INSIGHTS
# =====================================================

latest = df.iloc[-1]

print("\nLATEST MARKET INSIGHTS")
print("=" * 60)

print(
    f"Close Price    : ₹{latest['Close']:.2f}"
)

print(
    f"RSI            : {latest['RSI']:.2f}"
)

print(
    f"Trend Score    : {latest['Trend_Score']}/100"
)

print(
    f"Recommendation : {latest['Recommendation']}"
)