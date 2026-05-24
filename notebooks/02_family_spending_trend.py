import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# Create visuals directory
# -----------------------------

visuals_dir = Path("visuals")
visuals_dir.mkdir(exist_ok=True)

# -----------------------------
# Data
# -----------------------------

# Aspen Institute / Project Play reported:
# 2024 average spending = $1,016
# 46% increase since 2019

data = pd.DataFrame({
    "year": [2019, 2024],
    "avg_spending": [696, 1016]
})

# -----------------------------
# Style
# -----------------------------

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 18,
    "axes.labelsize": 12
})

fig, ax = plt.subplots(figsize=(11, 6))

# -----------------------------
# Line chart
# -----------------------------

ax.plot(
    data["year"],
    data["avg_spending"],
    marker="o",
    linewidth=3
)

# -----------------------------
# Titles
# -----------------------------

ax.set_title(
    "Average Family Spending on Youth Sports Rose 46%",
    loc="left",
    pad=35,
    weight="bold"
)

fig.text(
    0.125,
    0.89,
    "Average annual spending on a child’s primary sport, 2019–2024",
    fontsize=11
)

# -----------------------------
# Axis formatting
# -----------------------------

ax.set_ylabel("Average annual spending")
ax.set_xlabel("")

ax.set_xticks([2019, 2020, 2021, 2022, 2023, 2024])

# Tighter Y-axis for visual impact
ax.set_ylim(600, 1100)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(axis="y", alpha=0.2)

# -----------------------------
# Data labels
# -----------------------------

for _, row in data.iterrows():
    ax.text(
        row["year"],
        row["avg_spending"] + 20,
        f"${row['avg_spending']:,.0f}",
        ha="center",
        fontsize=11
    )

# -----------------------------
# Growth annotation
# -----------------------------

ax.annotate(
    "+46%",
    xy=(2024, 1016),
    xytext=(2021.5, 965),
    arrowprops=dict(arrowstyle="->", lw=1.5),
    fontsize=16,
    weight="bold"
)

# -----------------------------
# Source note
# -----------------------------

fig.text(
    0.125,
    0.02,
    "Source: Aspen Institute Project Play. 2019 value derived from reported 46% increase.",
    fontsize=9
)

# -----------------------------
# Layout
# -----------------------------

plt.tight_layout(rect=[0, 0.04, 1, 0.88])

# -----------------------------
# Save chart
# -----------------------------

output_file = Path(__file__).resolve().parents[1] / "visuals" / "family_spending_trend.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(f"Saved chart to: {output_file}")