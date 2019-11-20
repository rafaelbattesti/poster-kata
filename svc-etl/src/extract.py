import swapi


def get_films():
    return swapi.get_all("films")


def get_starships():
    return swapi.get_all("starships")


def get_characters():
    return swapi.get_all("people")


def get_planets():
    return swapi.get_all("planets")
