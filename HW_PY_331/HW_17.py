from abc import ABC, abstractmethod
from typing import Dict


# Создание абстрактного класса для умных устройств
class SmartDevice(ABC):
    """
    Абстрактный класс для создания умных устройств
    """

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def turn_on_device(self, *args, **kwargs):
        """
        Метод для включенния устройстве

        """
        pass

    @abstractmethod
    def turn_off_device(self, *args, **kwargs) -> str:
        """
        Метод для выключения устройства

        """
        pass

    @abstractmethod
    def check_device_status(self, *args, **kwargs) -> bool:
        """
        Метод для получения состояния устройства (включено/выключено)

        """
        pass


# создание класса Умная лампочка
class SmartLedBuld(SmartDevice):
    """
    Класс "Умная Лампочка" наследуется от абстрактного класса SmartDevice
    """

    def __init__(self, name: str, brightness: int, power: int, device_status: bool = False) -> None:
        """
        Инициализация экземпляров класса
        :param name: название
        :param brightness: яркость лампочки
        :param power: максимальная мощность лампочки
        :param device_status: статус лампочки (по умолчанию выключено - False)
        """
        super().__init__(name)
        self.device_status = device_status
        self.brightness = brightness
        self.power = power

    def turn_on_device(self):
        """
        Метод для включения устройства Умная лампочка

        """
        self.device_status = True

    def turn_off_device(self):
        """
        Метод для выключения устройства - Умная лампочка

        """
        self.device_status = False

    def check_device_status(self):
        """
        Метод для получения состояния устройства (включено/выключено) - Умная лампочка

        """
        if self.device_status:
            return f'Лампочка включена'
        else:
            return f'Лампочка выключена'

    def set_brightness(self, brightness: int):
        """
        Метод регулирования яркости лампочки. Проверяет на корректность ввода значения яркости лампочки

        :param brightness: яркость лампочки
        """
        self.brightness = brightness
        if self.brightness <= self.power:
            print(f'Яркость SmartLedBuld = {self.brightness}')
        else:
            raise ValueError(f'Некорректное значение яркости лампочки (мощность всего {self.power})')


# Создание класса Умный датчик дыма
class SmartSmokeDetector(SmartDevice):
    """
    Класс "Умный датчик дыма" наследуется от абстрактного класса SmartDevice
    """

    def __init__(self, name: str, device_status: bool = False) -> None:
        """
        Инициализация экземпляров класса
        :param name: название
        :param device_status: статус датчика дыма (по умолчанию выключено - False)
        """
        super().__init__(name)
        self.device_status = device_status

    def turn_on_device(self):
        """
        Метод для включения устройства - Умный датчик дыма
        """
        self.device_status = True

    def turn_off_device(self):
        """
        Метод для выключения устройства - Умный датчик дыма
        """
        self.device_status = False

    def check_device_status(self):
        """
        Метод для получения состояния устройства (включено/выключено) - Умный датчик дыма
        :return: str
        """
        if self.device_status:
            return f'Датчик дыма включен'
        else:
            return f'Датчик дыма выключен'

    def check_smoke(self, is_smoke=False) -> bool:
        """
        Метод для проверки дыма

        """
        self.is_smoke = is_smoke
        if is_smoke:
            return self.is_smoke
        else:
            return self.is_smoke


# Создание класса Умный увлажнитель воздуха
class SmartHumidifier(SmartDevice):
    """
    Класс "Умный увлажнитель воздуха" наследуется от абстрактного класса SmartDevice
    """

    def __init__(self, name: str, humidity_level: int, max_humidity: int, device_status: bool = False) -> None:
        """
        Инициализация экземпляров класса
        :param name: название
        :param humidity_level: уровень влажности
        :param max_humidity: максимальная уровень влажности устройства
        :param device_status: статус устройства (по умолчанию выключено - False)
        """
        super().__init__(name)
        self.device_status = device_status
        self.humidity_level = humidity_level
        self.max_humidity = max_humidity

    def turn_on_device(self):
        """
        Метод для включения устройства - Умный увлажнитель воздуха

        """
        self.device_status = True

    def turn_off_device(self):
        """
        Метод для выключения устройства - Умный увлажнитель воздуха

        """
        self.device_status = False

    def check_device_status(self):
        """
        Метод для получения состояния устройства (включено/выключено) - Умный увлажнитель воздуха

        :return: str
        """
        if self.device_status:
            return f'Увлажнитель воздуха включен'
        else:
            return f'Увлажнитель воздуха выключен'

    def set_humidity(self, humidity_level: int):
        """
        Метод регулирования влажности воздуха

        :humidity: значение влажности воздуха.
        :max_humidity: максимальная уровень влажности воздуха
        :return: str
        """
        self.humidity_level = humidity_level
        if self.humidity_level <= self.max_humidity:
            print(f'Влажность воздуха будет установлена: {self.humidity_level}')
        else:
            raise ValueError(f'Некорректное значение влажности воздуха (мощность всего {self.max_humidity})')


# Миксины
# Миксин "Срочное уведомление"
class MixinNotice:
    """
    Миксин для отправки срочного уведомления

    """

    def __init__(self, message: str):
        self.message = message

    def send_message(self, message: str):
        """
        Метод для отправки срочного уведомления

        :message: сообщение для отправки с умного устройства.
        """
        self.message = message
        print(f'{self.message}')


# Миксин "Подключение к Wi-Fi"
class MixinWiFi:
    """
    Миксин для подключения к Wi-Fi

    """
    def __init__(self, name_net: str, password: str):
        """
        Инициализация миксина
        :param name_net: имя сети
        :param password: пароль сети
        """
        self.name_net = name_net
        self.password = password

    def connect_wifi(self, name_net: str, password: str):
        """
        Метод для подключения к Wi-Fi
        :param name_net: имя сети
        :param password: пароль к сети
        """
        return self.name_net == name_net, self.password == password


# Миксин "Время работы"
class MixinWorkTime:
    """
    Миксин для установки времени работы устройства

    """

    def __init__(self, time: Dict[str, str]):
        """
        Инициализация миксина
        :param time: время работы устройства
        """
        self.time = time

    def set_schedule(self, time: Dict[str, str]):
        """
        Метод для установки времени работы устройства
        :param time: время работы устройства
        """
        return self.time == time


# Создание классов устройств с Миксинами
# Умная лампочка
class SmartLedBuldXiaomi(SmartLedBuld, MixinWiFi):
    """
    Класс "Умная Лампочка Xiaomi" наследуется от класса SmartLedBuld+MixinWiFi
    """

    def __init__(self, name: str, brightness: int, name_net: str, password: str,
                 power: int = 9) -> None:
        super().__init__(name, brightness, power)
        MixinWiFi.__init__(self, name_net, password)


# Умный увлажнитель воздуха
class SmartHumidifierKitfort(SmartHumidifier, MixinWiFi, MixinWorkTime):
    """
    Класс "Умный увлажнитель Kitfort" наследуется от класса SmartHumidifier+MixinWiFi+MixinWorkTime
    """

    def __init__(self, name: str, name_net: str, password: str, humidity_level: int = 45,
                 max_humidity: int = 75, time=None) -> None:
        super().__init__(name, humidity_level, max_humidity)
        MixinWiFi.__init__(self, name_net, password)
        MixinWorkTime.__init__(self, time)


# Умный датчик дыма
class SmartSmokeDetectorLegrand(SmartSmokeDetector, MixinWiFi, MixinNotice):
    """
    Класс "Умный датчик дыма Legrand" наследуется от класса SmartSmokeDetector+MixinWiFi+MixinNotice
    """

    def __init__(self, name: str, name_net: str, password: str, message=None) -> None:
        super().__init__(name)
        MixinWiFi.__init__(self, name_net, password)
        MixinNotice.__init__(self, message)


# Проверка работы методов класса
print('===========Умная лампочка==========')
# Создание устройства
lamp_hall = SmartLedBuldXiaomi('Гостиная', 50, 'MyNetwork', '123456')
# Настройка устройства (подключение к wi-fi)
lamp_hall.connect_wifi('MyNetwork', '123456')

# Управление устройством (включение)
lamp_hall.turn_on_device()
# Управление устройством (выключение)
# lamp_hall.turn_off_device()
# Управление устройством (установка яркости лампочки)
lamp_hall.set_brightness(5)

# Статус устройства
print(lamp_hall.check_device_status())

print('===========Умный увлажнитель==========')
# Создание устройства
humidifier_child = SmartHumidifierKitfort('Детская', 'MyNetwork', '123456')
# Настройка устройства
humidifier_child.connect_wifi('MyNetwork', '123456')
humidifier_child.set_schedule({'10.00': 'включить', '22:00': 'выключить'})

# Управление устройством (включение)
humidifier_child.turn_on_device()
# Управление устройством (выключение)
# humidifier_child.turn_off_device()
# Управление устройством (установка влажности в помещении)
humidifier_child.set_humidity(50)

# Статус устройства
print(humidifier_child.check_device_status())

print('===========Умный датчик дыма==========')
# Создание устройства
smoke_detector_kitchen = SmartSmokeDetectorLegrand('Кухня', 'MyNetwork', '123456')
# Настройка устройства
smoke_detector_kitchen.connect_wifi('MyNetwork', '123456')

# Управление устройством (включение)
smoke_detector_kitchen.turn_on_device()
# Управление устройством (выключение)
# smoke_detector_kitchen.turn_off_device()

# Статус устройства
print(smoke_detector_kitchen.check_device_status())

# Имитация проверки срабатывания датчика дыма
if smoke_detector_kitchen.check_smoke(True):
    smoke_detector_kitchen.send_message("Обнаружен дым на кухне!")
#
