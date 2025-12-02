
-- DDL: Star Schema for Sales Data Warehouse

CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    date TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    year_month TEXT
);

CREATE TABLE dim_customer (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    customer_email TEXT
);

CREATE TABLE dim_product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT
);

CREATE TABLE dim_store (
    store_id INTEGER PRIMARY KEY,
    store_region TEXT
);

CREATE TABLE fact_sales (
    sale_id INTEGER PRIMARY KEY,
    date_id INTEGER,
    customer_id INTEGER,
    product_id INTEGER,
    store_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    total_amount REAL,
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY(customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY(product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY(store_id) REFERENCES dim_store(store_id)
);
