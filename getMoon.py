import bs4
from urllib.request import Request, urlopen

def request_page(link):
    page_request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(page_request).read()
    html_content = bs4.BeautifulSoup(webpage, "html.parser")
    return html_content




def get_data(html):
    data = html.select(".rise_highlight")
    all_moon_data = data[0].findAll(lambda tag: tag.name == 'td')
    rise = all_moon_data[0].text
    apex = all_moon_data[1].text
    sets = all_moon_data[3].text
    moon_array = [rise, apex, sets]
    return moon_array


def get_moon(zipcode, today):
    link =f'https://www.almanac.com/astronomy/moon-rise-and-set/zipcode/{zipcode}/{today}'
    moon_html = request_page(link)
    moon_array = get_data(moon_html)
    return moon_array