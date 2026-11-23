-- ============================================================
-- FILE 03: REGIONAL ANALYSIS
-- ============================================================

-- QUERY 4: Sales and Profit by Region
SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Region
ORDER BY Total_Sales DESC;


-- QUERY 11: Sales and Profit by State (West Region)
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


-- QUERY 18: Sales and Profit by Region and Category
SELECT
    Region,
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM superstore
GROUP BY Region, Category
ORDER BY Region, Total_Sales DESC;


-- QUERY 20: State Performance Using CTE
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

