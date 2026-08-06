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
recommended_time = get_value("recommended_brushing_time")
average_time = get_value("average_brushing_time")
flow_rate = get_value("faucet_flow_rate")
frequency = get_value("brushing_frequency")

print()
print("Recommended brushing time:", recommended_time)
print("Average brushing time:", average_time)
print("Flow rate:", flow_rate)
print("Frequency:", frequency)

# -----------------------------
# Unit conversions
# -----------------------------

recommended_time_min = recommended_time / 60
average_time_min = average_time / 60

print()
print("Recommended brushing time (min):", recommended_time_min)
print("Average brushing time (min):", round(average_time_min, 2))

# -----------------------------
# Water used per brushing
# -----------------------------

recommended_water = flow_rate * recommended_time_min
average_water = flow_rate * average_time_min

print()
print("Water per recommended brushing:", recommended_water, "L")
print("Water per average brushing:", round(average_water, 2), "L")

# -----------------------------
# Validation
# -----------------------------
print("\n--- Validation ---")

if flow_rate <= 0:
    raise ValueError("Flow rate must be greater than zero.")

if recommended_time <= 0:
    raise ValueError("Brushing time must be greater than zero.")

if frequency <= 0:
    raise ValueError("Frequency must be greater than zero.")

print("All assumptions are valid.")

# -----------------------------
# Build dataset
# -----------------------------

dataset = pd.DataFrame({
    "scenario": [
        "Recommended brushing",
        "Average brushing"
    ],
    "brushing_time_sec": [
        recommended_time,
        average_time
    ],
    "flow_rate_lpm": [
        flow_rate,
        flow_rate
    ],
    "frequency_per_day": [
        frequency,
        frequency
    ]
})

print()
print(dataset)

dataset["brushing_time_min"] = dataset["brushing_time_sec"] / 60

dataset["water_per_brush_l"] = (
    dataset["flow_rate_lpm"]
    * dataset["brushing_time_min"]
)

dataset["water_per_day_l"] = (
    dataset["water_per_brush_l"]
    * dataset["frequency_per_day"]
)

dataset["water_per_year_l"] = (
    dataset["water_per_day_l"]
    * 365
)

print()
print(dataset)

dataset.to_csv(
    DATA_DIR / "dataset.csv",
    index=False
)

print("\nDataset saved.")