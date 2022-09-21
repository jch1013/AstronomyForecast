from timezonefinder import TimezoneFinder
from datetime import date, datetime
from pytz import timezone, utc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4

import getMoon
import getPlanets
import getWeather
import getDSO


def make_link(coordinates, time_zone):
    lat = coordinates[0]
    long = coordinates[1]
    year = date.today().strftime("%Y")
    month = int(date.today().strftime("%m"))
    day = int(date.today().strftime("%d"))
    return f'https://in-the-sky.org/whatsup_times.php?year={year}&month={month}&day={day}&latitude={lat}&longitude={long}&timezone={time_zone}'


def get_timezone(lat, lng):
    now = datetime.now()
    tf = TimezoneFinder()
    tz_target = timezone(tf.certain_timezone_at(lng=lng, lat=lat))
    # ATTENTION: tz_target could be None! handle error case
    today_target = tz_target.localize(now)
    today_utc = utc.localize(now)
    return (today_utc - today_target).total_seconds() / 3600


# This function uses selenium to get the page containing important object rise times after the entire page is loaded
# the complete page HTML is passed to several scripts in order to find relevant information.
def request_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "lightgreybox"))
        )
    finally:
        pass
    html = driver.page_source
    html_content = bs4.BeautifulSoup(html, "html.parser")
    return html_content


# This function makes calls to all scripts that gather data, and assembles the information into a printable report
def make_report(lat, lng):
    # if Google Maps api cannot find the location, return an error message
    if lat == 0 and lng == 0:
        return error_message
    report_body = "-----General Information-----\n"
    time_zone = get_timezone(lat, lng)
    link = make_link([lat, lng], time_zone)

    # Add weather data to report
    weather = getWeather.get_forecast(lat, lng)
    report_body += weather + '\n'

    # Information on planets, moon, deep sky objects
    all_html = request_page(link)

    # Add moon information to report
    moon_report = getMoon.get_moon(all_html)
    report_body += moon_report

    # Add planet information to report
    planets = getPlanets.get_planets(all_html)
    report_body += planets

    # Add deep sky object information to report
    dso_report = getDSO.dso_report(all_html)
    report_body += dso_report

    return report_body


error_message = ("**Error: Invalid location. Please retry with a valid location**\n\nTo use this service, simply send "
                 "an email to <astroforecasttonight@gmail.com> with the desired location in the subject line. This "
                 "program will accept an address, a zipcode, the name of a city or coordinates as valid locations. A "
                 "reply email will be sent with important information for seeing conditions at night. A template "
                 "email is shown below:\n\nTo: astroforecasttonight@gmail.com\nFrom: <your_email>\nSubject: Los "
                 "Angeles\n Body: (leave this blank)\n\nNOTE: This program only works for locations within the United "
                 "States, and data provided for international locations may be either incorrect or missing.")