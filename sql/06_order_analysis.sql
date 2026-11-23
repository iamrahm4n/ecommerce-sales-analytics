-- ============================================================
-- FILE 06: ORDER ANALYSIS
-- ============================================================

-- QUERY 10: Orders with Above-Average Sales
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


-- QUERY 12: Profit/Loss Classification
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


-- QUERY 17: Sales and Profit by Shipping Mode
SELECT
    "Ship Mode",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY "Ship Mode"
ORDER BY Total_Sales DESC;


-- QUERY 22: Sales and Profit by Year
SELECT
    substr("Order Date", -4, 4) AS Order_Year,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore
GROUP BY Order_Year
ORDER BY Order_Year;


-- QUERY 25: Order Profitability Classification
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

