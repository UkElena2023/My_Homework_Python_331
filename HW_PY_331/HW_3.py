user_input = input('Введите слово: ')
if user_input.lower() == user_input.lower()[::-1]:
    message_da = f"Введенное Вами слово \"{user_input}\" является палиндромом!"
    print(message_da)
else:
    message_net = f"Введенное Вами слово \"{user_input}\" НЕ является палиндромом!"
    print(message_net)
