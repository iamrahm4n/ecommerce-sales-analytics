import pandas as pd

# Load dataset
file_path = "data/raw/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

print(df[["Order Date", "Sales"]].head())

print("\nDate conversion completed successfully.")

# Extract year and month
df["Year_Month"] = df["Order Date"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = df.groupby("Year_Month")["Sales"].sum()

print("\n===== MONTHLY SALES =====")
print(monthly_sales.round(2).to_string())

import matplotlib.pyplot as plt

# Convert monthly periods into timestamps for plotting
monthly_sales.index = monthly_sales.index.to_timestamp()

# Create monthly sales trend chart
plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

# Save chart
plt.savefig("reports/monthly_sales_trend.png", dpi=300, bbox_inches="tight")

plt.show()

# ===== SALES BY MONTH OF YEAR =====

df["Month"] = df["Order Date"].dt.month

month_sales = df.groupby("Month")["Sales"].sum().sort_values(ascending=False)

print("\n===== SALES BY MONTH =====")

print(month_sales.round(2).to_string())

# ===== SALES BY CALENDAR MONTH =====

month_sales = df.groupby(df["Order Date"].dt.month)["Sales"].sum()

month_names = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

month_sales.index = month_names

plt.figure(figsize=(10, 6))

plt.bar(month_sales.index, month_sales.values)

plt.title("Total Sales by Month (2014–2017)")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()

plt.savefig("reports/sales_by_month.png", dpi=300, bbox_inches="tight")

plt.close()