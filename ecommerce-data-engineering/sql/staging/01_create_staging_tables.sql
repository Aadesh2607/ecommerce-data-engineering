-- ==========================================
-- Create Schemas
-- ==========================================

CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS warehouse;
CREATE SCHEMA IF NOT EXISTS analytics;

-- ==========================================
-- Customers
-- ==========================================

CREATE TABLE IF NOT EXISTS staging.stg_customers (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    signup_date DATE
);

-- ==========================================
-- Products
-- ==========================================

CREATE TABLE IF NOT EXISTS staging.stg_products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(100),
    price NUMERIC(10,2)
);

-- ==========================================
-- Orders
-- ==========================================

CREATE TABLE IF NOT EXISTS staging.stg_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(12,2),
    order_date DATE
);

-- ==========================================
-- Payments
-- ==========================================

CREATE TABLE IF NOT EXISTS staging.stg_payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    payment_date DATE
);

-- ==========================================
-- Shipments
-- ==========================================

CREATE TABLE IF NOT EXISTS staging.stg_shipments (
    shipment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    shipment_status VARCHAR(50),
    shipment_date DATE
);