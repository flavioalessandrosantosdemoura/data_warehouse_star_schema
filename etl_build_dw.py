
import pandas as pd
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
raw = pd.read_csv(BASE / "raw_sales.csv", parse_dates=["transaction_date"])

# DIM_DATE
raw["date"] = pd.to_datetime(raw["transaction_date"])
dim_date = raw[["date"]].drop_duplicates().sort_values("date").reset_index(drop=True)
dim_date["date_id"] = dim_date.index + 1
dim_date["year"] = dim_date["date"].dt.year
dim_date["month"] = dim_date["date"].dt.month
dim_date["day"] = dim_date["date"].dt.day
dim_date["year_month"] = dim_date["date"].dt.strftime("%Y-%m")
dim_date = dim_date[["date_id","date","year","month","day","year_month"]]

# DIM_CUSTOMER
dim_customer = raw[["customer_name","customer_email"]].drop_duplicates().reset_index(drop=True)
dim_customer["customer_id"] = dim_customer.index + 1
dim_customer = dim_customer[["customer_id","customer_name","customer_email"]]

# DIM_PRODUCT
dim_product = raw[["product_name","category"]].drop_duplicates().reset_index(drop=True)
dim_product["product_id"] = dim_product.index + 1
dim_product = dim_product[["product_id","product_name","category"]]

# DIM_STORE
dim_store = raw[["store_region"]].drop_duplicates().reset_index(drop=True)
dim_store["store_id"] = dim_store.index + 1
dim_store = dim_store[["store_id","store_region"]]

# FACT_SALES
fact = raw.merge(dim_date, left_on=pd.to_datetime(raw["transaction_date"]), right_on="date")           .merge(dim_customer, on=["customer_name","customer_email"])           .merge(dim_product, on=["product_name","category"])           .merge(dim_store, on="store_region")

fact["sale_id"] = fact["transaction_id"]
fact["quantity"] = fact["quantity"]
fact["unit_price"] = fact["unit_price"]
fact["total_amount"] = fact["quantity"] * fact["unit_price"]
fact_sales = fact[["sale_id","date_id","customer_id","product_id","store_id","quantity","unit_price","total_amount"]]

# Save dimension and fact CSVs
dim_date.to_csv(BASE / "dw_dim_date.csv", index=False)
dim_customer.to_csv(BASE / "dw_dim_customer.csv", index=False)
dim_product.to_csv(BASE / "dw_dim_product.csv", index=False)
dim_store.to_csv(BASE / "dw_dim_store.csv", index=False)
fact_sales.to_csv(BASE / "dw_fact_sales.csv", index=False)

# Create SQLite DB and load tables
db_path = BASE / "data_warehouse.db"
conn = sqlite3.connect(db_path)
dim_date.to_sql("dim_date", conn, if_exists="replace", index=False)
dim_customer.to_sql("dim_customer", conn, if_exists="replace", index=False)
dim_product.to_sql("dim_product", conn, if_exists="replace", index=False)
dim_store.to_sql("dim_store", conn, if_exists="replace", index=False)
fact_sales.to_sql("fact_sales", conn, if_exists="replace", index=False)
conn.close()

print("ETL completed. Files created:")
print(" - dw_dim_date.csv, dw_dim_customer.csv, dw_dim_product.csv, dw_dim_store.csv, dw_fact_sales.csv")
print(" - data_warehouse.db (SQLite)")

