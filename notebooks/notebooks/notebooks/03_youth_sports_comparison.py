import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# Create visuals directory
# -----------------------------

visuals_dir = Path("visuals")
visuals_dir.mkdir(exist_ok=True)

# -----------------------------
# Style
# -----------------------------

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 22
})

# -----------------------------
# Create figure
# -----------------------------

fig, ax = plt.subplots(figsize=(12, 7))

# Remove axes
ax.axis("off")

# -----------------------------
# Main headline number
# -----------------------------

fig.text(
    0.5,
    0.68,
    "$40 BILLION",
    ha="center",
    fontsize=42,
    weight="bold"
)

# -----------------------------
# Subtitle
# -----------------------------

fig.text(
    0.5,
    0.58,
    "Estimated annual size of the U.S. youth sports economy",
    ha="center",
    fontsize=15
)

# -----------------------------
# Included spending categories
# -----------------------------

fig.text(
    0.23,
    0.34,
    "Includes:",
    fontsize=13,
    weight="bold"
)

fig.text(
    0.23,
    0.18,
    "• club fees\n"
    "• tournament travel\n"
    "• coaching and training\n"
    "• recruiting platforms\n"
    "• apparel and equipment\n"
    "• showcases and camps",
    fontsize=12
)

# -----------------------------
# Comparison section
# -----------------------------

fig.text(
    0.62,
    0.34,
    "For comparison:",
    fontsize=13,
    weight="bold"
)

fig.text(
    0.62,
    0.18,
    "WNBA annual revenue ≈ $200M\n\n"
    "Minor League Baseball ≈ $1.2B",
    fontsize=12
)

# -----------------------------
# Source note
# -----------------------------

fig.text(
    0.12,
    0.05,
    "Sources: Aspen Institute Project Play, public industry reporting, Forbes estimates.",
    fontsize=9
)

# -----------------------------
# Save chart
# -----------------------------

output_file = visuals_dir / "youth_sports_comparison.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print(f"Saved chart to: {output_file}")