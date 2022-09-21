"""
This code uses the requests library to retrieve the weather forecast page for the nighttime weather at the given
coordinates and the Beautiful Soup library to process and extract the data. Data is pulled from weather.gov.
"""

import bs4
import requests


# This function returns the forecast at a given location for tonight
def get_forecast(lat, lng):
    link = f'https://forecast.weather.gov/MapClick.php?lon={lng}&lat={lat}'
    print(link)
    page = requests.get(link)
    html = bs4.BeautifulSoup(page.text, "html.parser")

    try:
        daytime = (html.select('.col-sm-2.forecast-label')[0].text != "Tonight")
    except:
        return "Unable to provide weather data at this time. Please try again later"

    if daytime:
        forecast = html.select('.col-sm-10.forecast-text')[1].text
    else:
        forecast = html.select('.col-sm-10.forecast-text')[0].text
    return forecast
