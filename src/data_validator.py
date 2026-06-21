import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================

print("\nLoading dataset...")

df = pd.read_csv(
    "data/raw/reliance_raw.csv"
)

# =====================================================
# BASIC INFORMATION
# =====================================================

print("\nDATA VALIDATION REPORT")
print("=" * 60)

print(f"Rows                : {len(df)}")
print(f"Columns             : {len(df.columns)}")

print("\nColumn Names")
print("-" * 60)

for col in df.columns:
    print(col)

# =====================================================
# DATA TYPES
# =====================================================

print("\nDATA TYPES")
print("-" * 60)

print(df.dtypes)

# =====================================================
# DATE VALIDATION
# =====================================================

if "Date" in df.columns:

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    print("\nDATE RANGE")
    print("-" * 60)

    print(
        f"Earliest Date       : {df['Date'].min()}"
    )

    print(
        f"Latest Date         : {df['Date'].max()}"
    )

# =====================================================
# MISSING VALUES
# =====================================================

print("\nMISSING VALUES")
print("-" * 60)

missing_values = df.isnull().sum()

print(missing_values)

print(
    f"\nTotal Missing Values : {missing_values.sum()}"
)

# =====================================================
# DUPLICATES
# =====================================================

duplicates = df.duplicated().sum()

print("\nDUPLICATE RECORDS")
print("-" * 60)

print(
    f"Duplicate Rows      : {duplicates}"
)

# =====================================================
# NEGATIVE VALUE CHECKS
# =====================================================

print("\nVALUE VALIDATION")
print("-" * 60)

price_columns = [
    "Open",
    "High",
    "Low",
    "Close"
]

for col in price_columns:

    if col in df.columns:

        negative_count = (
            df[col] < 0
        ).sum()

        print(
            f"Negative {col:<10}: {negative_count}"
        )

if "Volume" in df.columns:

    negative_volume = (
        df["Volume"] < 0
    ).sum()

    print(
        f"Negative Volume    : {negative_volume}"
    )

# =====================================================
# OUTLIER SUMMARY
# =====================================================

print("\nNUMERICAL SUMMARY")
print("-" * 60)

print(
    df.describe()
)

# =====================================================
# FINAL STATUS
# =====================================================

print("\nVALIDATION STATUS")
print("=" * 60)

if (
    missing_values.sum() == 0
    and duplicates == 0
):
    print(
        "Dataset validation completed successfully."
    )

else:
    print(
        "Dataset contains issues that should be reviewed."
    )