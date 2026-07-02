-- Customers
ALTER TABLE staging.stg_customers
ADD CONSTRAINT pk_stg_customers
PRIMARY KEY (customer_id);

-- Products
ALTER TABLE staging.stg_products
ADD CONSTRAINT pk_stg_products
PRIMARY KEY (product_id);

-- Orders
ALTER TABLE staging.stg_orders
ADD CONSTRAINT pk_stg_orders
PRIMARY KEY (order_id);

-- Payments
ALTER TABLE staging.stg_payments
ADD CONSTRAINT pk_stg_payments
PRIMARY KEY (payment_id);

-- Shipments
ALTER TABLE staging.stg_shipments
ADD CONSTRAINT pk_stg_shipments
PRIMARY KEY (shipment_id);