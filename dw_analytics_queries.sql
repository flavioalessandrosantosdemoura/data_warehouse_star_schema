
-- Analytical queries for the Data Warehouse

-- 1) Top products by revenue
SELECT p.product_name, p.category, SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;

-- 2) Revenue by month
SELECT d.year_month, SUM(f.total_amount) AS monthly_revenue
FROM fact_sales f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY d.year_month
ORDER BY d.year_month;

-- 3) Revenue by customer segment (example uses customer name)
SELECT c.customer_name, SUM(f.total_amount) AS total_spent
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_spent DESC
LIMIT 10;

-- 4) Low-stock / not applicable here but sample: sales count by region
SELECT s.store_region, SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_store s ON f.store_id = s.store_id
GROUP BY s.store_region
ORDER BY revenue DESC;
