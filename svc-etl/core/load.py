"""
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-20
Module to load data by interfacing with the driver and sws_dw
"""

import core.data_access as da


def load_swapi_data():
    da.push_sws_dw_starship_film_raw()


def load_sws_data():
    da.push_sws_dw_sales_raw()
