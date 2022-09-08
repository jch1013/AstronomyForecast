"""
This code uses the requests library to retrieve the weather forecast page for the nighttime weather at the given
coordinates and the Beautiful Soup library to process and extract the data. Data is pulled from weather.gov.
"""

import bs4
import requests


def get_forecast(lat, lng):
    link = f'https://forecast.weather.gov/MapClick.php?lon={lng}&lat={lat}'
    page = requests.get(link)
    html = bs4.BeautifulSoup(page.text, "html.parser")
    forecast = html.select('.col-sm-10.forecast-text')[1].text
    return forecast
