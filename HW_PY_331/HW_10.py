# импорт библиотеки json
import json

# _________________операции по созданию json файла _________________
# импорт словаря "cities_list" из файла "cities.py"
# from cities import cities_list
# создание сета наполненного городами из списка
# cities_set = {value['name'].lower().replace("ё", 'е') for value in cities_list}
# создание списка словарей с парой ключ-значение
# json_city_set = []
# for item in cities_set:
#     json_city_set.append(
#         {'name': item}
#     )
# # создаем файл json с сетом из городов
# with open('cities_set.json', 'w', encoding='UTF-8') as file:
#     json.dump(json_city_set, file, ensure_ascii=False, indent=4)
# _________________конец операций по созданию json файла _________________

# # _________________операции по созданию json-файла для результата игры _________________
# result = []
# with open('result.json', 'w', encoding='UTF-8') as file:
#     json.dump(list(result), file, ensure_ascii=False, indent=4)
# # _________________конец операций по созданию json-файла для результата игры _________________


# чтение из созданного файла cities_set.json данных для создания сета городов
with open('cities_set.json', 'r', encoding='UTF-8') as file:
    city_set = json.load(file)
    # создание сета городов России
    cities_set_2 = {value['name'].lower().replace("ё", 'е') for value in city_set}

# начало игры
print('ИГРА В ГОРОДА РОССИИ\n'
      'Правила:\n'
      '1. Название города в России должно начинаться на последнюю букву города, выданного компьютером.\n'
      '2. Если название города заканчивается на "ь" или "ы" Вы можете ввести город с предпоследней буквы '
      '(компьютер сделает также).\n'
      '3. Повторять города нельзя.\n')

# чтение из созданного файла result.json данных для выведения результата игры
with open('result.json', 'r', encoding='UTF-8') as file:
    result_list = json.load(file)

# проверка на количество результатов в result.json
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

# вводим флаг для отсечки прекращения игры
flag = False

# задаем цикл на игру в города
while not flag:
    # запрос названия города от пользователя
    city_name_user = input('Введите название города в России или "стоп", если не знаете города: ').lower()
    city_name_user = city_name_user.replace("ё", 'е').strip()

    # остановка игры при помощи "стоп" слова
    if city_name_user == 'стоп':
        flag = True
        # вывод результата игры, если компьютер выиграл
        print('Вы проиграли, компьютер оказался умнее!')
        result_list.insert(0, 'Вы проиграли, компьютер оказался умнее!')
        # break
    # создание условий для проверки верного ввода пользователем города России
    elif city_name_user not in cities_set_2 and city_name_user not in cities_set_repeat:
        print('Такого города нет в России или Вы неправильно написали!')
    elif city_name_random[-1] == 'ы' and city_name_user[0] != city_name_random[-2]:
        print(f'Вы назвали город не на ту букву, Вам на "{city_name_random[-2]}"!')
    elif city_name_random[-1] == 'ь' and city_name_user[0] != city_name_random[-2]:
        print(f'Вы назвали город не на ту букву, Вам на "{city_name_random[-2]}"!')
    elif city_name_user[0] != city_name_random[-1] and city_name_random[-1] != 'ы' and city_name_random[-1] != 'ь':
        print(f'Вы назвали город не на ту букву, Вам на "{city_name_random[-1]}"!')
    elif city_name_user in cities_set_repeat:
        print('Такой город уже называли!')

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
            flag = True
            # вывод результата игры, если компьютер проиграл
            print('Поздравляю, Вы обыграли компьютер!')
            result_list.insert(0, 'Поздравляю, Вы обыграли компьютер!')

# result_list.clear() # очистка списка результатов

# перезапись файла result.json с результатами окончания игры
with open('result.json', 'w', encoding='UTF-8') as file:
    json.dump(list(result_list), file, ensure_ascii=False, indent=4)
