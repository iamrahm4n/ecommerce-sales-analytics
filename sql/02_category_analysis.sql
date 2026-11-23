-- ============================================================
-- FILE 02: CATEGORY ANALYSIS
-- ============================================================

-- QUERY 16: Subcategory Profitability Analysis
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


-- QUERY 24: High-Discount Loss-Making Subcategories
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

