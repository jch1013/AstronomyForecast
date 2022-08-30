import bs4
from datetime import date
from urllib.request import Request, urlopen

def request_page(link):
    page_request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(page_request).read()
    html_content = bs4.BeautifulSoup(webpage, "html.parser")
    return html_content




def get_data(html):
    print('getting data')







def get_moon(zipcode, today):
    link =f'https://www.almanac.com/astronomy/moon-rise-and-set/zipcode/{zipcode}/{today}'
    moon_html = request_page(link)
    moon_data = get_data(moon_html)
    return moon_data
