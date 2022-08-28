import bs4
import requests

lat = 47.606;
long = -122.332;

link = f'https://sky-tonight.com/?cat=Planet'


def getData(link):
    all_data = requests.get(link);
    html_content = bs4.BeautifulSoup(all_data.text, "lxml")
    all_objects = html_content.select(".object_card")[0]
    name = all_objects.select(".col-lg-12.col-sm-12.col-md-12.col-xs-12.text-center")[0].text
    #print(type(all_objects))
    print(name)



getData(link)
