from typing import Callable, List
import csv


# Задание №1 (mypy пройдено)

def password_checker(func: Callable) -> Callable:
    """
    Функция-декоратор проводит валидацию пароля на сложность, сообщает что введен некорректно
    :param func: функция для оборачивания
    :return: обернутая функция
    """

    def wrapper(password: str) -> None:
        # переменная для формирования сообщения пользователю об ошибках в пароле
        result_password = ''
        # параметры для проверки на сложность
        min_length: int = 8
        min_uppercase: int = 1
        min_lowercase: int = 1
        min_digit: int = 1
        special_chars: int = 1

        # флаги для проверки
        is_len: bool = False
        is_upper: bool = False
        is_lower: bool = False
        is_spacebar: bool = False
        is_special: bool = False
        is_digit: bool = False

        # проверка длины пароля
        if len(password) >= min_length:
            is_len = True
        else:
            result_password += 'Пароль должен быть не менее 8 символов!\n'

        # проверка на количество заглавных букв в пароле
        if sum(symbol.isupper() for symbol in password) >= min_uppercase:
            is_upper = True
        else:
            result_password += 'Пароль должен содержать хотя бы 1 заглавную букву!\n'

        # проверка на количество строчных букв в пароле
        if sum(symbol.islower() for symbol in password) >= min_lowercase:
            is_lower = True
        else:
            result_password += 'Пароль должен содержать хотя бы 1 строчную букву!\n'

        # проверка на количество строчных букв в пароле
        if sum(symbol.isdigit() for symbol in password) >= min_digit:
            is_digit = True
        else:
            result_password += 'Пароль должен содержать хотя бы 1 цифру!\n'

        # проверка на отсутствие пробелов в пароле
        if password.find(" ") >= 0:
            result_password += 'Пароль не должен содержать пробел!\n'
        else:
            is_spacebar = True

        # проверка наличия спецзнаков
        if (len(password) - sum(symbol.isalnum() for symbol in password)) >= special_chars:
            is_special = True
        else:
            result_password += 'В пароле должен быть хотя 1 спецзнак, например @ + * # %\n'

        # итоговое соблюдение всех требований к паролю
        if is_len and is_upper and is_lower and is_digit and is_spacebar and is_special:
            return func(password)
        else:
            result_password += 'Пароль не подходит!'
            print(result_password)

    return wrapper


@password_checker
def register_user(password: str) -> None:
    """
    Функция, сообщает пользователю, об успешной регистрации при прохождении проверки пароля на сложность
    :param password: принимает пароль
    :return: None
    """
    print('Вы ввели надежный пароль и прошли регистрацию!')


print('=========Проверка кода по Заданию №1===========')
print('Требования к сложности Пароля:\n'
      '1. Длина пароля не менее 8 символов и не содержать пробелов.\n'
      '2. Пароль должен содержать хотя бы 1 цифру.\n'
      '3. Пароль должен содержать хотя бы 1 заглавную букву.\n'
      '4. Пароль должен содержать хотя бы 1 строчную букву.\n'
      '5. Пароль должен содержать хотя бы 1 из спецзнаков, например @ + * # %\n')
# тестирование проверки сложности пароля
register_user('Passw123####')
register_user('Pass1*')
register_user('passw123%')
register_user('PASSW123*')
register_user('Password/')
register_user('Passw 123+')
register_user('Passw123')
register_user('25524858252*')
print('\n')


# Задание №2 (mypy пройдено)
def password_validator(min_length: int = 8, min_uppercase: int = 1, min_lowercase: int = 1, min_digit: int = 1,
                       min_special_chars: int = 1):
    """
    Функция валидации пароля с параметрами по умолчанию
    :param min_length: длина пароля не менее 8 знаков
    :param min_uppercase: наличие в пароле букв верхнего регистра (не менее 1)
    :param min_lowercase: наличие в пароле букв нижнего регистра (не менее 1)
    :param min_digit: наличие в пароле цифр (не менее 1)
    :param min_special_chars: наличие в пароле спецзнаков (не менее 1)
    :return: обернутая функция
    """

    def decorator_password_validator(func: Callable) -> Callable:
        """
        Функция-декоратор проверки пароля на сложность с использованием параметров
        :param func: функция для оборачивания
        :return: обернутая функция
        """

        def wrapper(username: str, password: str) -> None:

            result_password = ''
            # флаги для проверки
            is_len: bool = False
            is_upper: bool = False
            is_lower: bool = False
            is_digit: bool = False
            is_spacebar: bool = False
            is_special: bool = False

            # проверка длины пароля
            if len(password) >= min_length:
                is_len = True
            else:
                result_password += f'Пароль должен быть не менее {min_length} символов!\n'

            # проверка на количество заглавных букв в пароле
            if sum(symbol.isupper() for symbol in password) >= min_uppercase:
                is_upper = True
            else:
                result_password += f'Пароль должен содержать не менее {min_uppercase} заглавные буквы!\n'

            # проверка на количество строчных букв в пароле
            if sum(symbol.islower() for symbol in password) >= min_lowercase:
                is_lower = True
            else:
                result_password += f'Пароль должен содержать не менее {min_lowercase} строчные буквы!\n'

            # проверка на количество цифр в пароле
            if sum(symbol.isdigit() for symbol in password) >= min_digit:
                is_digit = True
            else:
                result_password += f'Пароль должен содержать не менее {min_digit} цифры!\n'

            # проверка на отсутствие пробелов
            if password.find(" ") >= 0:
                result_password += 'Пароль не должен содержать пробел!\n'
            else:
                is_spacebar = True

            # проверка на наличие спецзнаков
            if (len(password) - sum(symbol.isalnum() for symbol in password)) >= min_special_chars:
                is_special = True
            else:
                result_password += (f'В пароле должно быть не менее {min_special_chars} из спецзнаков,'
                                    f'например @ + * # %\n')

            # итоговая проверка
            if not (is_len and is_upper and is_lower and is_digit and is_spacebar and is_special):
                result_password += 'Пароль не подходит!'
                raise ValueError(result_password)
            return func(username, password)

        return wrapper

    return decorator_password_validator


def username_validator(func: Callable) -> Callable:
    """
    Функция-декоратор проверки имени пользователя без пробелов
    :param func: функция для оборачивания
    :return: обернутая функция
    """

    def wrapper(username: str, password: str) -> None:
        if username.find(" ") > 0:
            raise ValueError(f'Имя пользователя "{username}" не подходит, т.к. содержит пробел!')
        return func(username, password)

    return wrapper


@password_validator(9, 2, 2, 2, 2)
@username_validator
def register_user_2(username: str, password: str) -> None:
    """
    Функция регистрации нового пользователя, при прохождении проверки пароля и имени пользователя на заданные условия.
    Записывает данные в CSV-файл
    :param username: Имя пользователя
    :param password: Пароль пользователя
    :return: None
    """

    print(f'Вы успешно прошли регистрацию:\n Имя пользователя: {username}\n Пароль: {password}')

    with open('register_form.csv', 'a', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([username, password])



print('=========Проверка кода по Заданию №2===========')
print('Требования к сложности Имени пользователя:\n'
      '1. Имя пользователя не должно содержать пробел. Буквы, цифры и спецсимволы допустимы.')
print('Требования к сложности Пароля:\n'
      '1. Длина пароля не менее 9 символов и не содержать пробелов.\n'
      '2. Пароль должен содержать не менее 2 заглавных буквы.\n'
      '3. Пароль должен содержать не менее 2 строчных буквы.\n'
      '4. Пароль должен содержать не менее 2 цифры.\n'
      '5. Пароль должен содержать не менее 2 из спецзнаков, например @ + * # %.\n')

# тестирование успешного случая
try:
    register_user_2('JohnDoe', 'PassW123+%')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')

# тестирование неудачного случая по паролю - нет спецзнака
try:
    register_user_2('JohnDoe', 'PassW1234')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')

# тестирование неудачного случая по паролю - мало символов
try:
    register_user_2('JohnDoe', 'PasS23+%')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')

# тестирование неудачного случая по паролю - мало цифр
try:
    register_user_2('JohnDoe', 'PassWord1+%')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')

# тестирование неудачного случая по паролю - нет букв верхнего регистра
try:
    register_user_2('JohnDoe', 'passw123+%')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')

# тестирование неудачного случая по паролю - нет букв нижнего регистра
try:
    register_user_2('JohnDoe', 'PASSW123+%')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')

# Тестирование неудачного случая по username
try:
    register_user_2('John Doe', 'PassW123+%')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')

# тестирование неудачного случая по username и паролю
try:
    register_user_2('John Doe', 'Passw123+%')
    print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')
