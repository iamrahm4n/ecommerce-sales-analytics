
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "data/raw/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Calculate sales and profit by category
category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

# Create charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sales chart
axes[0].bar(category_analysis["Category"], category_analysis["Total_Sales"])
axes[0].set_title("Total Sales by Category")
axes[0].set_ylabel("Sales")
axes[0].tick_params(axis="x", rotation=15)

# Profit chart
axes[1].bar(category_analysis["Category"], category_analysis["Total_Profit"])
axes[1].set_title("Total Profit by Category")
axes[1].set_ylabel("Profit")
axes[1].tick_params(axis="x", rotation=15)

plt.tight_layout()

# Save chart
plt.savefig("reports/sales_vs_profit_by_category.png", dpi=300, bbox_inches="tight")

plt.show()
