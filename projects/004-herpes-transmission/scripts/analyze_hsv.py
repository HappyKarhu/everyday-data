from pathlib import Path
import pandas as pd

# -----------------------------
# Project paths
# -----------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"


# -----------------------------
# Load HSV-001
# -----------------------------

hsv001 = pd.read_csv(
    DATA_DIR / "HSV-001.csv"
)

print("\n--- HSV-001 ---")
print(hsv001.to_string(index=False))


# -----------------------------
# Load HSV-002
# -----------------------------

hsv002 = pd.read_csv(
    DATA_DIR / "HSV-002.csv"
)

print("\n--- HSV-002 ---")
print(hsv002.to_string(index=False))


# -----------------------------
# Load HSV-003
# -----------------------------

hsv003 = pd.read_csv(
    DATA_DIR / "HSV-003.csv"
)

print("\n--- HSV-003 ---")
print(hsv003.to_string(index=False))


# -----------------------------
# Load HSV-004
# -----------------------------

hsv004 = pd.read_csv(
    DATA_DIR / "HSV-004.csv"
)

print("\n--- HSV-004 ---")
print(hsv004.to_string(index=False))


# -----------------------------
# Load HSV-005
# -----------------------------

hsv005 = pd.read_csv(
    DATA_DIR / "HSV-005.csv"
)

print("\n--- HSV-005 ---")
print(hsv005.to_string(index=False))


# ============================================================
# Simple calculations
# ============================================================

# -----------------------------
# HSV-003
# Virus-positive lesions
# -----------------------------

virus_positive = float(
    hsv003.loc[
        hsv003["Measurement"] == "Virus-positive lesions",
        "Value"
    ].iloc[0]
)

print("\n--- HSV-003 values ---")
print("Virus-positive lesions:", virus_positive, "%")


# -----------------------------
# HSV-004
# Shedding duration
# -----------------------------

subjects = int(
    hsv004.loc[
        hsv004["Variable"] == "Subjects",
        "Value"
    ].iloc[0]
)

pcr_shedding = float(
    hsv004.loc[
        hsv004["Variable"] == "HSV-1 shedding duration by PCR",
        "Value"
    ].iloc[0]
)

culture_shedding = float(
    hsv004.loc[
        hsv004["Variable"] == "HSV-1 shedding duration by culture",
        "Value"
    ].iloc[0]
)

difference = pcr_shedding - culture_shedding


print("\n--- HSV-004 values ---")
print("Subjects:", subjects)
print("PCR shedding duration:", pcr_shedding, "hours")
print("Culture shedding duration:", culture_shedding, "hours")
print("Difference:", difference, "hours")


# -----------------------------
# HSV-005
# Asymptomatic shedding
# -----------------------------

asymptomatic = hsv005.loc[
    hsv005["Variable"] == "Asymptomatic shedding",
    "Value"
].iloc[0]

print("\n--- HSV-005 values ---")
print("Asymptomatic shedding:", asymptomatic)


# -----------------------------
# Final summary
# -----------------------------

print("\n==============================")
print("HSV RESEARCH SUMMARY")
print("==============================")

print("HSV-003 virus-positive lesions:", virus_positive, "%")
print("HSV-004 PCR shedding:", pcr_shedding, "hours")
print("HSV-004 culture shedding:", culture_shedding, "hours")
print("HSV-004 difference:", difference, "hours")
print("HSV-005 asymptomatic shedding:", asymptomatic)