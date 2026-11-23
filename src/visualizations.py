
import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/raw/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 8))

bars = ax.barh(
    subcategory_profit.index,
    subcategory_profit.values
)

ax.set_title("Profit by Product Subcategory", fontsize=16)
ax.set_xlabel("Total Profit")
ax.set_ylabel("Subcategory")
ax.axvline(0, color="black", linewidth=0.8)

# Display profit values on bars
for bar in bars:
    width = bar.get_width()
    ax.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f"{width:,.0f}",
        va="center",
        ha="left" if width >= 0 else "right",
        fontsize=8
    )

plt.tight_layout()
plt.savefig("reports/profit_by_subcategory.png", dpi=300, bbox_inches="tight")
plt.show()
