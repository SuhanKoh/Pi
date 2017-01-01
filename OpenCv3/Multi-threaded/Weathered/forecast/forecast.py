class Forecast:

    def __init__(self, forecast_list):
        self.data = forecast_list
        self.__parse()

    def get_datetime_parsed(self):
        return self.datetime_parsed

    def get_temp(self):
        return self.temp

    def get_temp_min(self):
        return self.temp_min

    def get_temp_max(self):
        return self.temp_max

    def get_pressure(self):
        return self.pressure

    def get_weather_main(self):
        return self.main

    def get_weather_description(self):
        return self.description

    def __main(self):
        return self.data["main"]

    def __weather(self):
        # Get the first element
        return (self.data["weather"])[0]

    def __wind(self):
        return self.data["wind"]

    def __parse(self):
        self.datetime = self.data["dt"]
        self.datetime_parsed = self.data["dt_txt"]
        self.temp = self.__main()["temp"]
        self.temp_min = self.__main()["temp_min"]
        self.temp_max = self.__main()["temp_max"]
        self.pressure = self.__main()["pressure"]
        self.sea_level = self.__main()["sea_level"]
        self.grnd_level = self.__main()["grnd_level"]
        self.humidity = self.__main()["humidity"]
        self.temp_kf = self.__main()["temp_kf"]
        self.id = self.__weather()["id"]
        self.main = self.__weather()["main"]
        self.description = self.__weather()["description"]
        self.icon = self.__weather()["icon"]
        self.wind_speed = self.__wind()["speed"]
        self.wind_degree = self.__wind()["deg"]
