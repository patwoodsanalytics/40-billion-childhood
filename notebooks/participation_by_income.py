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

data = pd.DataFrame({
    "income_group": [
        "Below Poverty Level",
        "100–199% FPL",
        "200–399% FPL",
        "400%+ FPL"
    ],
    "participation_rate": [
        31.2,
        45.0,
        58.0,
        70.2
    ]
})

# -----------------------------
# Style settings
# -----------------------------

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 18,
    "axes.labelsize": 12
})

# -----------------------------
# Create figure
# -----------------------------

fig, ax = plt.subplots(figsize=(11, 6))

# -----------------------------
# Create bars
# -----------------------------

bars = ax.barh(
    data["income_group"],
    data["participation_rate"]
)

# -----------------------------
# Titles
# -----------------------------

ax.set_title(
    "Youth Sports Participation by Household Income",
    loc="left",
    pad=40,
    weight="bold"
)

fig.text(
    0.125,
    0.885,
    "Children ages 6–17 participating in organized sports",
    fontsize=11
)

# -----------------------------
# Axis formatting
# -----------------------------

ax.set_xlim(0, 80)

ax.set_xlabel("Participation Rate (%)")
ax.set_ylabel("")

# Remove unnecessary borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Light vertical grid
ax.grid(axis="x", alpha=0.2)

# -----------------------------
# Add percentage labels
# -----------------------------

for bar in bars:
    width = bar.get_width()

    ax.text(
        width + 1,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.1f}%",
        va="center",
        fontsize=11
    )

# -----------------------------
# Source note
# -----------------------------

fig.text(
    0.125,
    0.02,
    "Source: CDC/NCHS National Health Interview Survey",
    fontsize=9
)

# -----------------------------
# Layout adjustment
# -----------------------------

plt.tight_layout(rect=[0, 0.04, 1, 0.88])

# -----------------------------
# Save chart
# -----------------------------

output_file = visuals_dir / "participation_by_income_v3.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Saved chart to: {output_file}")