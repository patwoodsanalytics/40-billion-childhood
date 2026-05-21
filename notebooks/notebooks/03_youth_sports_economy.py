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

market_size = 40  # billions

# -----------------------------
# Style
# -----------------------------

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 22,
    "axes.labelsize": 12
})

fig, ax = plt.subplots(figsize=(12, 5))

# -----------------------------
# Bar chart
# -----------------------------

bars = ax.barh(
    ["U.S. Youth Sports Economy"],
    [market_size],
    height=0.55
)

# -----------------------------
# Titles
# -----------------------------

ax.set_title(
    "A $40 Billion Childhood",
    loc="left",
    pad=35,
    weight="bold"
)

fig.text(
    0.125,
    0.89,
    "Estimated size of the U.S. youth sports economy",
    fontsize=12
)

# -----------------------------
# Axis formatting
# -----------------------------

ax.set_xlim(0, 45)

ax.set_xlabel("Estimated Market Size (Billions USD)")
ax.set_ylabel("")

# Remove unnecessary borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

# Light grid
ax.grid(axis="x", alpha=0.2)

# -----------------------------
# Value label
# -----------------------------

ax.text(
    market_size + 0.7,
    0,
    "$40B",
    va="center",
    fontsize=22,
    weight="bold"
)

# -----------------------------
# Annotation text
# -----------------------------

fig.text(
    0.125,
    0.18,
    "Includes spending on:\n"
    "• travel tournaments\n"
    "• club fees\n"
    "• coaching and training\n"
    "• equipment and uniforms\n"
    "• hotels and travel\n"
    "• recruiting platforms and showcases",
    fontsize=11
)

# -----------------------------
# Source note
# -----------------------------

fig.text(
    0.125,
    0.02,
    "Source: Industry estimates from Aspen Institute Project Play, market research reports, and public reporting.",
    fontsize=9
)

# -----------------------------
# Layout
# -----------------------------

plt.tight_layout(rect=[0, 0.08, 1, 0.88])

# -----------------------------
# Save chart
# -----------------------------

output_file = visuals_dir / "youth_sports_economy.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Saved chart to: {output_file}")