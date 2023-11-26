# импорт словаря "cities_list" из файла "cities.py"
from cities import cities_list

print('ИГРА В ГОРОДА РОССИИ\n'
      'Правила:\n'
      '1. Название города в России должно начинаться на последнюю букву города, выданного компьютером.\n'
      '2. Если название города заканчивается на "ь" или "ы" Вы можете ввести город с предпоследней буквы '
      '(компьютер сделает также).\n'
      '3. Повторять города нельзя.\nВаш ход!\n')
# создание сета наполненный городами из списка
cities_set = {value['name'].lower().replace("ё", 'е') for value in cities_list}

# создание сета с удаленными городами
cities_set_repeat = set()
# вводим флаг для отсечки прекращения игры по "стоп" слову
flag = True
# задаем цикл на игру в города
while flag:
    # запрос названия города от пользователя
    city_name = input('Введите название города в России или "стоп" для завершения игры: ').lower()
    city_name_end = city_name.replace("ё", 'е').strip()
    # условия остановки игры при помощи "стоп" слова
    if city_name_end == 'стоп':
        flag = False
        # вывод результата игры, если компьютер выиграл
        print('Вы проиграли, компьютер оказался умнее!')
        break
    # задаем условие на проверку наличия города в сете городов
    if city_name_end in cities_set:
        # переменная на определение города компьютером по последней букве города от пользователя
        first_letter = city_name_end[-1]
        # переменная на определение города компьютером по предпоследней букве города от пользователя
        first_letter_2 = city_name_end[-2]
        # добавление названного пользователем города в пустой сет "cities_set_repeat" для выявления повторений
        cities_set_repeat.add(city_name_end)
        # удаление названного пользователем города из сета городов "cities_set"
        cities_set.discard(city_name_end)
        # задание цикла для компьютера - определение названия города для передачи пользователю
        for city_name_comp in cities_set:
            if first_letter == city_name_comp[0] and (first_letter != 'ь' or first_letter != 'ы'):
                print(city_name_comp.capitalize())
                # добавление названного компьютером города в сет "cities_set_repeat" для выявления повторений
                cities_set_repeat.add(city_name_comp)
                # удаление названного компьютером города из сета городов "cities_set"
                cities_set.discard(city_name_comp)
                break
            elif first_letter_2 == city_name_comp[0] and (first_letter == 'ь' or first_letter == 'ы'):
                print(city_name_comp.capitalize())
                # добавление названного компьютером города в сет "cities_set_repeat" для выявления повторений
                cities_set_repeat.add(city_name_comp)
                # удаление названного компьютером города из сета городов "cities_set"
                cities_set.discard(city_name_comp)
                break
        else:
            # вывод результата игры, если компьютер проиграл
            print('Поздравляю, Вы обыграли компьютер!')
            break
    else:
        # проверка ввода пользователем города на повтор и на наличие в сете оставшихся городов
        if city_name_end in cities_set_repeat:
            print('Такой город уже называли!')
        else:
            print('Такого города нет в России или Вы неправильно написали!')

# print(cities_set_repeat)
# print(cities_set)
