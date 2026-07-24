from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True) #Samodejno ustvari mapo, če ne obstaja

dataset = pd.read_csv(DATA_DIR / "dataset.csv")

print(dataset)

# -----------------------------
# Chart: Water used per brushing
# -----------------------------

plt.figure(figsize=(6,4))

plt.bar(
    dataset["scenario"],
    dataset["water_per_brush_l"]
)

plt.title("Water used per brushing")

plt.xlabel("Scenario")

plt.ylabel("Liters")

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "water_per_brush.png",
    dpi=300
)

plt.show()