-- ==========================================
-- WAREHOUSE SCHEMA
-- ==========================================

CREATE SCHEMA IF NOT EXISTS warehouse;

-- ==========================================
-- DIMENSION: CUSTOMERS
-- ==========================================

CREATE TABLE IF NOT EXISTS warehouse.dim_customers (
    customer_key SERIAL PRIMARY KEY,
    customer_id INTEGER UNIQUE,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255),
    city VARCHAR(100),
    country VARCHAR(100),
    signup_date DATE
);

-- ==========================================
-- DIMENSION: PRODUCTS
-- ==========================================

CREATE TABLE IF NOT EXISTS warehouse.dim_products (
    product_key SERIAL PRIMARY KEY,
    product_id INTEGER UNIQUE,
    product_name VARCHAR(255),
    category VARCHAR(100),
    price NUMERIC(10,2)
);

-- ==========================================
-- DIMENSION: DATE
-- ==========================================

CREATE TABLE IF NOT EXISTS warehouse.dim_date (
    date_key DATE PRIMARY KEY,
    day INTEGER,
    month INTEGER,
    month_name VARCHAR(20),
    quarter INTEGER,
    year INTEGER,
    weekday VARCHAR(20)
);

-- ==========================================
-- FACT TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS warehouse.fact_sales (
    sales_key SERIAL PRIMARY KEY,
    order_id INTEGER,
    customer_key INTEGER,
    product_key INTEGER,
    date_key DATE,
    quantity INTEGER,
    unit_price NUMERIC(10,2),
    total_amount NUMERIC(12,2),
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    shipment_status VARCHAR(50)
);