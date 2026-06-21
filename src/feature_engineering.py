# =====================================================

# FEATURE ENGINEERING PIPELINE

# =====================================================

import pandas as pd
import numpy as np

# =====================================================

# LOAD DATA

# =====================================================

print("\nLoading dataset...")

df = pd.read_csv(
"data/processed/reliance_processed.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# =====================================================

# DAILY RETURNS

# =====================================================

df["Daily_Return"] = (
df["Close"]
.pct_change()
)

# =====================================================

# MOVING AVERAGES

# =====================================================

df["MA20"] = (
df["Close"]
.rolling(window=20)
.mean()
)

df["MA50"] = (
df["Close"]
.rolling(window=50)
.mean()
)

df["MA200"] = (
df["Close"]
.rolling(window=200)
.mean()
)

# =====================================================

# VOLATILITY

# =====================================================

df["Volatility_20"] = (
df["Daily_Return"]
.rolling(window=20)
.std()
)

# =====================================================

# RSI (14 DAY)

# =====================================================

delta = df["Close"].diff()

gain = delta.where(
delta > 0,
0
)

loss = -delta.where(
delta < 0,
0
)

avg_gain = gain.rolling(
window=14
).mean()

avg_loss = loss.rolling(
window=14
).mean()

rs = avg_gain / avg_loss

df["RSI"] = (
100 -
(
100 / (1 + rs)
)
)

# =====================================================

# MACD

# =====================================================

ema12 = df["Close"].ewm(
span=12,
adjust=False
).mean()

ema26 = df["Close"].ewm(
span=26,
adjust=False
).mean()

df["MACD"] = (
ema12 - ema26
)

df["Signal_Line"] = (
df["MACD"]
.ewm(
span=9,
adjust=False
)
.mean()
)

df["MACD_Histogram"] = (
df["MACD"]
- df["Signal_Line"]
)

# =====================================================

# BOLLINGER BANDS

# =====================================================

df["BB_Middle"] = (
df["Close"]
.rolling(window=20)
.mean()
)

std = (
df["Close"]
.rolling(window=20)
.std()
)

df["BB_Upper"] = (
df["BB_Middle"]
+ (2 * std)
)

df["BB_Lower"] = (
df["BB_Middle"]
- (2 * std)
)

# =====================================================
# TREND SCORE
# =====================================================

def calculate_trend_score(row):

    score = 0

    if (
        pd.notna(row["MA20"])
        and row["Close"] > row["MA20"]
    ):
        score += 25

    if (
        pd.notna(row["MA50"])
        and row["MA20"] > row["MA50"]
    ):
        score += 25

    if (
        pd.notna(row["MA200"])
        and row["MA50"] > row["MA200"]
    ):
        score += 25

    if (
        pd.notna(row["MACD"])
        and pd.notna(row["Signal_Line"])
        and row["MACD"] > row["Signal_Line"]
    ):
        score += 25

    return score


df["Trend_Score"] = df.apply(
    calculate_trend_score,
    axis=1
)

# =====================================================
# MARKET REGIME
# =====================================================

def market_regime(score):

    if score >= 75:
        return "Strong Bullish"

    elif score >= 50:
        return "Bullish"

    elif score >= 25:
        return "Neutral"

    else:
        return "Bearish"


df["Market_Regime"] = (
    df["Trend_Score"]
    .apply(market_regime)
)

# =====================================================
# AI RECOMMENDATION ENGINE
# =====================================================

def recommendation(row):

    if pd.isna(row["RSI"]):
        return "N/A"

    if (
        row["Trend_Score"] >= 75
        and row["RSI"] < 40
        and row["MACD"] > row["Signal_Line"]
    ):
        return "STRONG BUY"

    elif (
        row["RSI"] < 30
        and row["MACD"] > row["Signal_Line"]
    ):
        return "BUY"

    elif (
        row["Trend_Score"] <= 25
        and row["RSI"] > 70
        and row["MACD"] < row["Signal_Line"]
    ):
        return "STRONG SELL"

    elif (
        row["RSI"] > 70
        and row["MACD"] < row["Signal_Line"]
    ):
        return "SELL"

    elif row["Trend_Score"] >= 50:
        return "BULLISH HOLD"

    elif row["Trend_Score"] <= 25:
        return "BEARISH HOLD"

    else:
        return "HOLD"


df["Recommendation"] = df.apply(
    recommendation,
    axis=1
)

# =====================================================

# SAVE DATASET

# =====================================================

output_path = (
"data/processed/reliance_features.csv"
)

df.to_csv(
output_path,
index=False
)

# =====================================================

# SUMMARY

# =====================================================

latest = df.iloc[-1]

print("\nFEATURE ENGINEERING COMPLETE")
print("=" * 60)

print(
f"Rows                : {len(df)}"
)

print(
f"Columns             : {len(df.columns)}"
)

print(
f"Latest Close Price  : ₹{latest['Close']:.2f}"
)

print(
f"Latest RSI          : {latest['RSI']:.2f}"
)

print(
f"Trend Score         : {latest['Trend_Score']}/100"
)

print(
f"Market Regime       : {latest['Market_Regime']}"
)

print(
f"Recommendation      : {latest['Recommendation']}"
)

print(
f"\nSaved To: {output_path}"
)

print("\nFeature Columns:")
print(df.columns.tolist())
