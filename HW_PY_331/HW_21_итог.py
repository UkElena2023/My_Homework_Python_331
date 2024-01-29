import datetime
import requests
import json
from dataclasses import dataclass
from marshmallow import Schema, fields, validate, post_load, ValidationError, INCLUDE
from marshmallow_jsonschema import JSONSchema


def get_weather(city_name):
    api_key = "62194ea0e4a2186b244e444d26557139"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'lang': 'ru',
        'units': 'metric',
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    return response.json()


# образец для отрисовки схемы marshmallow по полям из ответа API
""" {
    'base': 'stations',
    'clouds': {'all': 100},
    'cod': 200,
    'coord': {'lat': 55.7522, 'lon': 37.6156},
    'dt': 1705238756,
    'id': 524901,
    'main': {'feels_like': -21.63,
             'grnd_level': 986,
             'humidity': 93,
             'pressure': 1005,
             'sea_level': 1005,
             'temp': -14.63,
             'temp_max': -14.23,
             'temp_min': -15.25},
    'name': 'Москва',
    'sys': {'country': 'RU',
            'id': 2000314,
            'sunrise': 1705211469,
            'sunset': 1705238701,
            'type': 2},
    'timezone': 10800,
    'visibility': 1616,
    'weather': [{'description': 'пасмурно',
                 'icon': '04n',
                 'id': 804,
                 'main': 'Clouds'}],
    'wind': {'deg': 167, 'gust': 11.16, 'speed': 4.35}
}
"""


# дата класс с полями из ответа API
@dataclass
class CurrentWeather:
    """
    Дата класс для создания/хранения информации о погоде в конкретном городе с полями из ответа API
    """
    city_name: str
    description: str
    temperature: float
    feels_like: float
    humidity: int
    pressure: int
    wind_speed: float

    def __str__(self):
        """
        Выводит информации о погоде в читаемом виде
        :return: str
        """
        return f'Погода в городе {self.city_name}:\n' \
               f'Температура: {self.temperature} °C, {self.description}\n' \
               f'Ощущается как: {self.feels_like} °C\n' \
               f'Влажность воздуха: {self.humidity} %\n' \
               f'Давление: {self.pressure} мм рт.ст.\n' \
               f'Скорость ветра: {self.wind_speed} м/с\n'


class CurrentWeatherSchema(Schema):
    """
    Класс для создания схемы marshmallow по ключам из json данных из API.
    Проходит валидация данных
    """
    city_name = fields.Str(data_key='name')
    description = fields.Str(data_key='weather.0.description')
    # самый холодный город Оймякон (Россия) -71.2, самый жаркий Деште-Лут (Иран) +70
    temperature = fields.Float(data_key='main.temp', validate=validate.Range(min=-72, max=71))
    feels_like = fields.Float(data_key='main.feels_like')
    humidity = fields.Integer(data_key='main.humidity', validate=validate.Range(max=100))
    pressure = fields.Integer(data_key='main.pressure')
    wind_speed = fields.Float(data_key='wind.speed')

    @post_load
    def make_current_weather(self, data, **kwargs):
        """
        Метод для десериализации данных после валидации данных
        :param data: данные о погоде в городе
        :param kwargs:
        :return: экземпляр датакласса CurrentWeather
        """
        return CurrentWeather(
            city_name=data['city_name'].capitalize(),
            description=data['weather'][0]['description'],
            temperature=round(data['main']['temp']),
            feels_like=round(data['main']['feels_like']),
            humidity=data['main']['humidity'],
            pressure=round(data['main']['pressure'] * 0.75006),
            wind_speed=round(data['wind']['speed'])
        )

    class Meta:
        """
        Параметр unknown указывает, что в ответе API могут быть и другие поля, которые не указаны в схеме.
        """
        unknown = INCLUDE


def main():
    user_city_name = input("Введите название города: ")
    # вывод на экран текущей даты в запрошенном городе
    current_date = datetime.datetime.now()
    print(current_date.strftime("%d.%m.%Y"))

    # получение данных о погоде из API
    weather_data = get_weather(user_city_name)

    # создание экземпляра класса CurrentWeatherSchema
    schema = CurrentWeatherSchema()

    # валидация
    current_weather = schema.load(weather_data)
    print(current_weather)

    # генерация JSON-схемы из Marshmallow-схемы
    json_chema_weather_in_city = JSONSchema().dump(schema)

    # запись JSON-схемы в json-файл
    with open('json_schema_result.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_chema_weather_in_city, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
