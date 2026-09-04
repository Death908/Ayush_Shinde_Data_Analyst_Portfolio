-- E-Commerce Sales Performance Analysis
-- Portfolio project | Synthetic dataset

-- 1. Overall KPIs
SELECT
    SUM(Revenue) AS total_revenue,
    SUM(Profit) AS total_profit,
    COUNT(DISTINCT Order_ID) AS total_orders,
    SUM(Units_Sold) AS units_sold,
    AVG(Revenue) AS average_order_value,
    SUM(Profit) / NULLIF(SUM(Revenue), 0) AS profit_margin
FROM Cleaned_Data;

-- 2. Monthly performance
SELECT
    Month,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    COUNT(DISTINCT Order_ID) AS orders,
    SUM(Units_Sold) AS units_sold
FROM Cleaned_Data
GROUP BY Month
ORDER BY Month;

-- 3. Regional performance
SELECT
    Region,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    COUNT(DISTINCT Order_ID) AS orders
FROM Cleaned_Data
GROUP BY Region
ORDER BY revenue DESC;

-- 4. Category performance
SELECT
    Category,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    SUM(Units_Sold) AS units_sold,
    SUM(Profit) / NULLIF(SUM(Revenue), 0) AS profit_margin
FROM Cleaned_Data
GROUP BY Category
ORDER BY revenue DESC;

-- 5. Top 10 products by revenue
SELECT
    Product,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    SUM(Units_Sold) AS units_sold
FROM Cleaned_Data
GROUP BY Product
ORDER BY revenue DESC
LIMIT 10;

-- 6. Sales channel performance
SELECT
    Sales_Channel,
    SUM(Revenue) AS revenue,
    SUM(Profit) AS profit,
    COUNT(DISTINCT Order_ID) AS orders
FROM Cleaned_Data
GROUP BY Sales_Channel
ORDER BY revenue DESC;
