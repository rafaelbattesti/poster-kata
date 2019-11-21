/*
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-19
Requirements: 
    - lz.swapi_starship_film
    - lz.sws_sales
    - sz.dim_film
    - sz.dim_starship
    - sz.dim_customer
    - sz.dim_product
    - sz.dim_promo_code
    - cz.v_spaceship
    - cz.v_customer
    - cz.v_product
    - cz.v_promo_code
*/
CREATE SCHEMA lz
    
    CREATE TABLE swapi_starship_film
    (
        txt_film_title TEXT,
        txt_film_release_date TEXT,
        txt_starship_name TEXT
    )

    CREATE TABLE sws_sales
    (
        txt_customer_dob TEXT,
        txt_customer_city TEXT,
        txt_customer_address TEXT,
        txt_customer_country_iso TEXT,
        txt_product_content TEXT,
        txt_product_qty TEXT,
        txt_product_price TEXT,
        txt_sales_rep TEXT,
        txt_promo_code TEXT
    )
;

CREATE SCHEMA sz

    CREATE TABLE dim_film
    (
        int_film_id INT GENERATED ALWAYS AS IDENTITY,
        txt_film_name TEXT,
        dt_film_release_date DATE,
        ts_created TIMESTAMP,
        ts_updated TIMESTAMP
    )

    CREATE TABLE dim_starship
    (
        int_starship_id INT GENERATED ALWAYS AS IDENTITY,
        txt_starship_name TEXT,
        ts_created TIMESTAMP,
        ts_updated TIMESTAMP
    )

    CREATE TABLE dim_customer
    (
        int_customer_id INT GENERATED ALWAYS AS IDENTITY,
        int_customer_id_source INT,
        dt_customer_dob DATE,
        txt_customer_city TEXT,
        txt_customer_address TEXT,
        txt_customer_country_iso TEXT,
        ts_created TIMESTAMP,
        ts_updated TIMESTAMP
    )

    CREATE TABLE dim_product
    (
        int_product_id INT GENERATED ALWAYS AS IDENTITY,
        int_product_id_source INT,
        txt_product_content TEXT,
        int_product_qty INT,
        num_product_price NUMERIC,
        ts_created TIMESTAMP,
        ts_updated TIMESTAMP
    )

    CREATE TABLE dim_promo_code
    (
        int_promo_code_id INT GENERATED ALWAYS AS IDENTITY,
        txt_promo_code_id_source TEXT,
        ts_created TIMESTAMP,
        ts_updated TIMESTAMP
    )
;

CREATE SCHEMA cz

    CREATE VIEW v_film AS
        SELECT * FROM sz.dim_film

    CREATE VIEW v_starship AS
        SELECT * FROM sz.dim_starship

    CREATE VIEW v_customer AS
        SELECT * FROM sz.dim_customer

    CREATE VIEW v_product AS
        SELECT * FROM sz.dim_product

    CREATE VIEW v_promo_code AS
        SELECT * FROM sz.dim_promo_code
;