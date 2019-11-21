"""
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-20
Module to extract data by interfacing with the driver and the data sources
"""

import core.data_access as da


def extract_swapi_data():
    df = da.source_swapi_starship_film_df()
    da.save_swapi_starship_film_csv(df)


def extract_sws_data():
    df = da.source_sws_sales_df()
    da.save_sws_sales_csv(df)
