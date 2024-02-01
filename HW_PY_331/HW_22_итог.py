from abc import ABC, abstractmethod


class IngredientFactory(ABC):
    """
    Класс (абстрактный) для создания ингредиентов пиццы
    """

    @abstractmethod
    def create_cheese(self) -> str:
        """
        Абстрактный метод для возврата типа сыра
        :return: str
        """
        pass

    @abstractmethod
    def create_sauce(self) -> str:
        """
        Абстрактный метод для возврата типа соуса
        :return: str
        """
        pass


class DodoIngredientFactory(IngredientFactory):
    """
    Класс (фабрика) на основе ингредиентов, предоставляемых Додо-пиццей
    """

    def create_cheese(self) -> str:
        """
        Метод для возврата типа сыра
        :return: str
        """
        return 'сыр Пармезан'

    def create_sauce(self) -> str:
        """
        Метод для возврата типа соуса
        :return: str
        """
        return 'соус Италиано'


class SizeFactory:
    """
    Класс (фабрика) для управления размером пиццы
    """

    def create_size(self, size: str):
        """
        Метод принимает название размера пиццы и возвращает его описание
        :param size: название пиццы
        :return: описание размера пиццы, при вводе неверного названия - выдает 'нет такого размера'
        """
        sizes = {
            'маленькая': 'размер 20 см',
            'средняя': 'размер 30 см',
            'большая': 'размер 40 см'
        }
        return sizes.get(size.lower(), "Неизвестный размер")


class PizzaBuilder:
    """
    Класс (строитель) в котором собираем пиццу, используя ингредиенты и размеры
    """

    def __init__(self, ingredient_factory, size_factory, pizza_tipe):
        self.ingredient_factory = ingredient_factory
        self.size_factory = size_factory
        self.pizza_tipe = pizza_tipe
        self.size = None

    def set_size(self, size: str):
        """
        Метод устанавливает размер пиццы
        :param size: размер пиццы
        :return: str
        """
        self.size = self.size_factory.create_size(size)

    def build(self):
        """
        Метод сборки пиццы
        :return: описание заказанной пиццы
        """
        cheese_pizza = self.ingredient_factory.create_cheese()
        sauce_pizza = self.ingredient_factory.create_sauce()
        return f"Пицца: {self.pizza_tipe}, {self.size}, {cheese_pizza} и {sauce_pizza}"


def create_pizza():
    """
    Функция создания заказа пиццы
    :return: описание заказа пиццы
    """
    ingredient_factory = DodoIngredientFactory()
    size_factory = SizeFactory()
    pizza_tipe = input('Выберите тип пиццы (Неаполитанcкая, Кальцоне, Римская, Сицилийская): ')
    size = input('Выберите размер пиццы (маленькая, средняя, большая): ')

    # создаем пиццу
    creation = PizzaBuilder(ingredient_factory, size_factory, pizza_tipe)
    # создание размера
    creation.set_size(size)

    return creation.build()


# точка входа в программу
def main():
    """
    Функция запуска программы по созданию пиццы
    :return: выводит описание заказа
    """
    order = create_pizza()
    print("Вы заказали: \n" + order)


if __name__ == "__main__":
    main()
