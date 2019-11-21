""" 
Author: Rafael Battesti - rafaelbattesti.com
Since: 2019-11-20
Module to declare the domain objects utilized in the etl service
"""

from collections import namedtuple

StarshipFilm = namedtuple(
    "StarshipFilm", ["film_title", "film_release_date", "starship_name"]
)
