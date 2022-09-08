from timezonefinder import TimezoneFinder
from datetime import date, datetime
from pytz import timezone, utc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
import getPlanets


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


def make_report(lat, lng):
    report_body = ""
    time_zone = get_timezone(lat, lng)
    link = make_link([lat, lng], time_zone)
    all_html = request_page(link)
    planets = getPlanets.get_planets(all_html)
    for p in planets:
        report_body += str(p)
        report_body += "\n----------\n"
    return report_body

