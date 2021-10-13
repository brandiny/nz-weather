from django.forms.fields import JSONField, JSONString
import requests
import pprint
from datetime import datetime

# Returns weather data by city (NZ only) in JSON format
# https://openweathermap.org/current#current_JSON - data format
def get_weather_data(city_name: str) -> JSONString:
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name + ", NZ",
        "appid": "30120c6d1ef133cea90f0a78c287c9ec",
        "units": "metric"
    }

    try:
        response = requests.get(url, params)
        response.raise_for_status()
        pprint.pprint(response.json())
        return response.json()
    except Exception as error:
        return None


# Given an integer UTC timestamp, returns date time string
# e.g 1634115646 --> Oct 13, 10.00pm
def utc_to_datestring(utc_int: int) -> str:
    MONTH_STRINGS = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    obj = datetime.fromtimestamp(utc_int)
    month_int = int(obj.strftime("%m"))
    month = MONTH_STRINGS[month_int]
    day = obj.strftime("%d")
    hour = str(int(obj.strftime("%H")) + 13)
    minute = obj.strftime("%M")
    period = "pm" if int(hour) >= 12 else "am"

    return "{} {}, {}:{} {}".format(
        day, month, str(int(hour) % 12), minute, period
    )

    
