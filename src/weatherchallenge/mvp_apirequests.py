import requests
import pprint
API_KEY = '30120c6d1ef133cea90f0a78c287c9ec'

query = 'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}&units=metric'.format(
    city_name='Wellington',
    key=API_KEY
)

# Gets weather data from Wellington
try:
    response = requests.get(query)
    response.raise_for_status()
    pprint.pprint(response.json())
except requests.exceptions.HTTPError as error:
    print(error)
