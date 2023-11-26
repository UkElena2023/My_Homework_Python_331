# Задание №1
sum_second = int(input('Введите произвольное количество секунд: '))
value_hours = sum_second // 3600
value_min = (sum_second - (value_hours * 3600)) // 60
value_sec = (sum_second - (value_hours * 3600)) % 60
print(f'В указанном количестве секунд {sum_second}: \nЧасов: {value_hours} '
      f'\nМинут: {value_min} \nСекунд: {value_sec}')

# Задание №2
degree_celsiyus= int(input('\nВведите произвольное количество градусов Цельсия: '))
degree_kelvin = degree_celsiyus + 273.15
degree_fahrenheit = degree_celsiyus * 1.8 + 32
degree_reaumur = degree_celsiyus * 0.8
print(f'В указанном количестве градусов Цельсия: {degree_celsiyus} \nГрадусов Кельвина: '
      f'{degree_kelvin} \nГрадусов Фаренгейта: {degree_fahrenheit:.2f} \nГрадусов Реомюра: '
      f'{degree_reaumur:.2f}')