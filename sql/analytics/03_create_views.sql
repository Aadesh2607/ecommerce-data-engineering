CREATE OR REPLACE VIEW analytics.sales_summary AS
SELECT
    d.year,
    d.month,
    p.category,
    COUNT(f.sales_key) AS total_orders,
    SUM(f.quantity) AS total_quantity,
    SUM(f.total_amount) AS total_sales
FROM warehouse.fact_sales f
JOIN warehouse.dim_products p
ON f.product_key = p.product_key
JOIN warehouse.dim_date d
ON f.date_key = d.date_key
GROUP BY
    d.year,
    d.month,
    p.category;