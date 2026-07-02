--------------------------------------------------
-- STAGING
--------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_orders_customer
ON staging.stg_orders(customer_id);

CREATE INDEX IF NOT EXISTS idx_orders_product
ON staging.stg_orders(product_id);

CREATE INDEX IF NOT EXISTS idx_orders_date
ON staging.stg_orders(order_date);

CREATE INDEX IF NOT EXISTS idx_payments_order
ON staging.stg_payments(order_id);

CREATE INDEX IF NOT EXISTS idx_shipments_order
ON staging.stg_shipments(order_id);

--------------------------------------------------
-- WAREHOUSE DIMENSIONS
--------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_dim_customer_id
ON warehouse.dim_customers(customer_id);

CREATE INDEX IF NOT EXISTS idx_dim_product_id
ON warehouse.dim_products(product_id);

CREATE INDEX IF NOT EXISTS idx_dim_date
ON warehouse.dim_date(date_key);

--------------------------------------------------
-- FACT TABLE
--------------------------------------------------

CREATE INDEX IF NOT EXISTS idx_fact_customer
ON warehouse.fact_sales(customer_key);

CREATE INDEX IF NOT EXISTS idx_fact_product
ON warehouse.fact_sales(product_key);

CREATE INDEX IF NOT EXISTS idx_fact_date
ON warehouse.fact_sales(date_key);

CREATE INDEX IF NOT EXISTS idx_fact_order
ON warehouse.fact_sales(order_id);