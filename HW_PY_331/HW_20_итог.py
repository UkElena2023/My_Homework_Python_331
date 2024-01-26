import json

from typing import List
from dataclasses import dataclass
from jsonschema import validate, ValidationError


# JSON-схема для данных о городах
json_schema = {
    "type": "object",
    "properties": {
        "coords": {
            "type": "object",
            "properties": {
                "lat": {"type": "string"},
                "lon": {"type": "string"}
            },
            "required": ["lat", "lon"]
        },
        "district": {"type": "string"},
        "name": {"type": "string"},
        "population": {"type": "integer"},
        "subject": {"type": "string"}
    },
    "required": ["coords", "district", "name", "population", "subject"]
}


class Validator:
    """
    Класс для проверки соответствия данных о городах заданной JSON-схеме.
    Внедряется в класс JsonFile через композицию.
    Проверяет данные на основе JSON-схеме перед чтением
    """

    def __init__(self, schema=None):
        """
        Инициализация объектов класса
        :param schema: схема для данных о городах в формате Json
        """
        if schema is None:
            schema = json_schema
        self.schema = schema

    def validate(self, data):
        """
        Метод для валидации данных
        :param data: данные для валидации
        :return: True, если данные валидны, иначе False
        """
        try:
            validate(data, self.schema)
        except ValidationError:
            print(f'Ошибка валидации!\nВ список городов не попали данные о городе: {data}')
            return False
        return True


class JsonFile:
    """
    Класс для работы с файлами Json (чтение, запись)
    """

    def __init__(self, file_name, schema):
        """
        Инициализация объектов класса
        """
        self.file_name = file_name
        self.validator = Validator(schema)

    def __validate_single_city(self, city: dict) -> bool:
        """
        Метод для валидации данных о городе
        :param city: данные об одном городе в виде словаря
        :return: True, если данные валидны, иначе False
        """
        return self.validator.validate(city)

    def get_all_cities(self) -> list:
        """
        Метод, который читает все города из файла и проверяет каждый город на валидность.
        Возвращает список всех валидных городов
        :return: список всех валидных городов
        """
        cities = self.__read_data()
        # создание списка валидных городов через LIST-comprehension
        valid_cities = [city for city in cities if self.__validate_single_city(city)]
        return valid_cities

    def __read_data(self):
        """
        Чтение данных из JSON файла
        :return: прочитанные данные из JSON-файла
        """
        with open(self.file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data

    def write_data(self, data):
        """
        Метод записи данных в файл Json
        :param data: данные для записи
        :return: None
        """
        with open(self.file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)


@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False

    # метод проверки на вхождение в класс City
    def __eq__(self, other):
        if isinstance(other, City):
            return self.name == other.name
        return False


class Serializer:
    """
    Класс для преобразования данных о городах между форматами
    """

    def __init__(self, city_data: list):
        """
        Метод для инициализации состояния объекта
        """
        self.city_data = city_data

    def __call__(self) -> List[City]:
        """
        Метод для запуска десериализации
        :return: список экземпляров класса City
        """
        return self.deserialize()

    def deserialize(self) -> List[City]:
        """
        Метод для десериализации данных из Json файла в данные для класса City
        :return: список словарей с данными о городах
        """
        # создание списка словарей через LIST-comprehension
        cities = [
            City(
                name=city['name'].lower().replace("ё", 'е'),
                population=city['population'],
                subject=city['subject'],
                district=city['district'],
                latitude=float(city['coords']['lat']),
                longitude=float(city['coords']['lon'])
            )
            for city in self.city_data]
        return cities


class CityGame:
    """
    Класс управляющий игрой
    """

    def __init__(self, cities: List[City]):
        self.cities = cities
        self.human_city: City | None = None
        self.computer_city: City | None = None

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:
        """
        Метод проверки правил игры.
        Возвращает True если правила соблюдены, иначе False
        :param last_city: последний названый город
        :param new_city: новый город
        :return:
        """

        # проверка правильного названия города по условиям игры (без ы, ь, й)
        if last_city[-1] == 'ы' and new_city[0] != last_city[-2]:
            return False
        elif last_city[-1] == 'ь' and new_city[0] != last_city[-2]:
            return False
        elif last_city[-1] == 'й' and new_city[0] != last_city[-2]:
            return False
        elif new_city[0] != last_city[-1] and last_city[-1] != 'ы' and last_city[-1] != 'ь' and last_city[-1] != 'й':
            return False
        else:
            return True

    def human_step(self):
        """
        Метод для хода человека
        :return:
        """
        # очистка ввода: будет приниматься равенство ё=е, в нижнем регистре тоже не будет выдавать ошибку
        self.human_city = input('Введите город: ').lower().replace("ё", 'е').strip()
        if self.human_city == 'стоп':
            print('Вы проиграли, компьютер оказался умнее!')
            return False

        for city in self.cities:
            if city.name == self.human_city:
                if city.is_used:
                    print(f'Город {self.human_city} уже был использован. Вы проиграли')
                    return False
                # убираем Йошкар-олу из списка
                elif city.name == 'йошкар-ола':
                    print(f'Город {self.human_city} нельзя использовать по условиям игры. Вы проиграли')
                    return False
                else:
                    self.human_city = city
                    break
        else:
            print(f'Города {self.human_city} нет в списке. Вы проиграли')
            return False

        if self.computer_city:
            if not self.check_game_rules(self.computer_city.name, self.human_city.name):
                print(f'Вы проиграли. Ваш ответ начинается на неверную букву')
                return False

        # флаг на элемент класса City, что он назван в игре вместо удаления из списка
        self.human_city.is_used = True
        return True

    def computer_step(self):
        """
        Метод для хода компьютера
        :return:
        """
        for city in self.cities:
            # Проверка правил игры методом из класса CityGame
            if self.check_game_rules(self.human_city.name, city.name):
                if city.is_used:
                    continue
                print(f'Компьютер называет город: {city.name.capitalize()}')
                self.computer_city = city
                city.is_used = True
                return True

        else:
            print('Вы победили! Компьютер не смог назвать город')
            return False


class GameManager:
    """
    Класс принимает аргументы из классов JsonFile, CityGame в качестве аргументов
    """

    def __init__(self, json_file: JsonFile, game: CityGame):
        self.json_file = json_file
        # self.cities = cities
        self.game = game

    def __start_game(self):
        """
        Метод для начала игры
        :return:
        """
        # цикл игры
        while True:
            if not self.game.human_step():
                break
            if not self.game.computer_step():
                break

    def __call__(self):
        """
        Метод для начала игры
        (позволяет вызывать объекты этого класса, как если бы они были функциями и который будет запускать игру)
        :return:
        """
        self.__start_game()
        print('Игра окончена')
        input('Нажмите Enter для выхода')


# ================Начало игры====================
print('ИГРА В ГОРОДА РОССИИ\n'
      'Правила:\n'
      '1. Название города в России должно начинаться на последнюю букву города, выданного компьютером.\n'
      '2. Название города "Йошкар-ола" использовать нельзя, он исключен для использования для более интересной игры.\n'
      '3. Если название города заканчивается на "ь", "ы" или "й" Вы можете ввести город с предпоследней буквы '
      '(компьютер сделает также).\n'
      '4. Повторять города нельзя.\n')

if __name__ == "__main__":

    # Создаем экземпляр класса JsonFile
    json_file = JsonFile("cities.json", json_schema)

    # создание экземпляра класса JsonFile для проверки по json-файлу c битыми данными
    # json_file = JsonFile("cities_invalid.json", json_schema)

    # получения списка валидных городов
    cities_data = json_file.get_all_cities()

    # Создаем экземпляр класса Serializer
    serializer = Serializer(cities_data)
    cities = serializer()

    # Создаем экземпляр класса CityGame
    game = CityGame(cities)

    # Создаем экземпляр класса GameManager
    game_manager = GameManager(json_file, game)
    
    # Запускаем игру
    game_manager()
