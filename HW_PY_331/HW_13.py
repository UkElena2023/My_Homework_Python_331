from pprint import pprint
from typing import List, Optional, Set, Any, Dict, Union

from marvel import full_dict

# Задание 2 (mypy пройдено)
user_input_list: List[str] = input('Введите несколько чисел через пробел: ').split(" ")
num_list: List[Optional[int]] = list(map(lambda num: int(num) if num.isdigit() else None, user_input_list))
print(f'Печать Задания №2 создание списка id:\n{num_list}')
print('=========================================================================\n')

# Задание 3 (mypy пройдено)
# словарь с фильтром по id, заданным пользователем
result_dict: Dict[int, Any] = dict(filter(lambda movie: movie[0] in num_list, full_dict.items()))
print(f'Печать Задания №3 словарь с фильтром по id, заданным пользователем:')
pprint(result_dict, sort_dicts=False)
print('=========================================================================\n')

# Задание 4 (mypy пройдено)
# задания через Set comprehension - создание сета по параметру "director"
director_set: Set[str] = {movie['director'] for movie in full_dict.values() if movie['director'] != 'TBA'}
print(f'Печать Задания №4 создание сета по параметру "director":')
pprint(director_set)
print('=========================================================================\n')

# Задание 5 (mypy пройдено)
# копия словаря full_dict с функцией str на параметре "year"
new_full_dict_4: Dict[int, Dict[str, str]] = {key:
                                                  {'title': value['title'],
                                                   'year': str(value['year']),
                                                   'director': value['director'],
                                                   'screenwriter': value['screenwriter'],
                                                   'producer': value['producer'],
                                                   'stage': value['stage']}
                                              for key, value in full_dict.items()}
print(f'Печать Задания №5 копия словаря full_dict с функцией str на параметре "year":')
pprint(new_full_dict_4, sort_dicts=False)
print('=========================================================================\n')

# Задание 6 (mypy пройдено)
# через filter создание словаря с фильтром фильмов на "Ч"
new_full_dict_filter: Dict[int, Any] = dict(filter(
    lambda v: v[1]['title'].startswith('Ч'), full_dict.items()))
print(f'Печать Задания №6 словарь с фильтром фильмов на "Ч":')
pprint(new_full_dict_filter, sort_dicts=False)
print('=========================================================================\n')

# Задание 7 (mypy пройдено)
# через lambda функцию по параметру 'title' по алфавиту
full_dict_sort1: Dict[int, Dict[str, str | int]] = dict(
    sorted(full_dict.items(), key=lambda item: item[1]['title'], reverse=False))
print(f'Печать Задания №7 словарь с сортировкой по параметру "title" по алфавиту:')
pprint(full_dict_sort1, sort_dicts=False)
print('=========================================================================\n')

# Задание 8 (mypy пройдено)
# через lambda функцию создание словаря по параметру 'screenwriter' по алфавиту и по году
full_dict_sort4: Dict[int, Dict[str, Union[str, int]]] = dict(
    sorted(full_dict.items(), key=lambda item: (item[1]['screenwriter'], item[1]['year']), reverse=False))
print(f'Печать Задания №8 словарь с сортировкой по параметрам "screenwriter по алфавиту и year":')
pprint(full_dict_sort4, sort_dicts=False)
print('=========================================================================\n')

# Задание 9 (mypy пройдено)
# создание словаря filter - по фазе "Первая фаза", sorted - по названию фильма по алфавиту и году выпуска
full_dict_sort5: Dict[int, Dict[str, Union[str, int]]] = dict(filter(lambda movie: movie[1]['stage'] == 'Первая фаза',
                                                                     sorted(full_dict.items(),
                                                                            key=lambda item: (
                                                                                item[1]['title'], item[1]['year']),
                                                                            reverse=False)))

print(f'Печать Задания №9 словарь отфильтрован по фазе "Первая фаза" с сортировкой по названию по алфавиту и году:')
pprint(full_dict_sort5, sort_dicts=False)
