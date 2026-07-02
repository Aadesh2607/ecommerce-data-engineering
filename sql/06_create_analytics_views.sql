CREATE SCHEMA IF NOT EXISTS analytics;

--------------------------------------------------
-- Sales Summary
--------------------------------------------------
CREATE OR REPLACE VIEW analytics.sales_summary AS

SELECT

    d.year,
    d.month,
    d.month_name,

    COUNT(f.order_id) AS total_orders,

    SUM(f.quantity) AS total_quantity,

    SUM(f.total_amount) AS total_sales,

    AVG(f.total_amount) AS average_order_value

FROM warehouse.fact_sales f

JOIN warehouse.dim_date d
ON f.date_key = d.date_key

GROUP BY

    d.year,
    d.month,
    d.month_name;

--------------------------------------------------
-- Product Performance
--------------------------------------------------
CREATE OR REPLACE VIEW analytics.product_summary AS

SELECT

    p.product_name,

    p.category,

    COUNT(f.order_id) AS orders,

    SUM(f.quantity) AS quantity_sold,

    SUM(f.total_amount) AS revenue

FROM warehouse.fact_sales f

JOIN warehouse.dim_products p
ON f.product_key = p.product_key

GROUP BY

    p.product_name,
    p.category;

--------------------------------------------------
-- Customer Summary
--------------------------------------------------
CREATE OR REPLACE VIEW analytics.customer_summary AS

SELECT

    c.customer_id,

    c.first_name,

    c.last_name,

    c.city,

    c.country,

    COUNT(f.order_id) AS total_orders,

    SUM(f.total_amount) AS total_spent,

    AVG(f.total_amount) AS average_order

FROM warehouse.fact_sales f

JOIN warehouse.dim_customers c
ON f.customer_key = c.customer_key

GROUP BY

    c.customer_id,
    c.first_name,
    c.last_name,
    c.city,
    c.country;