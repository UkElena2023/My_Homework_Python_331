import json
from typing import List
from dataclasses import dataclass


class JsonFile:
    """
    Класс для работы с файлами Json (чтение, запись)
    """

    def __init__(self, file_name):
        """
        Инициализация объектов класса
        """
        self.file_name = file_name

    def read_data(self):
        """
        Чтение данных из JSON файла
        :return: данные из JSON файла
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


class Cities:
    """
    Класс используется для представления данных о городах из Json-файла
    """

    def __init__(self, city_data: List):
        """
        Метод для инициализации состояния объекта
        :param city_data: список городов
        """
        self.city_data = city_data
        self.names_list = self.__get_names_list()

    def __get_names_list(self):
        """
        Метод для получения списка экземпляров класса City
        из списка словарей с данными о городах
        :return: список экземпляров класса City
        """
        # list comprehension для получение списка экземпляров класса City
        names_list = [
            City(
                name=city['name'].lower().replace("ё", 'е'),
                population=city['population'],
                subject=city['subject'],
                district=city['district'],
                latitude=float(city['coords']['lat']),
                longitude=float(city['coords']['lon'])
            )
            for city in self.city_data]
        return names_list


class CityGame:
    """
    Класс управляющий игрой. Принимает экземпляр класса из класса Cities в качестве аргумента
    """

    def __init__(self, cities: Cities):
        self.cities_obj = cities
        self.cities: List[City] = self.cities_obj.names_list
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
    Класс принимает аргументы из классов JsonFile, Cities, CityGame в качестве аргументов
    """

    def __init__(self, json_file: JsonFile, cities: Cities, game: CityGame):
        self.json_file = json_file
        self.cities = cities
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
    json_file = JsonFile("cities.json")
    # Создаем экземпляр класса Cities
    cities = Cities(json_file.read_data())
    # Создаем экземпляр класса CityGame
    game = CityGame(cities)
    # Создаем экземпляр класса GameManager
    game_manager = GameManager(json_file, cities, game)
    # Запускаем игру
    game_manager()
