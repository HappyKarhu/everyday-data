import pandas as pd

# ==========================================================
# EN-003 – Laptop Electricity Consumption
# ==========================================================

# ----------------------------------------------------------
# 1. Load data
# ----------------------------------------------------------

df = pd.read_csv("data/EN-003-laptop-data.csv")
assumptions = pd.read_csv("data/assumptions.csv")


# ----------------------------------------------------------
# 2. Basic statistics
# ----------------------------------------------------------

stats = df[[
    "Off W",
    "Sleep W",
    "Long Idle W",
    "Short Idle W"
]].agg(["count", "mean", "median", "min", "max"])


# ----------------------------------------------------------
# 3. Difference between Sleep and Off
# ----------------------------------------------------------

df["Sleep minus Off W"] = df["Sleep W"] - df["Off W"]

sleep_off_difference = df["Sleep minus Off W"].agg(
    ["mean", "median", "min", "max"]
)


# ----------------------------------------------------------
# 4. Read assumptions
# ----------------------------------------------------------

sleep_hours = assumptions.loc[
    assumptions["assumption"] == "sleep_hours_per_day",
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


# ----------------------------------------------------------
# 5. Representative power values
# ----------------------------------------------------------

median_sleep_w = df["Sleep W"].median()
median_off_w = df["Off W"].median()


# ----------------------------------------------------------
# 6. Energy calculation – 8 hours Sleep
# ----------------------------------------------------------

sleep_8h_kwh_day = (
    median_sleep_w * sleep_hours / 1000
)

sleep_8h_kwh_year = (
    sleep_8h_kwh_day * days_per_year
)


# ----------------------------------------------------------
# 7. Energy calculation – 16 hours Sleep
# ----------------------------------------------------------

sleep_16h_kwh_day = (
    median_sleep_w * sleep_hours_extended / 1000
)

sleep_16h_kwh_year = (
    sleep_16h_kwh_day * days_per_year
)


# ----------------------------------------------------------
# 8. Energy calculation – Off
# ----------------------------------------------------------

off_8h_kwh_day = (
    median_off_w * sleep_hours / 1000
)

off_8h_kwh_year = (
    off_8h_kwh_day * days_per_year
)


off_16h_kwh_day = (
    median_off_w * sleep_hours_extended / 1000
)

off_16h_kwh_year = (
    off_16h_kwh_day * days_per_year
)


# ----------------------------------------------------------
# 9. Additional energy from Sleep instead of Off
# ----------------------------------------------------------

additional_8h_kwh_year = (
    sleep_8h_kwh_year - off_8h_kwh_year
)

additional_16h_kwh_year = (
    sleep_16h_kwh_year - off_16h_kwh_year
)


# ----------------------------------------------------------
# 10. Print results
# ----------------------------------------------------------

print("=== EN-003 Laptop Electricity Consumption ===")

print("\nBasic statistics:")
print(stats)

print("\nSleep minus Off:")
print(sleep_off_difference)

print("\nRepresentative values:")
print(f"Median Sleep: {median_sleep_w:.2f} W")
print(f"Median Off:   {median_off_w:.2f} W")

print("\n8-hour scenario:")
print(f"Sleep: {sleep_8h_kwh_year:.3f} kWh/year")
print(f"Off:   {off_8h_kwh_year:.3f} kWh/year")
print(f"Extra Sleep energy: {additional_8h_kwh_year:.3f} kWh/year")

print("\n16-hour scenario:")
print(f"Sleep: {sleep_16h_kwh_year:.3f} kWh/year")
print(f"Off:   {off_16h_kwh_year:.3f} kWh/year")
print(f"Extra Sleep energy: {additional_16h_kwh_year:.3f} kWh/year")