TRUNCATE TABLE warehouse.dim_customers
RESTART IDENTITY CASCADE;

INSERT INTO warehouse.dim_customers
(
    customer_id,
    first_name,
    last_name,
    email,
    city,
    country,
    signup_date
)
SELECT
    customer_id,
    first_name,
    last_name,
    email,
    city,
    country,
    signup_date
FROM staging.stg_customers;


TRUNCATE TABLE warehouse.dim_products
RESTART IDENTITY CASCADE;

INSERT INTO warehouse.dim_products
(
    product_id,
    product_name,
    category,
    price
)
SELECT
    product_id,
    product_name,
    category,
    price
FROM staging.stg_products;


TRUNCATE TABLE warehouse.dim_date CASCADE;

INSERT INTO warehouse.dim_date
(
    date_key,
    day,
    month,
    month_name,
    quarter,
    year,
    weekday
)
SELECT DISTINCT

    order_date,

    EXTRACT(DAY FROM order_date),

    EXTRACT(MONTH FROM order_date),

    TO_CHAR(order_date,'Month'),

    EXTRACT(QUARTER FROM order_date),

    EXTRACT(YEAR FROM order_date),

    TO_CHAR(order_date,'Day')

FROM staging.stg_orders;


TRUNCATE TABLE warehouse.fact_sales
RESTART IDENTITY;

INSERT INTO warehouse.fact_sales
(
    order_id,
    customer_key,
    product_key,
    date_key,
    quantity,
    unit_price,
    total_amount,
    payment_method,
    payment_status,
    shipment_status
)

SELECT

    o.order_id,

    dc.customer_key,

    dp.product_key,

    o.order_date,

    o.quantity,

    o.unit_price,

    o.total_amount,

    p.payment_method,

    p.payment_status,

    s.shipment_status

FROM staging.stg_orders o

JOIN warehouse.dim_customers dc
    ON o.customer_id = dc.customer_id

JOIN warehouse.dim_products dp
    ON o.product_id = dp.product_id

LEFT JOIN staging.stg_payments p
    ON o.order_id = p.order_id

LEFT JOIN staging.stg_shipments s
    ON o.order_id = s.order_id;