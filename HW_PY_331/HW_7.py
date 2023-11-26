# Задание №1
# первичный список для проверки данных на валидность (=число)
data_lst = ['1', '2', '3', 'jhkh', '458', '4d', 5]
# пустой список для наполнения данными, прошедшими проверку на валидность (=число)
new_lst = []

# задание цикла на проверку
for num in data_lst:
    # конструкция "try-except" на выявление логической ошибки при выявлении нечислового значения данных
    try:
        num_int = int(num)
        new_lst.append(num_int)
    except ValueError:
        print(f'Значение "{num}" из списка не прошло проверку на валидность!')

print(new_lst)

# Задание №2
user_input = input('Введите, пожалуйста, номера телефонов, разделяя их знаком ";" \n')

# создание списка номеров введенных пользователем для проверки на валидность
user_input_list = user_input.split(";")
# user_input_list_end = []

# задаем цикл для проверки номеров в списке на валидность
for number in user_input_list:
    # очистка каждого номера из списка до состава из одних цифр
    number_1 = number.strip()
    number_2 = number_1.replace('-', "").replace(' ', "")
    number_3 = number_2.replace(')', "").replace('(', "")
    number_end = number_3.strip('+')

    # генерируем исключения для вывода ошибок
    # Ошибка 1 - проверка на отсутствие данных при первичном вводе пользователем
    if len(user_input) == 0:
        raise ValueError(f'Вы не ввели номер "{number}" телефона!\n')

    # Ошибка 2 - проверка на разрешенное начало номера +7, 8
    if not (number_3.startswith('+7') or number_3.startswith('8')):
        raise ValueError(f'Номер телефона "{number}" должен начинаться с +7 или 8!\n')

    # Ошибка 3 - проверка на лишние знаки внутри номера, кроме разрешенных
    if not number_end.isdigit():
        raise TypeError(f'Введенный номер "{number}" должен содержать только цифры!\n')

    # Ошибка 4 - количество цифр в номере
    if len(number_end) <= 10 or len(number_end) > 11:
        raise ValueError(f'Введенный номер "{number}" должен содержать 11 цифр!\n')
    # добавление проверенных номеров в конечный список
    # user_input_list_end.append(number_end)

# print(user_input_list_end)
