from pprint import pprint
from typing import Any, List, Dict
import csv
import json


class CsvFileHandler:
    """
    Класс для работы с файлами CSV
    """

    def __init__(self, filepath: str, delimiter: str = ';', encoding: str = 'windows-1251'):
        self.data = None
        self.filepath = filepath
        self.delimiter = delimiter
        self.encoding = encoding

    def read_file(self, as_dict: bool = False) -> List[List] | List[Dict]:
        """
        Метод чтения данных из CSV файла
        :param as_dict: флаг для работы с типами данных в файле
        (по умолчанию принимает List[List], при as_dict=True принимает List[Dict])
        :return: List[List] | List[Dict]
        """
        # with open(self.filepath, 'r', encoding=self.encoding, newline='') as file:
        with open(self.filepath, 'r', encoding=self.encoding) as file:
            self.data = file.readlines()
            if as_dict:
                return [dict(zip(self.data[0].split(self.delimiter), line.split(self.delimiter))) for line in
                        self.data[1:]]
            else:
                return [line.split(self.delimiter) for line in self.data]

    def write_file(self, data: List[Dict] | List[List], as_dict: bool = False) -> None:
        """
        Метод записи данных в файл CSV
        :param data: данные в виде List[Dict] | List[List]
        :param as_dict: флаг для работы с типами данных в файле
        (по умолчанию принимает List[List], при as_dict=True принимает List[Dict])
        :return: None
        """
        with open(self.filepath, 'w', encoding=self.encoding) as file:
            if as_dict:
                file.writelines([self.delimiter.join(data[0].keys()) + '\n'])
                for line in data:
                    file.writelines([self.delimiter.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([self.delimiter.join(line) + '\n'])

    def append_file(self, data: List[Dict] | List[List], as_dict: bool = False) -> None:
        """
        Метод дозаписи данных в файл CSV
        :param data: список списков или список словарей
        :param as_dict: флаг для работы с типами данных в файле
        (по умолчанию принимает List[List], при as_dict=True принимает List[Dict])
        :return: None
        """
        # with open(self.filepath, 'a', encoding=self.encoding, newline='') as file:
        with open(self.filepath, 'a', encoding=self.encoding, newline='') as file:
            if as_dict:
                for line in data:
                    file.writelines([self.delimiter.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([self.delimiter.join(line) + '\n'])


class JsonFileHandler:
    """
    Класс для работы с файлами Json (чтение, запись, при вызове метода дозаписи - выдаст ошибку на применение метода)
    """

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def read_file(self, as_dict: bool = False) -> List[List] | List[Dict]:
        """
        Метод чтения данных из Json файла
        :param as_dict: флаг для работы с типами данных в файле
        (по умолчанию принимает List[List], при as_dict=True принимает List[Dict])
        :return: List[List] | List[Dict]
        """
        with open(self.filepath, 'r', encoding='UTF-8') as file:
            self.data = json.load(file)
            return self.data

    def write_file(self, data: List[List] | List[Dict], as_dict: bool = False) -> None:
        """
        Метод записи данных в файл Json
        :param data: список списков или список словарей
        :param as_dict: флаг для работы с типами данных в файле
        (по умолчанию принимает List[List], при as_dict=True принимает List[Dict])
        :return: None
        """
        with open(self.filepath, 'w', encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def append_file(self, data: List[List] | List[Dict]) -> None:
        """
        Метод дозаписи данных в файл Json - при его вызове выдаст ошибку о невозможности данной операции
        :return:
        """

        raise TypeError(print('Данный тип файла не поддерживает эту операцию!'))


class TxtFileHandler:
    """
    Класс для работы с файлами Txt (чтение, запись, дозапись)
    """

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def read_file(self) -> List[str]:
        """
        Метод для чтения данных из файла txt
        :return: List[str]
        """
        with open(self.filepath, 'r', encoding='UTF-8') as file:
            self.data = file.readlines()
            return self.data

    def write_file(self, data: List[str]) -> None:
        """
        Метод для записи данных в файл txt
        :param data: данные для записи в файл txt в виде List[str]
        :return: None
        """
        with open(self.filepath, 'w', encoding='UTF-8') as file:
            file.writelines(data)

    def append_file(self, data: List[str]) -> None:
        """
        Метод для записи файла txt
        :param data: данные для дозаписи в файл txt в виде List[str]
        :return: None
        """
        with open(self.filepath, 'a', encoding='UTF-8') as file:
            file.writelines(data)


# Данные для тестирования=====================
# список машин для тестирования
list_cars = [
    ['Марка', 'Модель', 'Год выпуска'],
    ['Mercedes', 'E200', '2020'],
    ['Mazda', 'cx90', '2010'],
    ['Nissan', 'Almera', '2005'],
]

# Создаем объект CSV
csv_file = CsvFileHandler('cars.csv')

# Записываем данные в файл Csv
csv_file.write_file(list_cars)

# Получаем данные в виде списка списков и в виде списка словарей
cars_list = csv_file.read_file()
cars_dict = csv_file.read_file(as_dict=True)

pprint(cars_list)
pprint(cars_dict, sort_dicts=False)

# Создаем объект Json
json_file = JsonFileHandler('cars.json')

# Записываем данные в файл Json
json_file.write_file(list_cars)

# Получаем данные в виде списка списков
cars_list_2 = json_file.read_file()
pprint(cars_list_2)

list_cars_2 = ['Mercedes', 'E200', '2020']

# Создаем объект Txt
txt_file = TxtFileHandler('cars.txt')

# Записываем данные в файл Json
txt_file.write_file(list_cars_2)

# Получаем данные в виде списка
cars_list_3 = txt_file.read_file()
pprint(cars_list_3)




