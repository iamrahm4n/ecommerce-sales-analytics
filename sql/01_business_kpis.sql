-- ============================================================
-- E-COMMERCE SALES ANALYTICS
-- FILE 01: BUSINESS KPIs
-- ============================================================

-- QUERY 1: Total Records
SELECT COUNT(*) AS Total_Records
FROM superstore;


-- QUERY 2: Overall Business KPIs
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Sales) / COUNT(DISTINCT "Order ID"), 2) AS Average_Order_Value
FROM superstore;


-- QUERY 3: Sales and Profit by Category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;


-- QUERY 4: Sales and Profit by Region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;


-- QUERY 5: Sales and Profit by Customer Segment
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;

