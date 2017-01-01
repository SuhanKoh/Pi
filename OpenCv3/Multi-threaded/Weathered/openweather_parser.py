from .forecast.forecast import Forecast

class OpenWeatherParser:

    def __init__(self, data):
        self.data = data

    def get_weather_list(self):
        return self.data["list"]

    def get_forecast(self):
        forecasts = []
        for forecast_data in self.get_weather_list():
            forecasts.append(Forecast(forecast_data))
        return forecasts
