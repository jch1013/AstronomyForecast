import bs4
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import planet


# requests HTML content from original webpage
# returns cleaned HTML content

def request_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "lightgreybox"))
        )
    finally:
        # driver.quit()
        pass
    html = driver.page_source
    html_content = bs4.BeautifulSoup(html, "html.parser")
    return html_content


# collects data from HTML and creates planet objects
# returns list of planet objects
def get_data(html):
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


# can accept zipcode input from main and calls all functions
# returns list of all planet objects
def get_planets(coordinates, today, timezone):
    link = make_link(coordinates, today, timezone)
    planet_html = request_page(link)
    all_planets = get_data(planet_html)
    return all_planets


def make_link(coordinates, today, timezone):
    lat = coordinates[0]
    long = coordinates[1]
    year = today[0]
    month = today[1]
    day = today[2]
    return f'https://in-the-sky.org/whatsup_times.php?year={year}&month={month}&day={day}&latitude={lat}&longitude={long}&timezone={timezone}'


