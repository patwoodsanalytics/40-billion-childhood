import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# Create visuals directory
# -----------------------------

visuals_dir = Path("visuals")
visuals_dir.mkdir(exist_ok=True)

# -----------------------------
# Data (billions USD)
# Approximate public estimates
# -----------------------------

data = pd.DataFrame({
    "category": [
        "Youth Sports Economy",
        "Minor League Baseball",
        "WNBA Revenue"
    ],
    "billions_usd": [
        40.0,
        1.2,
        0.2
    ]
})

# Sort largest to smallest
data = data.sort_values("billions_usd")

# -----------------------------
# Style
# -----------------------------

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 20,
    "axes.labelsize": 12
})

fig, ax = plt.subplots(figsize=(11, 6))

# -----------------------------
# Bar chart
# -----------------------------

bars = ax.barh(
    data["category"],
    data["billions_usd"]
)

# -----------------------------
# Titles
# -----------------------------

ax.set_title(
    "The Scale of the Youth Sports Economy",
    loc="left",
    pad=35,
    weight="bold"
)

fig.text(
    0.125,
    0.89,
    "Estimated annual revenue/economic activity (billions USD)",
    fontsize=11
)

# -----------------------------
# Axis formatting
# -----------------------------

ax.set_xlim(0, 45)

ax.set_xlabel("Billions USD")
ax.set_ylabel("")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

ax.grid(axis="x", alpha=0.2)

# -----------------------------
# Labels
# -----------------------------

for bar in bars:
    width = bar.get_width()

    label = f"${width:.1f}B"

    ax.text(
        width + 0.5,
        bar.get_y() + bar.get_height()/2,
        label,
        va="center",
        fontsize=11,
        weight="bold"
    )

# -----------------------------
# Source note
# -----------------------------

fig.text(
    0.125,
    0.02,
    "Sources: Aspen Institute Project Play, public sports industry reporting, Forbes estimates.",
    fontsize=9
)

# -----------------------------
# Layout
# -----------------------------

plt.tight_layout(rect=[0, 0.04, 1, 0.88])

# -----------------------------
# Save chart
# -----------------------------

output_file = visuals_dir / "youth_sports_comparison.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Saved chart to: {output_file}")