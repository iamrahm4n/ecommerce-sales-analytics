-- ============================================================
-- FILE 04: PRODUCT ANALYSIS
-- ============================================================

-- QUERY 7: Top 10 Best-Selling Products
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM superstore
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;


-- QUERY 8: Top 10 Loss-Making Products
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


-- QUERY 9: Sales and Profit by Discount Level
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


-- QUERY 21: Search Products Using LIKE
SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM superstore
WHERE "Product Name" LIKE '%Chair%'
GROUP BY "Product Name"
ORDER BY Total_Sales DESC;

