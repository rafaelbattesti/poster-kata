import swapi

def get_films():
    return swapi.get_all("films")

def get_starships():
    return swapi.get_all("starships")

def get_characters():
    return swapi.get_all("people")

def get_planets():
    return swapi.get_all("planets")

f = get_films()
s = get_starships()
c = get_characters()
p = get_planets()

for film in f.items:
    print(film.title)

for starship in s.items:
    print(starship.name)

for character in c.items:
    print(character.name)

for planet in p.items:
    print(planet.name)