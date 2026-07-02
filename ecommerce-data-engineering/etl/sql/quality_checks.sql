-- ============================================================
-- DATA QUALITY CHECKS
-- ============================================================

-- name: staging_tables_not_empty
SELECT 'stg_customers' AS table_name, COUNT(*) AS row_count
FROM staging.stg_customers

UNION ALL

SELECT 'stg_products', COUNT(*)
FROM staging.stg_products

UNION ALL

SELECT 'stg_orders', COUNT(*)
FROM staging.stg_orders

UNION ALL

SELECT 'stg_payments', COUNT(*)
FROM staging.stg_payments

UNION ALL

SELECT 'stg_shipments', COUNT(*)
FROM staging.stg_shipments;

-- name: duplicate_customer_ids
SELECT customer_id, COUNT(*)
FROM staging.stg_customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- name: duplicate_product_ids
SELECT product_id, COUNT(*)
FROM staging.stg_products
GROUP BY product_id
HAVING COUNT(*) > 1;

-- name: duplicate_order_ids
SELECT order_id, COUNT(*)
FROM staging.stg_orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- name: null_customer_ids
SELECT COUNT(*) AS null_customer_ids
FROM staging.stg_customers
WHERE customer_id IS NULL;

-- name: null_product_ids
SELECT COUNT(*) AS null_product_ids
FROM staging.stg_products
WHERE product_id IS NULL;

-- name: null_order_ids
SELECT COUNT(*) AS null_order_ids
FROM staging.stg_orders
WHERE order_id IS NULL;

-- name: orphan_orders
SELECT COUNT(*) AS orphan_orders
FROM staging.stg_orders o
LEFT JOIN staging.stg_customers c
ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- name: orphan_products
SELECT COUNT(*) AS orphan_products
FROM staging.stg_orders o
LEFT JOIN staging.stg_products p
ON o.product_id = p.product_id
WHERE p.product_id IS NULL;

-- name: warehouse_row_counts
SELECT
    (SELECT COUNT(*) FROM warehouse.dim_customers) AS dim_customers,
    (SELECT COUNT(*) FROM warehouse.dim_products) AS dim_products,
    (SELECT COUNT(*) FROM warehouse.fact_sales) AS fact_sales;