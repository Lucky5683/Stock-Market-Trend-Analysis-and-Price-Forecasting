import yfinance as yf
import pandas as pd

# =====================================================
# CONFIGURATION
# =====================================================

TICKER = "RELIANCE.NS"
START_DATE = "2020-01-01"
END_DATE = "2024-12-31"

# =====================================================
# DOWNLOAD DATA
# =====================================================

print("\nDownloading stock data...")

df = yf.download(
    TICKER,
    start=START_DATE,
    end=END_DATE,
    auto_adjust=True
)

# =====================================================
# CLEAN DATA
# =====================================================

df = df.reset_index()

# Remove multi-index if present
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

required_columns = [
    "Date",
    "Close",
    "High",
    "Low",
    "Open",
    "Volume"
]

df = df[required_columns]

# =====================================================
# SAVE DATA
# =====================================================

output_path = "data/raw/reliance_raw.csv"

df.to_csv(
    output_path,
    index=False
)

# =====================================================
# SUMMARY
# =====================================================

print("\nDATA DOWNLOAD COMPLETE")
print("=" * 60)

print(f"Ticker             : {TICKER}")
print(f"Rows               : {len(df)}")
print(f"Columns            : {len(df.columns)}")

print(
    f"Start Date         : {df['Date'].min()}"
)

print(
    f"End Date           : {df['Date'].max()}"
)

print(
    f"\nSaved To: {output_path}"
)

print("\nPreview:")
print(df.head())