import bs4
from datetime import date
from urllib.request import Request, urlopen
import planet

today = date.today().strftime("%Y-%m-%d")
zip = 61820

link = f'https://www.almanac.com/astronomy/planets-rise-and-set/zipcode/{zip}/{today}'

def request_page(link):
    page_request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(page_request).read()
    html_content = bs4.BeautifulSoup(webpage, "html.parser")
    return html_content

def get_data(html):
    planets = []
    all_objects = html.select(".rise_highlight")
    for object in all_objects:
        name = object.find(lambda tag: tag.name == 'th').text
        data = object.findAll(lambda tag: tag.name == 'td')
        rise = data[0].text
        apex = data[1].text
        set = data[3].text
        new_planet = planet.Planet(name, rise, set, apex)
        planets.append(new_planet)
    return planets

planet_html = request_page(link)
all = get_data(planet_html)
