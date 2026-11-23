-- ============================================================
-- FILE 05: CUSTOMER ANALYSIS
-- ============================================================

-- QUERY 13: Top 10 Customers by Profit
SELECT
    "Customer Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore
GROUP BY "Customer Name"
ORDER BY Total_Profit DESC
LIMIT 10;


-- QUERY 14: Bottom 10 Customers by Profit
SELECT
    "Customer Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders
FROM superstore
GROUP BY "Customer Name"
ORDER BY Total_Profit ASC
LIMIT 10;


-- QUERY 15: Bottom Customers by Profit Margin
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

