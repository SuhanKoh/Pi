import requests
from .openweather_parser import OpenWeatherParser
from pprint import pprint
from datetime import datetime

APPID = "" # App/api key from Open weather
CITYID = "" # City id from Open weather


def get_weather():
    url = "http://api.openweathermap.org/data/2.5/forecast?id=" + CITYID + "&APPID=" + APPID
    r = requests.get(url)

    active_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if r.status_code == requests.codes.ok:
        data = r.json()
        parser = OpenWeatherParser(data)
        forecasts = parser.get_forecast()

        if len(forecasts) > 6:
            range_index = 5
        else:
            range_index = len(forecasts)

        for i in range(0, range_index):
            pprint("*****   " + forecasts[i].get_datetime_parsed() + "  *****")
            pprint("        " + forecasts[i].get_weather_main() + "    -    " + forecasts[i].get_weather_description())
            print("\n")

        pprint("Last updated were at: " + active_time)

    else:

        pprint("Unable to fetch data - " + active_time)
