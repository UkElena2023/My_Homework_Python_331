# импорт библиотеки json
import json

from typing import List, Set


def get_cities_set_from_json(file_name: str) -> Set[str]:
    """
    Функция читает список городов России из файла cities_set_2.json
    :param file_name: файл со списком городов России
    :return: возвращает сет городов России
    """

    with open(file_name, 'r', encoding='UTF-8') as file:
        city_set = json.load(file)
        # создание сета городов России
        cities_set_2 = {value['name'].lower().replace("ё", 'е') for value in city_set}
    return cities_set_2


def get_list_result_from_json(file_name_result: str) -> List[str]:
    """
    Функция читает список результатов игры из файла json для выдачи информации счета перед началом игры
    :param file_name_result: файл с результатами игры
    :return: возвращает список результатов игры
    """
    with open(file_name_result, 'r', encoding='UTF-8') as file:
        result_list = json.load(file)
    return result_list


def check_city_user(city_random: str, user_input: str) -> bool:
    """
    Функция проверки верного ввода пользователем города России на правильную букву
    :param city_random: город в России выбранный рандомно в начале игры, потом он заменяется на город от компьютера
    :param user_input: ввод пользователем города России
    :return: bool
    """
    if city_random[-1] == 'ы' and user_input[0] != city_random[-2]:
        print(f'Вы назвали город не на ту букву, Вам на "{city_random[-2]}"!')
        return True
    elif city_random[-1] == 'ь' and user_input[0] != city_random[-2]:
        print(f'Вы назвали город не на ту букву, Вам на "{city_random[-2]}"!')
        return True
    elif user_input[0] != city_random[-1] and city_random[-1] != 'ы' and city_random[-1] != 'ь':
        print(f'Вы назвали город не на ту букву, Вам на "{city_random[-1]}"!')
        return True
    else:
        return False


def write_list_result_in_json(file_result: str, result_list_end: str) -> str:
    """
    Функция записывает результаты игры в файл result_2.json по ее завершении
    :param file_result: файл с результатами игры
    :param result_list_end: список результатов игры
    :return: обновленный список результатов игры
    """
    with open(file_result, 'w', encoding='UTF-8') as file:
        json.dump(list(result_list_end), file, ensure_ascii=False, indent=4)
    return result_list_end


def main():
    """
    Главная функция
    """
    # чтение из созданного файла result.json данных для выведения результата игры
    result_list = get_list_result_from_json('result_2.json')

    # проверка на количество результатов в result_2.json
    if len(result_list) > 5:
        result_list.pop()

    # читаем сет городов из файла cities_set.json данных для создания сета городов
    cities_set_2 = get_cities_set_from_json('cities_set_2.json')

    # начало игры
    print('ИГРА В ГОРОДА РОССИИ\n'
          'Правила:\n'
          '1. Название города в России должно начинаться на последнюю букву города, выданного компьютером.\n'
          '2. Если название города заканчивается на "ь" или "ы" Вы можете ввести город с предпоследней буквы '
          '(компьютер сделает также).\n'
          '3. Повторять города нельзя.\n')

    # чтение из созданного файла result.json данных для выведения результата игры
    result_list = get_list_result_from_json('result_2.json')

    # проверка на количество результатов в result_2.json
    if len(result_list) > 5:
        result_list.pop()

    # определение счета в игре
    score_user = result_list.count('Поздравляю, Вы обыграли компьютер!')
    score_comp = result_list.count('Вы проиграли, компьютер оказался умнее!')

    # вывод результатов последних 5-ти игр перед началом игры
    if score_user > score_comp:
        print(f'Счет в последних 5-ти играх {score_user} : {score_comp} в Вашу пользу!\n')
    elif score_user == score_comp:
        print(f'Счет в последних 5-ти играх {score_user} : {score_comp} - ничья!\n')
    else:
        print(f'Счет в последних 5-ти играх {score_comp} : {score_user} в пользу компьютера!\n')

    # создание сета с удаленными городами
    cities_set_repeat = set()

    # создание рандомного города для начала игры, удаление его из сета городов
    city_name_random = cities_set_2.pop()

    # добавление названного пользователем города в пустой сет "cities_set_repeat" для выявления повторений
    cities_set_repeat.add(city_name_random)
    print('Компьютер начинает: ' + city_name_random.capitalize())

    # задаем цикл на игру в города
    while cities_set_2:
        # запрос названия города от пользователя
        city_name_user = input('Введите название города в России или "стоп", если не знаете города: ').lower()
        city_name_user = city_name_user.replace("ё", 'е').strip()

        # остановка игры при помощи "стоп" слова
        if city_name_user == 'стоп':
            # flag = True
            # вывод результата игры, если компьютер выиграл
            print('Вы проиграли, компьютер оказался умнее!')
            result_list.insert(0, 'Вы проиграли, компьютер оказался умнее!')
            break

        # проверка названия города, введенного пользователем на правильную букву
        if check_city_user(city_name_random, city_name_user, ):
            print('Вы проиграли, компьютер оказался умнее!')
            result_list.insert(0, 'Вы проиграли, компьютер оказался умнее!')
            break

        # проверка названия города, введенного пользователем на повтор
        if city_name_user in cities_set_repeat:
            print('Такой город уже называли!')
            print('Вы проиграли, компьютер оказался умнее!')
            result_list.insert(0, 'Вы проиграли, компьютер оказался умнее!')
            break

        # проверка названия города, введенного пользователем на вхождение в сет городов
        if city_name_user not in cities_set_2 and city_name_user not in cities_set_repeat:
            print('Такого города нет в России или Вы неправильно написали!')
            print('Вы проиграли, компьютер оказался умнее!')
            result_list.insert(0, 'Вы проиграли, компьютер оказался умнее!')
            break

        else:
            print('Такой город есть!')
            # добавление названного пользователем города в пустой сет "cities_set_repeat" для выявления повторений
            cities_set_repeat.add(city_name_user)
            # удаление названного пользователем города из сета городов "cities_set"
            cities_set_2.discard(city_name_user)

        # задание цикла для компьютера - определение названия города для передачи пользователю
        for city_name_comp in cities_set_2:
            if city_name_comp[0] == city_name_user[-1] and (city_name_user[-1] != 'ь' or city_name_user[-1] != 'ы'):
                city_name_random = city_name_comp
                print(f'Я называю: {city_name_comp.capitalize()}')
                # добавление названного компьютером города в сет "cities_set_repeat" для выявления повторений
                cities_set_repeat.add(city_name_comp)
                # удаление названного компьютером города из сета городов "cities_set"
                cities_set_2.discard(city_name_comp)
                break
            elif city_name_comp[0] == city_name_user[-2] and (city_name_user[-1] == 'ь' or city_name_user[-1] == 'ы'):
                city_name_random = city_name_comp
                print(f'Я называю: {city_name_comp.capitalize()}')
                # добавление названного компьютером города в сет "cities_set_repeat" для выявления повторений
                cities_set_repeat.add(city_name_comp)
                # удаление названного компьютером города из сета городов "cities_set"
                cities_set_2.discard(city_name_comp)
                break

        else:
            # вывод результата игры, если компьютер проиграл
            print('Поздравляю, Вы обыграли компьютер!')
            result_list.insert(0, 'Поздравляю, Вы обыграли компьютер!')
            break

    write_list_result_in_json('result_2.json', result_list)


main()
