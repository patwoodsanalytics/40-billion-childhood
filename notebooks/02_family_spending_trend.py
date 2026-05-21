import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

visuals_dir = Path("visuals")
visuals_dir.mkdir(exist_ok=True)

# Aspen Institute / Project Play reported 2024 average spending of $1,016,
# up 46% since 2019. 2019 value is derived as 1016 / 1.46.
data = pd.DataFrame({
    "year": [2019, 2024],
    "avg_spending": [1016 / 1.46, 1016]
})

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 18,
    "axes.labelsize": 12
})

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    data["year"],
    data["avg_spending"],
    marker="o",
    linewidth=3
)

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

ax.set_ylabel("Average annual spending")
ax.set_xlabel("")
ax.set_xticks(data["year"])
ax.set_ylim(0, 1200)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.grid(axis="y", alpha=0.2)

for _, row in data.iterrows():
    ax.text(
        row["year"],
        row["avg_spending"] + 45,
        f"${row['avg_spending']:,.0f}",
        ha="center",
        fontsize=11
    )

ax.annotate(
    "+46%",
    xy=(2024, 1016),
    xytext=(2021.5, 950),
    arrowprops=dict(arrowstyle="->", lw=1.5),
    fontsize=14,
    weight="bold"
)

fig.text(
    0.125,
    0.02,
    "Source: Aspen Institute Project Play. 2019 value derived from reported 46% increase.",
    fontsize=9
)

plt.tight_layout(rect=[0, 0.04, 1, 0.88])

output_file = visuals_dir / "family_spending_trend.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print(f"Saved chart to: {output_file}")