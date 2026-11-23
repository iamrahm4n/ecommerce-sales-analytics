import pandas as pd

# Load dataset
file_path = "data/raw/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Regional sales and profit analysis
region_analysis = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
)

# Sort by sales
region_analysis = region_analysis.sort_values(
    by="Total_Sales", ascending=False
)

print("\nRegional Sales & Profit Analysis")
print(region_analysis.round(2))

# Profit margin calculation
region_analysis["Profit_Margin_%"] = (
    region_analysis["Total_Profit"] / region_analysis["Total_Sales"] * 100
)

print("\nRegional Profit Margins")
print(region_analysis[["Profit_Margin_%"]].round(2))

import matplotlib.pyplot as plt

# Regional Sales vs Profit Visualization
regions = region_analysis.index
sales = region_analysis["Total_Sales"]
profits = region_analysis["Total_Profit"]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sales chart
axes[0].bar(regions, sales)
axes[0].set_title("Sales by Region")
axes[0].set_ylabel("Total Sales")
axes[0].tick_params(axis="x", rotation=45)

# Profit chart
axes[1].bar(regions, profits)
axes[1].set_title("Profit by Region")
axes[1].set_ylabel("Total Profit")
axes[1].tick_params(axis="x", rotation=45)

plt.tight_layout()

plt.savefig("reports/regional_sales_vs_profit.png", dpi=300)
plt.close()

print("\nRegional Sales vs Profit chart saved successfully!")