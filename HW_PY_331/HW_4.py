# Задание №2
user_input = input('Придумайте пароль, который должен содержать более 7 символов, заглавные и строчные буквы,'
                   ' хотя бы один из спецзнаков = * # % \n')
result_pass = ''
is_len = False
is_result = False
is_propusk = False
is_special = False

if len(user_input) > 7:
    is_len = True
else:
    result_pass += 'Пароль должен быть более 7 символов!\n'

if not (user_input.islower() or user_input.isupper()):
    is_result = True
else:
    result_pass += 'В пароле должны быть буквы разных регистров!\n'

if user_input.find(" ") >= 0:
    result_pass += 'Пароль не должен содержать пробел!\n'
else:
    is_propusk = True

if user_input.find("=") >= 0 or user_input.find("*") >= 0 or user_input.find("#") >= 0 or user_input.find("%") >= 0:
    is_special = True
else:
    result_pass += 'В пароле должен быть хотя бы один спецзнак = * # %!\n'

if is_len and is_result and is_propusk and is_special:
    result_pass += 'Вы ввели надежный пароль!'
else:
    result_pass += 'Пароль не подходит!'
print(result_pass)

# Задание №1
user_input_2 = input('Введите свой номер телефона, пожалуйста: ')
user_input_2_1 = user_input_2.strip().strip('+')
user_input_2_2 = user_input_2_1.replace('-', "").replace(' ', "")
user_input_end = user_input_2_2.replace(')', "").replace('(', "")

result_num = ''
is_len_2 = False
is_num = False
is_start = False

if len(user_input_end) == 11:
    is_len_2 = True
else:
    result_num += 'Введенный номер должен содержать 11 цифр!\n'

if user_input_end.isdigit():
    is_num = True
else:
    result_num += 'Введенный номер должен содержать только цифры!\n'

if user_input_2.startswith('+') or user_input_2.startswith('+7') or user_input_2.startswith('8'):
    is_start = True
else:
    result_num += 'Начало Вашего номера должно начинаться с +7 или 8!\n'

if is_len_2 and is_num and is_start:
    result_num += 'Спасибо, Вы ввели номер телефона верно!'
else:
    result_num += 'Неверно введен номер телефона!'

print(result_num)
