import bs4
from urllib.request import Request, urlopen
import planet


#requests HTML content from original webpage
#returns cleaned HTML content
def request_page(link):
    page_request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(page_request).read()
    html_content = bs4.BeautifulSoup(webpage, "html.parser")
    return html_content

#collects data from HTML and creates planet objects
#returns list of planet objects
def get_data(html):
    planets = []
    all_planets = html.select(".rise_highlight")
    for obj in all_planets:
        name = obj.find(lambda tag: tag.name == 'th').text
        data = obj.findAll(lambda tag: tag.name == 'td')
        rise = data[0].text
        apex = data[1].text
        sets = data[3].text
        new_planet = planet.Planet(name, rise, sets, apex)
        planets.append(new_planet)
    return planets


#can accept zipcode input from main and calls all functions
#returns list of all planet objects
def get_planets(zipcode, today):
    link = f'https://www.almanac.com/astronomy/planets-rise-and-set/zipcode/{zipcode}/{today}'
    planet_html = request_page(link)
    all = get_data(planet_html)
    return all





