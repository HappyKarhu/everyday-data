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

# -----------------------------
# Load HSV-007
# -----------------------------

hsv007 = pd.read_csv(
    DATA_DIR / "HSV-007.csv"
)

print("\n--- HSV-007 ---")
print(hsv007.to_string(index=False))

# -----------------------------
# Load HSV-008
# -----------------------------

hsv008 = pd.read_csv(
    DATA_DIR / "HSV-008.csv"
)

print("\n--- HSV-008 ---")
print(hsv008.to_string(index=False))

# -----------------------------
# Load HSV-009
# -----------------------------

hsv009 = pd.read_csv(
    DATA_DIR / "HSV-009.csv"
)

print("\n--- HSV-009 ---")
print(hsv009.to_string(index=False))


# -----------------------------
# Load HSV-010
# -----------------------------

hsv010 = pd.read_csv(
    DATA_DIR / "HSV-010.csv"
)

print("\n--- HSV-010 ---")
print(hsv010.to_string(index=False))


# -----------------------------
# Load HSV-011
# -----------------------------

hsv011 = pd.read_csv(
    DATA_DIR / "HSV-011.csv"
)

print("\n--- HSV-011 ---")
print(hsv011.to_string(index=False))


# ============================================================
# Calculations
# ============================================================

# -----------------------------
# HSV-003
# Virus-positive lesions
# -----------------------------

virus_positive = float(
    hsv003.loc[
        hsv003["Variable"] == "Maximum virus-positive lesions",
        "Value"
    ].iloc[0]
)

print("\n--- HSV-003 values ---")
print("Maximum virus-positive lesions:", virus_positive, "%")


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
    "Prodrome/erythema:",
    "<",
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

# -----------------------------
# HSV-007
# Virus-positive lesions
# -----------------------------

hsv007_positive = float(
    hsv007.loc[
        hsv007["Variable"] == "HSV isolated",
        "Value"
    ].iloc[0]
)

print("\n--- HSV-007 values ---")
print("HSV isolated:", hsv007_positive, "%")


# -----------------------------
# HSV-008
# Mean vesicle healing time
# -----------------------------

hsv008_healing = float(
    hsv008.loc[
        hsv008["Variable"] == "Mean vesicle healing time",
        "Value"
    ].iloc[0]
)

print("\n--- HSV-008 values ---")
print("Mean vesicle healing time:", hsv008_healing, "days")


# -----------------------------
# HSV-009
# HSV-positive specimens
# -----------------------------

hsv009_positive = float(
    hsv009.loc[
        hsv009["Variable"] == "HSV-positive specimens",
        "Value"
    ].iloc[0]
)

hsv009_positive_percent = float(
    hsv009.loc[
        hsv009["Variable"] == "HSV-positive specimens",
        "Unit"
    ].iloc[0]
) if False else float(
    hsv009.loc[
        hsv009["Variable"] == "HSV-positive specimens",
        "Note"
    ].iloc[0]
) if False else float(
    hsv009.loc[
        hsv009["Variable"] == "HSV-positive specimens",
        "Value"
    ].iloc[0]
) / 637 * 100

print("\n--- HSV-009 values ---")
print("HSV-positive specimens:", hsv009_positive)
print(
    "HSV-positive specimens calculated:",
    round(hsv009_positive_percent, 2),
    "%"
)

# ============================================================
# HSV-003
# Lesion stage detection
# ============================================================

stage_data = pd.read_csv(
    DATA_DIR / "HSV-stage-detection.csv"
)

hsv003_stages = stage_data[
    stage_data["Study"] == "HSV-003"
].copy()

print("\n--- HSV-003 lesion stages ---")
print(
    hsv003_stages[
        ["Stage", "Detected_Percent", "Sample_Size", "Method"]
    ].to_string(index=False)
)

print("\n--- HSV-003 stage calculations ---")

for _, row in hsv003_stages.iterrows():
    detected = float(row["Detected_Percent"])
    not_detected = 100 - detected

    print(
        row["Stage"],
        ":",
        detected,
        "% detected |",
        not_detected,
        "% not detected"
    )


# ============================================================
# Fresh lesion vs crust
# ============================================================

fresh_detection = float(
    hsv003_stages.loc[
        hsv003_stages["Stage"] == "First 24 hours",
        "Detected_Percent"
    ].iloc[0]
)

vesicle_detection = float(
    hsv003_stages.loc[
        hsv003_stages["Stage"] == "Vesicle",
        "Detected_Percent"
    ].iloc[0]
)

crust_detection = float(
    hsv003_stages.loc[
        hsv003_stages["Stage"] == "Ulcer + soft crust",
        "Detected_Percent"
    ].iloc[0]
)

fresh_to_crust_drop = fresh_detection - crust_detection
fresh_to_crust_relative_drop = (
    fresh_to_crust_drop / fresh_detection
) * 100

vesicle_to_crust_drop = vesicle_detection - crust_detection
vesicle_to_crust_relative_drop = (
    vesicle_to_crust_drop / vesicle_detection
) * 100

print("\n--- Fresh lesion vs crust ---")
print("First 24 hours:", fresh_detection, "%")
print("Vesicle:", vesicle_detection, "%")
print("Ulcer + soft crust:", crust_detection, "%")

print(
    "Fresh lesion to crust decrease:",
    fresh_to_crust_drop,
    "percentage points"
)

print(
    "Fresh lesion to crust relative decrease:",
    round(fresh_to_crust_relative_drop, 2),
    "%"
)

print(
    "Vesicle to crust decrease:",
    vesicle_to_crust_drop,
    "percentage points"
)

print(
    "Vesicle to crust relative decrease:",
    round(vesicle_to_crust_relative_drop, 2),
    "%"
)


# ============================================================
# Final summary
# ============================================================

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
print("HSV-007 HSV isolated:", hsv007_positive, "%")
print("HSV-008 mean vesicle healing time:", hsv008_healing, "days")
print("HSV-009 HSV-positive specimens:", hsv009_positive)
print(
    "HSV-009 HSV-positive specimens calculated:",
    round(hsv009_positive_percent, 2),
    "%"
)
print(
    "HSV-003 prodrome/erythema relative titre: <",
    round(prodrome_relative, 4),
    "%"
)
print(
    "HSV-003 vesicle relative titre:",
    round(vesicle_relative, 2),
    "%"
)
print("HSV-003 maximum reported titre: 100.0 %")