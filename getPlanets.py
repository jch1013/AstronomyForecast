import planet


# collects data from HTML and creates planet objects
# returns list of planet objects
def get_planets(html):
    planets = []
    all_planet_html = html.select(".lightgreybox")[1]
    all_planets = all_planet_html.findAll(lambda tag: tag.name == 'tr')
    for p in all_planets[2:]:
        planet_data = []
        for val in p:
            planet_data.append(val.text)
        new_planet = planet.Planet(planet_data[0], planet_data[1], planet_data[3], planet_data[2])
        planets.append(new_planet)
    return planets



