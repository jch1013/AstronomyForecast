import requests


def lat_long(location):
    lat, lng = 0, 0
    api_key = 'AIzaSyB12rdUGHEz8sqBtLZYwy4y_HukouNJcFE'
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={location}&key={api_key}"
    r = requests.get(endpoint)

    # make sure request is successful
    if r.status_code not in range(200, 299):
        return 0, 0
    try:
        '''
        This try block incase any of our inputs are invalid. This is done instead
        of actually writing out handlers for all kinds of responses.
        '''
        results = r.json()['results'][0]
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    return lat, lng
