-- ==========================================================
-- ANALYTICS SCHEMA
-- ==========================================================

CREATE SCHEMA IF NOT EXISTS analytics;

-- ==========================================================
-- MONTHLY SALES
-- ==========================================================

CREATE OR REPLACE VIEW analytics.monthly_sales AS

SELECT

    d.year,

    d.month,

    d.month_name,

    COUNT(f.order_id) AS total_orders,

    SUM(f.quantity) AS total_items,

    ROUND(SUM(f.total_amount),2) AS revenue

FROM warehouse.fact_sales f

JOIN warehouse.dim_date d
ON f.date_key = d.date_key

GROUP BY

    d.year,
    d.month,
    d.month_name

ORDER BY

    d.year,
    d.month;


-- ==========================================================
-- TOP PRODUCTS
-- ==========================================================

CREATE OR REPLACE VIEW analytics.top_products AS

SELECT

    p.product_name,

    p.category,

    SUM(f.quantity) AS units_sold,

    ROUND(SUM(f.total_amount),2) AS revenue

FROM warehouse.fact_sales f

JOIN warehouse.dim_products p

ON f.product_key = p.product_key

GROUP BY

    p.product_name,
    p.category

ORDER BY revenue DESC;


-- ==========================================================
-- CUSTOMER SALES
-- ==========================================================

CREATE OR REPLACE VIEW analytics.customer_sales AS

SELECT

    c.customer_id,

    c.first_name,

    c.last_name,

    c.country,

    COUNT(f.order_id) AS total_orders,

    ROUND(SUM(f.total_amount),2) AS revenue

FROM warehouse.fact_sales f

JOIN warehouse.dim_customers c

ON f.customer_key = c.customer_key

GROUP BY

    c.customer_id,
    c.first_name,
    c.last_name,
    c.country

ORDER BY revenue DESC;


-- ==========================================================
-- PAYMENT SUMMARY
-- ==========================================================

CREATE OR REPLACE VIEW analytics.payment_summary AS

SELECT

    payment_method,

    payment_status,

    COUNT(*) AS total_transactions,

    ROUND(SUM(total_amount),2) AS revenue

FROM warehouse.fact_sales

GROUP BY

    payment_method,
    payment_status;


-- ==========================================================
-- SHIPMENT SUMMARY
-- ==========================================================

CREATE OR REPLACE VIEW analytics.shipment_summary AS

SELECT

    shipment_status,

    COUNT(*) AS total_orders,

    ROUND(SUM(total_amount),2) AS revenue

FROM warehouse.fact_sales

GROUP BY shipment_status;