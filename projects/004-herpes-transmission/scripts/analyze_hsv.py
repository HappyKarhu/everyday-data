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

# -----------------------------
# Load HSV-006
# -----------------------------

hsv006 = pd.read_csv(
    DATA_DIR / "HSV-006.csv"
)

print("\n--- HSV-006 ---")
print(hsv006.to_string(index=False))

# ============================================================
# Calculations
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
# HSV-003
# Relative viral titre
# -----------------------------

# Reported mean titres from HSV-003
# Maximum reported lesion-swab titre = 10^5 PFU
# Prodromal/erythema titre = <10^1 PFU
# Vesicle titre = 10^4.7 PFU

max_titre = 10**5
prodrome_titre_upper = 10**1
vesicle_titre = 10**4.7

# Calculate relative titre compared with the maximum reported titre
prodrome_relative = (prodrome_titre_upper / max_titre) * 100
vesicle_relative = (vesicle_titre / max_titre) * 100

print("\n--- HSV-003 relative viral titre ---")
print(
    "Prodrome/erythema: <",
    round(prodrome_relative, 4),
    "% of maximum reported titre"
)
print(
    "Vesicle:",
    round(vesicle_relative, 2),
    "% of maximum reported titre"
)
print(
    "Maximum reported titre:",
    100,
    "% of maximum reported titre"
)


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
# HSV-006
# Detectable HSV-1
# -----------------------------

detectable_episode = float(
    hsv006.loc[
        hsv006["Variable"] == "HSV-1 detectable during episode",
        "Value"
    ].iloc[0]
)

vesicle_ulcer_shedding = float(
    hsv006.loc[
        hsv006["Variable"] == "Shedding during vesicle/ulcer stage",
        "Value"
    ].iloc[0]
)

print("\n--- HSV-006 values ---")
print("HSV-1 detectable during episode:", detectable_episode, "%")
print("Vesicle/ulcer shedding:", vesicle_ulcer_shedding, "%")

# ============================================================
# Stage Detection Calculations
# ============================================================

stage_data = pd.read_csv(
    DATA_DIR / "HSV-stage-detection.csv"
)

print("\n--- HSV stage detection ---")
print(stage_data.to_string(index=False))


# -----------------------------
# Calculate not-detected %
# -----------------------------

stage_data["Not_Detected_Percent"] = (
    100 - stage_data["Detected_Percent"]
)

print("\n--- Detection vs non-detection ---")
print(
    stage_data[
        [
            "Stage",
            "Detected_Percent",
            "Not_Detected_Percent",
            "Study",
            "Method"
        ]
    ].to_string(index=False)
)


# -----------------------------
# HSV-003: drop from vesicle
# to ulcer + soft crust
# -----------------------------

vesicle_detection = float(
    stage_data.loc[
        stage_data["Stage"] == "Vesicle",
        "Detected_Percent"
    ].iloc[0]
)

ulcer_crust_detection = float(
    stage_data.loc[
        stage_data["Stage"] == "Ulcer + soft crust",
        "Detected_Percent"
    ].iloc[0]
)

absolute_drop = (
    vesicle_detection - ulcer_crust_detection
)

relative_drop = (
    absolute_drop / vesicle_detection
) * 100

print("\n--- HSV-003 stage comparison ---")
print(
    "Vesicle detection:",
    vesicle_detection,
    "%"
)

print(
    "Ulcer + soft crust detection:",
    ulcer_crust_detection,
    "%"
)

print(
    "Absolute decrease:",
    absolute_drop,
    "percentage points"
)

print(
    "Relative decrease:",
    round(relative_drop, 2),
    "%"
)
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
print("HSV-006 detectable during episode:", detectable_episode, "%")
print("HSV-006 vesicle/ulcer shedding:", vesicle_ulcer_shedding, "%")
print("HSV-003 prodrome/erythema relative titre: <", round(prodrome_relative, 4), "%")
print("HSV-003 vesicle relative titre:", round(vesicle_relative, 2), "%")
print("HSV-003 maximum reported titre: 100.0 %")
