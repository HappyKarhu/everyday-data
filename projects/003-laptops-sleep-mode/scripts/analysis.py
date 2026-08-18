from pathlib import Path
import pandas as pd

# ==========================================================
# EN-003 – Laptop Electricity Consumption
# ==========================================================

# ----------------------------------------------------------
# 1. Project paths
# ----------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)


# ----------------------------------------------------------
# 2. Load data
# ----------------------------------------------------------

df = pd.read_csv(DATA_DIR / "EN-003-laptop-data.csv")
assumptions = pd.read_csv(DATA_DIR / "assumptions.csv")

print("\n--- CSV columns ---")
print(df.columns.tolist())


# ----------------------------------------------------------
# 3. Basic statistics
# ----------------------------------------------------------

power_columns = [
    "Off W",
    "Sleep W",
    "Long Idle W",
    "Short Idle W"
]

stats = df[power_columns].agg(
    ["count", "mean", "median", "min", "max"]
)

print("\n=== Basic statistics ===")
print(stats)


# ----------------------------------------------------------
# 4. Sleep minus Off
# ----------------------------------------------------------

df["Sleep minus Off W"] = (
    df["Sleep W"] - df["Off W"]
)

sleep_off_difference = df["Sleep minus Off W"].agg(
    ["mean", "median", "min", "max"]
)

print("\n=== Sleep minus Off ===")
print(sleep_off_difference)


# ----------------------------------------------------------
# 5. Read assumptions
# ----------------------------------------------------------

sleep_hours = assumptions.loc[
    assumptions["assumption"] == "sleep_hours_per_night",
    "value"
].iloc[0]

sleep_hours_extended = assumptions.loc[
    assumptions["assumption"] == "sleep_hours_extended_per_day",
    "value"
].iloc[0]

days_per_year = assumptions.loc[
    assumptions["assumption"] == "days_per_year",
    "value"
].iloc[0]

led_bulb_power = assumptions.loc[
    assumptions["assumption"] == "led_bulb_power",
    "value"
].iloc[0]


# ----------------------------------------------------------
# 6. Representative values
# ----------------------------------------------------------

median_sleep_w = df["Sleep W"].median()
median_off_w = df["Off W"].median()

mean_sleep_w = df["Sleep W"].mean()
mean_off_w = df["Off W"].mean()

min_sleep_w = df["Sleep W"].min()
max_sleep_w = df["Sleep W"].max()

min_off_w = df["Off W"].min()
max_off_w = df["Off W"].max()


print("\n=== Representative values ===")
print(f"Median Sleep: {median_sleep_w:.2f} W")
print(f"Median Off:   {median_off_w:.2f} W")
print(f"Mean Sleep:   {mean_sleep_w:.3f} W")
print(f"Mean Off:     {mean_off_w:.3f} W")


# ----------------------------------------------------------
# 7. Function for annual energy
# ----------------------------------------------------------

def annual_energy_kwh(power_w, hours_per_day):
    return (
        power_w
        * hours_per_day
        * days_per_year
        / 1000
    )


# ----------------------------------------------------------
# 8. Calculate scenarios
# ----------------------------------------------------------

scenarios = []

for hours in [sleep_hours, sleep_hours_extended]:

    sleep_kwh = annual_energy_kwh(
        median_sleep_w,
        hours
    )

    off_kwh = annual_energy_kwh(
        median_off_w,
        hours
    )

    additional_kwh = sleep_kwh - off_kwh

    led_hours = (
        additional_kwh * 1000
        / led_bulb_power
    )

    scenarios.append({
        "scenario": f"{int(hours)} hours Sleep per day",
        "sleep_hours_per_day": hours,
        "median_sleep_w": median_sleep_w,
        "median_off_w": median_off_w,
        "sleep_kwh_per_year": sleep_kwh,
        "off_kwh_per_year": off_kwh,
        "additional_sleep_kwh_per_year": additional_kwh,
        "led_bulb_power_w": led_bulb_power,
        "led_equivalent_hours_per_year": led_hours
    })


results = pd.DataFrame(scenarios)


# ----------------------------------------------------------
# 9. Print results
# ----------------------------------------------------------

print("\n=== Annual scenarios ===")

print(
    results[
        [
            "scenario",
            "sleep_kwh_per_year",
            "off_kwh_per_year",
            "additional_sleep_kwh_per_year",
            "led_equivalent_hours_per_year"
        ]
    ].to_string(index=False)
)


# ----------------------------------------------------------
# 10. Statistics output
# ----------------------------------------------------------

statistics_output = stats.reset_index()

statistics_output = statistics_output.rename(
    columns={"index": "statistic"}
)

statistics_output.to_csv(
    OUTPUT_DIR / "EN-003-statistics.csv",
    index=False
)


# ----------------------------------------------------------
# 11. Sleep vs Off output
# ----------------------------------------------------------

sleep_off_output = pd.DataFrame({
    "statistic": sleep_off_difference.index,
    "sleep_minus_off_w": sleep_off_difference.values
})

sleep_off_output.to_csv(
    OUTPUT_DIR / "EN-003-sleep-vs-off.csv",
    index=False
)


# ----------------------------------------------------------
# 12. Main results
# ----------------------------------------------------------

results.to_csv(
    OUTPUT_DIR / "EN-003-results.csv",
    index=False
)


# ----------------------------------------------------------
# 13. Comparison output for article / Power BI
# ----------------------------------------------------------

comparison = results[
    [
        "scenario",
        "sleep_hours_per_day",
        "sleep_kwh_per_year",
        "off_kwh_per_year",
        "additional_sleep_kwh_per_year",
        "led_bulb_power_w",
        "led_equivalent_hours_per_year"
    ]
].copy()

comparison.to_csv(
    OUTPUT_DIR / "EN-003-comparison.csv",
    index=False
)


# ----------------------------------------------------------
# 14. Dataset summary
# ----------------------------------------------------------

dataset_summary = pd.DataFrame({
    "metric": [
        "Number of laptops",
        "Median Sleep power",
        "Mean Sleep power",
        "Minimum Sleep power",
        "Maximum Sleep power",
        "Median Off power",
        "Mean Off power",
        "Minimum Off power",
        "Maximum Off power",
        "Median Sleep minus Off",
        "Mean Sleep minus Off",
        "Minimum Sleep minus Off",
        "Maximum Sleep minus Off"
    ],
    "value": [
        len(df),
        median_sleep_w,
        mean_sleep_w,
        min_sleep_w,
        max_sleep_w,
        median_off_w,
        mean_off_w,
        min_off_w,
        max_off_w,
        sleep_off_difference["median"],
        sleep_off_difference["mean"],
        sleep_off_difference["min"],
        sleep_off_difference["max"]
    ],
    "unit": [
        "laptops",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W",
        "W"
    ]
})

dataset_summary.to_csv(
    OUTPUT_DIR / "EN-003-summary.csv",
    index=False
)


# ----------------------------------------------------------
# 15. Final message
# ----------------------------------------------------------

print("\n=== Files saved ===")

print(OUTPUT_DIR / "EN-003-results.csv")
print(OUTPUT_DIR / "EN-003-comparison.csv")
print(OUTPUT_DIR / "EN-003-statistics.csv")
print(OUTPUT_DIR / "EN-003-sleep-vs-off.csv")
print(OUTPUT_DIR / "EN-003-summary.csv")

print("\nAnalysis complete.")