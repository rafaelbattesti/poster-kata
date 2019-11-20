/*
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-19
Requirements: 
    - ordering.dim_customer
    - ordering.dim_product
    - ordering.dim_promo_code
    - ordering.fact_sales_order
    - ordering.fact_sales_order_item
*/
CREATE SCHEMA ordering

    CREATE TABLE dim_customer
    (
        int_customer_id INT GENERATED ALWAYS AS IDENTITY,
        txt_customer_name TEXT NOT NULL,
        txt_customer_address TEXT,
        txt_customer_city TEXT,
        dt_customer_dob DATE
    )

    CREATE TABLE dim_product
    (
        int_product_id INT GENERATED ALWAYS AS IDENTITY,
        txt_product_content TEXT NOT NULL,
        num_product_price NUMERIC
    )

    CREATE TABLE dim_promo_code
    (
        txt_promo_code_id TEXT PRIMARY KEY,
        int_promo_code_discount INT NOT NULL
    )

    CREATE TABLE fact_sales_order
    (
        int_sales_order_id INT GENERATED ALWAYS AS IDENTITY,
        int_customer_id INT NOT NULL,
        ts_sales_order_created TIMESTAMP NOT NULL,
        ts_sales_order_updated TIMESTAMP,
        ts_sales_order_fulfilled TIMESTAMP
    )

    CREATE TABLE fact_sales_order_item
    (
        int_sales_order_item_id INT GENERATED ALWAYS AS IDENTITY,
        int_sales_order_id INT NOT NULL,
        int_product_id INT NOT NULL,
        int_sales_order_item_qty INT NOT NULL
    )
;