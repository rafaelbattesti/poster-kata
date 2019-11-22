"""
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-20
Module to provide data access, from and to external or internal persistence(i.e. csv for loading)
"""

import csv
import os

import swapi

import psycopg2 as pg

# DBs
# TODO: Investigate docker-compose .env
PG_HOST = os.getenv("POSTGRES_HOST", "svc-postgres")
PG_USER = os.getenv("POSTGRES_USER", "postgres")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "YqEa3$R8wpUJVJJc")
PG_BASE_CONNECTION_STRING = "postgresql://{}:{}@{}/{}"

# SWS
SWS_DB = "sws"
SWS_CONNECTION_STRING = PG_BASE_CONNECTION_STRING.format(
    PG_USER, PG_PASS, PG_HOST, SWS_DB
)
SWS_DIM_CUSTOMER_TGT = "ordering.dim_customer"
SWS_DIM_PRODUCT_TGT = "ordering.dim_product"
SWS_DIM_PROMO_TGT = "ordering.dim_promo_code"
SWS_FACT_SALES_ORDER_TGT = "ordering.fact_sales_order"
SWS_FACT_SALES_ORDER_ITEM_TGT = "ordering.fact_sales_order_item"

# CSV
SWS_DIM_CUSTOMER_CSV = "dim_customer.csv"
SWS_DIM_PRODUCT_CSV = "dim_product.csv"
SWS_DIM_PROMO_CODE_CSV = "dim_promo_code.csv"
SWS_FACT_SALES_ORDER_CSV = "fact_sales_order.csv"
SWS_FACT_SALES_ORDER_ITEM_CSV = "fact_sales_order_item.csv"


def get_sws_conn():
    """ Get a psycopg2 connection to sws """
    return pg.connect(SWS_CONNECTION_STRING)


def source_swapi_starship_raw():
    """ Fetch raw starship data """
    return swapi.get_all("starships")


def save_csv(df, csv_file):
    df.to_csv(
        csv_file, index=True, header=False, quoting=csv.QUOTE_MINIMAL, sep=",",
    )


def save_dim_customer_csv(df_dim_customer):
    save_csv(df_dim_customer, SWS_DIM_CUSTOMER_CSV)


def save_dim_product_csv(df_dim_product):
    save_csv(df_dim_product, SWS_DIM_PRODUCT_CSV)


def save_dim_promo_code_csv(df_dim_promo_code):
    save_csv(df_dim_promo_code, SWS_DIM_PROMO_CODE_CSV)


def save_fact_sales_order_csv(df_fact_sales_order):
    save_csv(df_fact_sales_order, SWS_FACT_SALES_ORDER_CSV)


def save_fact_sales_order_item_csv(df_fact_sales_order_item):
    save_csv(df_fact_sales_order_item, SWS_FACT_SALES_ORDER_ITEM_CSV)


def push_sws_table(csv, table):
    conn = get_sws_conn()
    cursor = conn.cursor()
    sql = """COPY {} FROM STDIN WITH CSV DELIMITER AS ','"""
    with open(csv) as f:
        cursor.copy_expert(
            sql=sql.format(table), file=f,
        )
    conn.commit()


def push_sws_dim_customer():
    push_sws_table(SWS_DIM_CUSTOMER_CSV, SWS_DIM_CUSTOMER_TGT)


def push_sws_dim_product():
    push_sws_table(SWS_DIM_PRODUCT_CSV, SWS_DIM_PRODUCT_TGT)


def push_sws_dim_promo_code():
    push_sws_table(SWS_DIM_PROMO_CODE_CSV, SWS_DIM_PROMO_TGT)


def push_sws_fact_sales_order():
    push_sws_table(SWS_FACT_SALES_ORDER_CSV, SWS_FACT_SALES_ORDER_TGT)


def push_sws_fact_sales_order_item():
    push_sws_table(SWS_FACT_SALES_ORDER_ITEM_CSV, SWS_FACT_SALES_ORDER_ITEM_TGT)
