import pandas as pd
import numpy as np

# =====================================================
# LOAD DATA
# =====================================================

print("\nLoading dataset...")

df = pd.read_csv(
    "data/processed/reliance_features.csv"
)

returns = (
    df["Daily_Return"]
    .dropna()
)

# =====================================================
# ANNUALIZED VOLATILITY
# =====================================================

volatility = (
    returns.std()
    * np.sqrt(252)
)

# =====================================================
# ANNUALIZED RETURN
# =====================================================

annual_return = (
    returns.mean()
    * 252
)

# =====================================================
# SHARPE RATIO
# =====================================================

risk_free_rate = 0.06

sharpe_ratio = (
    annual_return
    - risk_free_rate
) / volatility

# =====================================================
# MAXIMUM DRAWDOWN
# =====================================================

cumulative_returns = (
    1 + returns
).cumprod()

running_max = (
    cumulative_returns
    .cummax()
)

drawdown = (
    cumulative_returns
    - running_max
) / running_max

max_drawdown = (
    drawdown.min()
)

# =====================================================
# VALUE AT RISK (95%)
# =====================================================

var_95 = np.percentile(
    returns,
    5
)

# =====================================================
# RISK SCORE
# =====================================================

risk_score = 0

# Volatility Component
if volatility < 0.15:
    risk_score += 40

elif volatility < 0.30:
    risk_score += 25

else:
    risk_score += 10

# Sharpe Component
if sharpe_ratio > 2:
    risk_score += 30

elif sharpe_ratio > 1:
    risk_score += 20

else:
    risk_score += 10

# Drawdown Component
if abs(max_drawdown) < 0.20:
    risk_score += 30

elif abs(max_drawdown) < 0.40:
    risk_score += 20

else:
    risk_score += 10

# =====================================================
# RISK CATEGORY
# =====================================================

if risk_score >= 80:
    risk_category = "Low Risk"

elif risk_score >= 60:
    risk_category = "Moderate Risk"

elif risk_score >= 40:
    risk_category = "High Risk"

else:
    risk_category = "Very High Risk"

# =====================================================
# SAVE REPORT
# =====================================================

risk_report = pd.DataFrame({
    "Metric": [
        "Annualized Volatility",
        "Annualized Return",
        "Sharpe Ratio",
        "Maximum Drawdown",
        "Value at Risk (95%)",
        "Risk Score"
    ],
    "Value": [
        volatility,
        annual_return,
        sharpe_ratio,
        max_drawdown,
        var_95,
        risk_score
    ]
})

risk_report.to_csv(
    "reports/risk_report.csv",
    index=False
)

# =====================================================
# OUTPUT
# =====================================================

print("\nRISK ANALYSIS REPORT")
print("=" * 60)

print(
    f"Annualized Return      : {annual_return:.4f}"
)

print(
    f"Annualized Volatility  : {volatility:.4f}"
)

print(
    f"Sharpe Ratio           : {sharpe_ratio:.4f}"
)

print(
    f"Maximum Drawdown       : {max_drawdown:.4f}"
)

print(
    f"VaR (95%)              : {var_95:.4f}"
)

print(
    f"Risk Score             : {risk_score}/100"
)

print(
    f"Risk Category          : {risk_category}"
)

print(
    "\nReport Saved To: reports/risk_report.csv"
)