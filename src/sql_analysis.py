import sqlite3

# Connect to database
conn = sqlite3.connect("data/processed/superstore.db")
cursor = conn.cursor()


# ==========================================================
# QUERY 1: Total Number of Records
# ==========================================================

query = """
SELECT COUNT(*)
FROM superstore;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nTotal Number of Records")

for row in results:
    print(row)


# ==========================================================
# QUERY 2: Overall Business KPIs
# ==========================================================

query = """
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Sales) / COUNT(DISTINCT "Order ID"), 2) AS Average_Order_Value
FROM superstore;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nOverall Business KPIs")

for row in results:
    print(row)


# ==========================================================
# QUERY 3: Sales and Profit by Category
# ==========================================================

query = """
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSales and Profit by Category")

for row in results:
    print(row)


# ==========================================================
# QUERY 4: Sales and Profit by Region
# ==========================================================

query = """
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSales and Profit by Region")

for row in results:
    print(row)


# ==========================================================
# QUERY 5: Sales and Profit by Customer Segment
# ==========================================================

query = """
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSales and Profit by Customer Segment")

for row in results:
    print(row)


# ==========================================================
# QUERY 6: Monthly Sales Trend
# ==========================================================

query = """
SELECT
    substr("Order Date", -4, 4) AS Year,
    CASE
        WHEN instr("Order Date", '/') = 2
        THEN '0' || substr("Order Date", 1, 1)
        ELSE substr("Order Date", 1, 2)
    END AS Month,
    ROUND(SUM(Sales), 2) AS Monthly_Sales,
    ROUND(SUM(Profit), 2) AS Monthly_Profit
FROM superstore
GROUP BY Year, Month
ORDER BY Year, Month;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nMonthly Sales Trend")

for row in results:
    print(row)


# ==========================================================
# QUERY 7: Top 10 Best-Selling Products
# ==========================================================

query = """
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nTop 10 Best-Selling Products")

for row in results:
    print(row)

# ==========================================================
# QUERY 8: Top 10 Loss-Making Products
# ==========================================================

query = """
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY "Product Name"
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nTop 10 Loss-Making Products")

for row in results:
    print(row)   

# ==========================================================
# QUERY 9: Sales and Profit by Discount Level
# ==========================================================

query = """
SELECT
    CASE
        WHEN Discount = 0 THEN 'No Discount'
        WHEN Discount <= 0.20 THEN 'Low Discount'
        WHEN Discount <= 0.50 THEN 'High Discount'
        ELSE 'Very High Discount'
    END AS Discount_Level,

    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(AVG(Discount) * 100, 2) AS Average_Discount_Percentage

FROM superstore

GROUP BY Discount_Level

ORDER BY Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSales and Profit by Discount Level")

for row in results:
    print(row)

# ==========================================================
# QUERY 10: Orders with Above-Average Sales
# ==========================================================

query = """
SELECT
    "Order ID",
    "Customer Name",
    ROUND(SUM(Sales), 2) AS Order_Sales,
    ROUND(SUM(Profit), 2) AS Order_Profit
FROM superstore
GROUP BY "Order ID", "Customer Name"
HAVING SUM(Sales) > (
    SELECT AVG(Order_Total)
    FROM (
        SELECT SUM(Sales) AS Order_Total
        FROM superstore
        GROUP BY "Order ID"
    )
)
ORDER BY Order_Sales DESC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nOrders with Above-Average Sales")

for row in results:
    print(row)    

# ==========================================================
# QUERY 11: Sales and Profit by State
# ==========================================================

query = """
SELECT
    State,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
WHERE Region = 'West'
GROUP BY State
HAVING SUM(Sales) > 50000
ORDER BY Total_Sales DESC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nTop States in West Region by Sales")

for row in results:
    print(row)

# ==========================================================
# QUERY 12: Profit and Loss Classification
# ==========================================================

query = """
SELECT
    CASE
        WHEN Profit > 0 THEN 'Profitable'
        WHEN Profit < 0 THEN 'Loss'
        ELSE 'Break-even'
    END AS Profit_Status,

    COUNT(*) AS Total_Records,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit

FROM superstore

GROUP BY Profit_Status

ORDER BY Total_Profit DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nProfit and Loss Classification")

for row in results:
    print(row)

# ==========================================================
# QUERY 13: Top 10 Customers by Profit
# ==========================================================

query = """
SELECT
    "Customer Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore
GROUP BY "Customer Name"
ORDER BY Total_Profit DESC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nTop 10 Customers by Profit")

for row in results:
    print(row)    

# ==========================================================
# QUERY 14: Bottom 10 Customers by Profit
# ==========================================================

query = """
SELECT
    "Customer Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore
GROUP BY "Customer Name"
ORDER BY Total_Profit ASC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nBottom 10 Customers by Profit")

for row in results:
    print(row)

# ==========================================================
# QUERY 15: Customer Profit Margin Analysis
# ==========================================================

query = """
SELECT
    "Customer Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY "Customer Name"
HAVING SUM(Sales) > 0
ORDER BY Profit_Margin ASC
LIMIT 10;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nBottom 10 Customers by Profit Margin")

for row in results:
    print(row)

# ==========================================================
# QUERY 16: Subcategory Profitability Analysis
# ==========================================================

query = """
SELECT
    Category,
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Category, "Sub-Category"
HAVING SUM(Sales) > 0
ORDER BY Profit_Margin ASC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSubcategory Profitability Analysis")

for row in results:
    print(row)    

# ==========================================================
# QUERY 17: Sales and Profit by Shipping Mode
# ==========================================================

query = """
SELECT
    "Ship Mode",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY "Ship Mode"
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSales and Profit by Shipping Mode")

for row in results:
    print(row)    

# ==========================================================
# QUERY 18: Sales and Profit by Region and Category
# ==========================================================

query = """
SELECT
    Region,
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Region, Category
ORDER BY Region, Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSales and Profit by Region and Category")

for row in results:
    print(row)    

# ==========================================================
# QUERY 19: Rank Subcategories by Profit Within Each Region
# ==========================================================

query = """
SELECT
    Region,
    "Sub-Category",
    ROUND(SUM(Profit), 2) AS Total_Profit,
    RANK() OVER (
        PARTITION BY Region
        ORDER BY SUM(Profit) DESC
    ) AS Profit_Rank
FROM superstore
GROUP BY Region, "Sub-Category"
ORDER BY Region, Profit_Rank;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSubcategory Profit Rankings by Region")

for row in results:
    print(row)  

# ==========================================================
# QUERY 20: State Performance Using a CTE
# ==========================================================

query = """
WITH StateSales AS (
    SELECT
        State,
        ROUND(SUM(Sales), 2) AS Total_Sales,
        ROUND(SUM(Profit), 2) AS Total_Profit
    FROM superstore
    GROUP BY State
)
SELECT
    State,
    Total_Sales,
    Total_Profit,
    ROUND(Total_Profit / Total_Sales * 100, 2) AS Profit_Margin
FROM StateSales
WHERE Total_Sales > 50000
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nState Performance Using CTE")

for row in results:
    print(row)      

# ==========================================================
# QUERY 21: Search Products Using LIKE
# ==========================================================

query = """
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM superstore
WHERE "Product Name" LIKE '%Chair%'
GROUP BY "Product Name"
ORDER BY Total_Sales DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nProducts Containing 'Chair'")

for row in results:
    print(row)    

# ==========================================================
# QUERY 22: Sales and Profit by Year
# ==========================================================

query = """
SELECT
    substr("Order Date", -4, 4) AS Order_Year,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore
GROUP BY Order_Year
ORDER BY Order_Year;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nSales and Profit by Year")

for row in results:
    print(row)    

# ==========================================================
# QUERY 23: Year-over-Year Sales Growth Using LAG
# ==========================================================

query = """
WITH YearlySales AS (
    SELECT
        substr("Order Date", -4, 4) AS Order_Year,
        SUM(Sales) AS Total_Sales
    FROM superstore
    GROUP BY Order_Year
)
SELECT
    Order_Year,
    ROUND(Total_Sales, 2) AS Current_Year_Sales,
    ROUND(
        LAG(Total_Sales) OVER (ORDER BY Order_Year),
        2
    ) AS Previous_Year_Sales,
    ROUND(
        Total_Sales - LAG(Total_Sales) OVER (ORDER BY Order_Year),
        2
    ) AS Sales_Growth,
    ROUND(
        (Total_Sales - LAG(Total_Sales) OVER (ORDER BY Order_Year))
        / LAG(Total_Sales) OVER (ORDER BY Order_Year) * 100,
        2
    ) AS Growth_Percentage
FROM YearlySales
ORDER BY Order_Year;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nYear-over-Year Sales Growth")

for row in results:
    print(row)    

# ==========================================================
# QUERY 24: High-Discount Loss-Making Subcategories
# ==========================================================

query = """
SELECT
    Category,
    "Sub-Category",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(AVG(Discount) * 100, 2) AS Average_Discount_Percentage,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Category, "Sub-Category"
HAVING AVG(Discount) >= 0.20
   AND SUM(Profit) < 0
ORDER BY Total_Profit ASC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nHigh-Discount Loss-Making Subcategories")

for row in results:
    print(row)    

# ==========================================================
# QUERY 25: Order Profitability Classification
# ==========================================================

query = """
WITH OrderSummary AS (
    SELECT
        "Order ID",
        SUM(Sales) AS Order_Sales,
        SUM(Profit) AS Order_Profit
    FROM superstore
    GROUP BY "Order ID"
)
SELECT
    CASE
        WHEN Order_Profit > 0 THEN 'Profitable Orders'
        WHEN Order_Profit < 0 THEN 'Loss-Making Orders'
        ELSE 'Break-Even Orders'
    END AS Order_Status,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Order_Sales), 2) AS Total_Sales,
    ROUND(SUM(Order_Profit), 2) AS Total_Profit,
    ROUND(AVG(Order_Sales), 2) AS Average_Order_Sales,
    ROUND(AVG(Order_Profit), 2) AS Average_Order_Profit
FROM OrderSummary
GROUP BY Order_Status
ORDER BY Total_Profit DESC;
"""

cursor.execute(query)
results = cursor.fetchall()

print("\nOrder Profitability Classification")

for row in results:
    print(row)    
conn.close()