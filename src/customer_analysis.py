import pandas as pd

# Load dataset
file_path = "data/raw/Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Customer segment analysis
segment_analysis = df.groupby("Segment").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique"),
    Total_Quantity=("Quantity", "sum")
)

# Sort by sales
segment_analysis = segment_analysis.sort_values(
    by="Total_Sales", ascending=False
)

print("\nCustomer Segment Analysis")
print(segment_analysis.round(2))

# Top 10 customers by sales

customer_sales = df.groupby("Customer Name").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Orders=("Order ID", "nunique")
)

top_10_customers = customer_sales.sort_values(
    by="Total_Sales", ascending=False
).head(10)

print("\nTop 10 Customers by Sales")
print(top_10_customers.round(2))

# Top 10 customers by profit

top_10_profit_customers = customer_sales.sort_values(
    by="Total_Profit", ascending=False
).head(10)

print("\nTop 10 Customers by Profit")
print(top_10_profit_customers.round(2))

import matplotlib.pyplot as plt

# Top 10 customers by sales visualization
top_customers = customer_sales.sort_values(
    by="Total_Sales", ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(12, 6))

x = range(len(top_customers))
width = 0.4

ax.bar(
    [i - width/2 for i in x],
    top_customers["Total_Sales"],
    width,
    label="Sales"
)

ax.bar(
    [i + width/2 for i in x],
    top_customers["Total_Profit"],
    width,
    label="Profit"
)

ax.set_title("Top 10 Customers: Sales vs Profit")
ax.set_ylabel("Amount ($)")
ax.set_xticks(list(x))
ax.set_xticklabels(top_customers.index, rotation=45, ha="right")
ax.legend()

plt.tight_layout()

plt.savefig("reports/top_10_customers_sales_vs_profit.png", dpi=300)
plt.close()

print("\nTop 10 Customers Sales vs Profit chart saved successfully!")

# Low-profit customers analysis

customer_profit_analysis = customer_sales.sort_values(
    by="Total_Profit", ascending=True
)

print("\nBottom 10 Customers by Profit")
print(customer_profit_analysis.head(10).round(2))

# Customer profit margin analysis

customer_sales["Profit_Margin_%"] = (
    customer_sales["Total_Profit"] / customer_sales["Total_Sales"] * 100
)

# Lowest profit margins
low_margin_customers = customer_sales.sort_values(
    by="Profit_Margin_%", ascending=True
).head(10)

print("\n10 Customers with Lowest Profit Margins")
print(low_margin_customers.round(2))

# Top 10 loss-making customers visualization

worst_customers = customer_sales.sort_values(
    by="Total_Profit", ascending=True
).head(10)

fig, ax = plt.subplots(figsize=(12, 6))

ax.barh(
    worst_customers.index,
    worst_customers["Total_Profit"]
)

ax.set_title("Top 10 Loss-Making Customers")
ax.set_xlabel("Profit / Loss ($)")
ax.set_ylabel("Customer Name")
ax.axvline(0, linewidth=1)

plt.tight_layout()

plt.savefig("reports/top_10_loss_making_customers.png", dpi=300)
plt.close()

print("\nTop 10 Loss-Making Customers chart saved successfully!")