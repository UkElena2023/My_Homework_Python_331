# импорт словаря "full_dict" из файла "marvel.py"
from marvel import full_dict

# словарь с элементами фаз
stage_dict = {
    1: 'Первая фаза',
    2: 'Вторая фаза',
    3: 'Третья фаза',
    4: 'Четвёртая фаза',
    5: 'Пятая фаза',
    6: 'Шестая фаза',
}
user_input = input('Введите номер фазы Киновселенной Marvel, чтобы узнать какие фильмы в нее вошли: ')

# создание списка ключей из словаря "stage" для проверки ввода пользователем фазы
stage_list = list(stage_dict.keys())
# print(stage_list)
# создание списка словарей с фильмами
full_dict_list = list(full_dict.values())

# создание списка для вывода фильмов относящихся к запросу пользователя "фаза"
film_list = []

# генерация ошибок ввода пользователем
# Ошибка №1
if not user_input.isdigit():
    raise TypeError('Вы ввели номер фазы не корректно, должно быть числовое значение!\n')

# Ошибка №2
if not int(user_input) in stage_list:
    raise ValueError(f'Такой фазы "{user_input}" в Киновселенной Marvel нет')

# создание условия для начала выборки
if int(user_input) in stage_list:
    print(f'\nВ {user_input} фазу Киновселенной Марвел входят следующие фильмы:')

# получение наименования "фазы"
value_stage = stage_dict.get(int(user_input))

# создание цикла для поиска в словаре full_dict по найденной фазе
for num, film_info in full_dict.items():
    film = film_info['title']
    if value_stage == film_info['stage']:
        film_list.append(film)

# вывод для пользователя списка найденных фильмов
count = 0
for title_film in film_list:
    print(f'{count + 1}. {title_film}')
    count += 1
