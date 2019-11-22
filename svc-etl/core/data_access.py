"""
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-20
Module to provide data access, from and to external or internal persistence(i.e. csv for loading)
"""

import csv
import os

import pandas as pd
import pandas.io.sql as sqlio
import swapi

import psycopg2 as pg
from core.domain import StarshipFilm

# DBs
# TODO: Investigate docker-compose .env
PG_HOST = os.getenv("POSTGRES_HOST", "svc-postgres")
PG_USER = os.getenv("POSTGRES_USER", "postgres")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "YqEa3$R8wpUJVJJc")
PG_BASE_CONNECTION_STRING = "postgresql://{}:{}@{}/{}"

# SWS_DW
SWS_DW_DB = "sws_dw"
SWS_DW_CONNECTION_STRING = PG_BASE_CONNECTION_STRING.format(
    PG_USER, PG_PASS, PG_HOST, SWS_DW_DB
)

# SWS
SWS_DB = "sws"
SWS_CONNECTION_STRING = PG_BASE_CONNECTION_STRING.format(
    PG_USER, PG_PASS, PG_HOST, SWS_DB
)
SWS_SALES_SRC = "ordering.v_sales"
SWS_SALES_CSV = "sws_sales.csv"
SWS_SALES_TGT = "lz.sws_sales"

# SWAPI
SWAPI_STARSHIP_FILM_CSV = "swapi_starship_film.csv"
SWAPI_STARSHIP_FILM_TGT = "lz.swapi_starship_film"


def get_sws_dw_conn():
    """ Get a psycopg2 connection to sws_dw """
    return pg.connect(SWS_DW_CONNECTION_STRING)


def get_sws_conn():
    """ Get a psycopg2 connection to sws """
    return pg.connect(SWS_CONNECTION_STRING)


def source_swapi_starship_raw():
    """ Fetch raw starship data """
    return swapi.get_all("starships")


def source_swapi_film_raw():
    """ Fetch raw films data """
    return swapi.get_all("films")


def source_swapi_starship_film_df():
    """ Join films and starships  """
    data = []
    for film in source_swapi_film_raw().items:
        for starship in film.get_starships().items:
            obj = StarshipFilm(film.title, film.release_date, starship.name)
            data.append(obj)
    return pd.DataFrame(data)


def source_sws_sales_df():
    """ Fetch sales data from ordering system """
    sql = "SELECT * FROM {};".format(SWS_SALES_SRC)
    conn = get_sws_conn()
    return sqlio.read_sql_query(sql, conn)


def save_csv(df, csv_file):
    df.to_csv(
        csv_file, index=False, header=False, quoting=csv.QUOTE_NONNUMERIC, sep=",",
    )


def save_swapi_starship_film_csv(df_starship_film):
    save_csv(df_starship_film, SWAPI_STARSHIP_FILM_CSV)


def save_sws_sales_csv(df_sales):
    save_csv(df_sales, SWS_SALES_CSV)


def push_table(conn, csv, table):
    cursor = conn.cursor()
    sql = """COPY {} FROM STDIN WITH CSV DELIMITER AS ','"""
    with open(csv) as f:
        cursor.copy_expert(
            sql=sql.format(table), file=f,
        )
    conn.commit()


def push_sws_dw_sales_raw():
    push_table(get_sws_dw_conn(), SWS_SALES_CSV, SWS_SALES_TGT)


def push_sws_dw_starship_film_raw():
    push_table(get_sws_dw_conn(), SWAPI_STARSHIP_FILM_CSV, SWAPI_STARSHIP_FILM_TGT)
