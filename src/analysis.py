import pandas as pd

# Load dataset
file_path = "data/raw/Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

# Display basic information
print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== STATISTICAL SUMMARY =====")
print(df.describe())

# ===== DATA QUALITY CHECKS =====

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== NEGATIVE PROFIT RECORDS =====")
print((df["Profit"] < 0).sum())

print("\n===== LOSS-MAKING SALES =====")
loss_df = df[df["Profit"] < 0]
print(loss_df[["Product Name", "Sales", "Quantity", "Discount", "Profit"]].head(10))

# ===== DISCOUNT AND PROFIT ANALYSIS =====

print("\n===== PROFIT BY DISCOUNT LEVEL =====")

discount_analysis = df.groupby("Discount").agg(
    Total_Orders=("Order ID", "count"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Average_Profit=("Profit", "mean")
).reset_index()

print(discount_analysis.round(2).to_string(index=False))

# ===== PROFIT BY CATEGORY =====

print("\n===== PROFIT BY CATEGORY =====")

category_analysis = df.groupby("Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).reset_index()

print(category_analysis.round(2).to_string(index=False))

# ===== PROFIT BY SUB-CATEGORY =====

print("\n===== PROFIT BY SUB-CATEGORY =====")

subcategory_analysis = df.groupby("Sub-Category").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
).reset_index()

subcategory_analysis = subcategory_analysis.sort_values(
    by="Total_Profit",
    ascending=True
)

print(subcategory_analysis.round(2).to_string(index=False))