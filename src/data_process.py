import pandas as pd

# =====================================================
# LOAD DATA
# =====================================================

print("\nLoading raw dataset...")

df = pd.read_csv(
    "data/raw/reliance_raw.csv"
)

# =====================================================
# DATE PROCESSING
# =====================================================

df["Date"] = pd.to_datetime(
    df["Date"]
)

# =====================================================
# SORT DATA
# =====================================================

df = df.sort_values(
    by="Date"
)

# =====================================================
# REMOVE DUPLICATES
# =====================================================

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

duplicates_removed = (
    before_duplicates
    - after_duplicates
)

# =====================================================
# HANDLE MISSING VALUES
# =====================================================

missing_before = (
    df.isnull()
    .sum()
    .sum()
)

df = df.ffill()

missing_after = (
    df.isnull()
    .sum()
    .sum()
)

# =====================================================
# RESET INDEX
# =====================================================

df = df.reset_index(
    drop=True
)

# =====================================================
# SAVE DATA
# =====================================================

output_path = (
    "data/processed/reliance_processed.csv"
)

df.to_csv(
    output_path,
    index=False
)

# =====================================================
# SUMMARY
# =====================================================

print("\nDATA PROCESSING COMPLETE")
print("=" * 60)

print(
    f"Rows               : {len(df)}"
)

print(
    f"Columns            : {len(df.columns)}"
)

print(
    f"Duplicates Removed : {duplicates_removed}"
)

print(
    f"Missing Before     : {missing_before}"
)

print(
    f"Missing After      : {missing_after}"
)

print(
    f"Date Range         : "
    f"{df['Date'].min()} "
    f"to "
    f"{df['Date'].max()}"
)

print(
    f"\nSaved To: {output_path}"
)

print("\nPreview:")
print(df.head())