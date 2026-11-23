-- ============================================================
-- FILE 07: ADVANCED SQL
-- ============================================================

-- QUERY 6: Monthly Sales and Profit
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


-- QUERY 19: Rank Subcategories by Profit Within Each Region
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


-- QUERY 23: Year-over-Year Sales Growth Using LAG
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
        LAG(Total_Sales) OVER (ORDER BY Order_Year), 2
    ) AS Previous_Year_Sales,
    ROUND(
        Total_Sales - LAG(Total_Sales) OVER (ORDER BY Order_Year), 2
    ) AS Sales_Growth,
    ROUND(
        (Total_Sales - LAG(Total_Sales) OVER (ORDER BY Order_Year))
        / LAG(Total_Sales) OVER (ORDER BY Order_Year) * 100,
        2
    ) AS Growth_Percentage
FROM YearlySales
ORDER BY Order_Year;

