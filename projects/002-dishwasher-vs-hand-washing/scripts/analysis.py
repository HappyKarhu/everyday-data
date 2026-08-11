from pathlib import Path
import pandas as pd

# -----------------------------
# Project paths
# -----------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# -----------------------------
# Load assumptions
# -----------------------------

assumptions = pd.read_csv(DATA_DIR / "assumptions.csv")

print(assumptions)

# -----------------------------
# Helper function
# -----------------------------

def get_value(variable):
    return assumptions.loc[
        assumptions["variable"] == variable,
        "value"
    ].iloc[0]

# -----------------------------
# Read values
# -----------------------------

place_settings = get_value("comparison_place_settings")

dishwasher_eu = get_value("dishwasher_eu_average_2020")
dishwasher_efficient = get_value("dishwasher_efficient")
dishwasher_consumer = get_value("dishwasher_consumer_test")

handwashing_consumer = get_value("handwashing_consumer_test")

manual_min = get_value("manual_water_min")
manual_max = get_value("manual_water_max")

dishwasher_min = get_value("dishwasher_water_min_review")
dishwasher_max = get_value("dishwasher_water_max_review")

manual_example = get_value("manual_comparison_example")
dishwasher_example = get_value("dishwasher_comparison_example")

uk_pre_rinse = get_value("uk_pre_rinsing_water")
italy_pre_rinse = get_value("italy_pre_rinsing_water")

handwashing_which = get_value("handwashing_which_2026")
dishwasher_which_main = get_value("dishwasher_which_main_2026")
dishwasher_which_eco = get_value("dishwasher_which_eco_2026")

print()
print("WA-008 values:")
print("Handwashing estimate:", handwashing_which, "L/place setting")
print("Dishwasher main:", dishwasher_which_main, "L/place setting")
print("Dishwasher eco:", dishwasher_which_eco, "L/place setting")

# -----------------------------
# Validation
# -----------------------------

print("\n--- Validation ---")

values_to_check = {
    "place_settings": place_settings,
    "dishwasher_eu": dishwasher_eu,
    "dishwasher_efficient": dishwasher_efficient,
    "dishwasher_consumer": dishwasher_consumer,
    "handwashing_consumer": handwashing_consumer,
    "manual_min": manual_min,
    "manual_max": manual_max,
    "dishwasher_min": dishwasher_min,
    "dishwasher_max": dishwasher_max,
    "manual_example": manual_example,
    "dishwasher_example": dishwasher_example,
    "uk_pre_rinse": uk_pre_rinse,
    "italy_pre_rinse": italy_pre_rinse,
    "handwashing_which": handwashing_which,
    "dishwasher_which_main": dishwasher_which_main,
    "dishwasher_which_eco": dishwasher_which_eco,
}

for name, value in values_to_check.items():
    if value <= 0:
        raise ValueError(f"{name} must be greater than zero.")

print("All assumptions are valid.")

# -----------------------------
# Build dataset
# -----------------------------

dataset = pd.DataFrame({
    "scenario": [
        "Dishwasher - EU average",
        "Dishwasher - efficient",
        "Dishwasher - Consumer NZ",
        "Dishwasher - review minimum",
        "Dishwasher - review maximum",
        "Dishwasher + UK pre-rinsing",
        "Dishwasher + Italy pre-rinsing",
        "Hand washing - Consumer NZ",
        "Hand washing - observed minimum",
        "Hand washing - observed maximum",
        "Hand washing - direct comparison",
        "Dishwasher - Which? main programme",
        "Dishwasher - Which? eco programme",
        "Hand washing - Which? estimate",
    ],
    "method": [
        "Dishwasher",
        "Dishwasher",
        "Dishwasher",
        "Dishwasher",
        "Dishwasher",
        "Dishwasher + pre-rinsing",
        "Dishwasher + pre-rinsing",
        "Hand washing",
        "Hand washing",
        "Hand washing",
        "Hand washing",
        "Dishwasher",
        "Dishwasher",
        "Hand washing",
    ],
    "water_l": [
        dishwasher_eu,
        dishwasher_efficient,
        dishwasher_consumer,
        dishwasher_min,
        dishwasher_max,
        dishwasher_consumer + uk_pre_rinse,
        dishwasher_consumer + italy_pre_rinse,
        handwashing_consumer,
        manual_min,
        manual_max,
        manual_example,
        dishwasher_which_main,
        dishwasher_which_eco,
        handwashing_which,
    ],
    "place_settings": [
        place_settings,
        15,
        place_settings,
        place_settings,
        place_settings,
        place_settings,
        place_settings,
        place_settings,
        place_settings,
        place_settings,
        place_settings,
        1,
        1,
        1,
    ],
})

# -----------------------------
# Add source type
# -----------------------------

dataset["source_type"] = [
    "EU average",
    "EU efficient technology",
    "Consumer test",
    "Scientific review",
    "Scientific review",
    "Scenario calculation",
    "Scenario calculation",
    "Consumer test",
    "Scientific review",
    "Scientific review",
    "Scientific review",
    "Which? practical testing",
    "Which? practical testing",
    "Which? estimated scenario",
]

# -----------------------------
# Add notes
# -----------------------------

dataset["note"] = [
    "EU average in 2020",
    "Efficient dishwasher, up to 15 place settings",
    "Full load",
    "Lowest reported country-level average",
    "Highest reported country-level average",
    "13 L dishwasher + 4.4 L UK pre-rinsing",
    "13 L dishwasher + 19.7 L Italy pre-rinsing",
    "Includes pre-rinsing",
    "Lowest country-level average reported",
    "Highest country-level average reported",
    "Direct comparison reported in review",
    "Average water use of 33 recently tested dishwashers",
    "Average water use of 33 recently tested dishwashers",
    "Estimated from a 9-L washing-up bowl for approximately two place settings",
]

# -----------------------------
# Display dataset
# -----------------------------

print("\n--- Dataset ---")
print(dataset.to_string(index=False))

# -----------------------------
# Water use per place setting
# -----------------------------

dataset["water_per_place_setting_l"] = (
    dataset["water_l"] / dataset["place_settings"]
)

print()
print(dataset[
    [
        "scenario",
        "water_l",
        "place_settings",
        "water_per_place_setting_l"
    ]
])

# -----------------------------
# Water use for 12 place settings
# -----------------------------

dataset["water_for_12_place_settings_l"] = (
    dataset["water_per_place_setting_l"] * place_settings
)

print()
print(dataset[
    [
        "scenario",
        "water_per_place_setting_l",
        "water_for_12_place_settings_l"
    ]
])

# -----------------------------
# Water savings compared with hand washing
# -----------------------------

hand_washing_12 = handwashing_which * place_settings

dataset["water_saved_vs_hand_washing_l"] = (
    hand_washing_12 - dataset["water_for_12_place_settings_l"]
)

dataset["water_saved_percent"] = (
    dataset["water_saved_vs_hand_washing_l"]
    / hand_washing_12
    * 100
)

# -----------------------------
# Annual water use
# -----------------------------

dataset["water_for_12_place_settings_per_year_l"] = (
    dataset["water_for_12_place_settings_l"] * 365
)

print()
print(dataset[
    [
        "scenario",
        "water_for_12_place_settings_l",
        "water_for_12_place_settings_per_year_l"
    ]
])

# -----------------------------
# Annual water use and savings
# -----------------------------

washes_per_year = 365

dataset["water_for_12_place_settings_per_year_l"] = (
    dataset["water_for_12_place_settings_l"]
    * washes_per_year
)

dataset["water_saved_per_year_l"] = (
    dataset["water_saved_vs_hand_washing_l"]
    * washes_per_year
)

print()
print(dataset[
    [
        "scenario",
        "water_for_12_place_settings_per_year_l",
        "water_saved_per_year_l"
    ]
])

print()
print(dataset[
    [
        "scenario",
        "water_for_12_place_settings_l",
        "water_saved_vs_hand_washing_l",
        "water_saved_percent"
    ]
])

# -----------------------------
# Convert annual water use to cubic metres
# -----------------------------

dataset["water_for_12_place_settings_per_year_m3"] = (
    dataset["water_for_12_place_settings_per_year_l"] / 1000
)

dataset["water_saved_per_year_m3"] = (
    dataset["water_saved_per_year_l"] / 1000
)

print()
print(dataset[
    [
        "scenario",
        "water_for_12_place_settings_per_year_m3",
        "water_saved_per_year_m3"
    ]
])

# -----------------------------
# Save dataset
# -----------------------------

dataset.to_csv(
    DATA_DIR / "dataset.csv",
    index=False
)

print("\nDataset saved.")