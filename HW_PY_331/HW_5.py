# Секретное послание
secret_letter = [
    ['DFВsjl24sfFFяВАДОd24fssflj234'],
    ['asdfFп234рFFdо24с$#afdFFтasfо'],
    ['оafбasdf%^о^FFжа$#af243ю'],
    ['afпFsfайFтFsfо13н'],
    ['fн13Fа1234де123юsdсsfь'],
    ['чFFтF#Fsfsdf$$о'],
    ['и$ՐҶsfF'], ['вSFSDам'],
    ['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
    ['FFэasdfтDFsfоasdfFт'],
    ['FяDSFзFFsыSfкFFf']
]
# список с маленькими русскими буквами
small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
             'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
             'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# переменная для создания списка после расшифровки
new_letter = []
# цикл проверки наличия русских букв в послании
for list_ in secret_letter:
    for item in list_:
        for symbol in item:
            if symbol in small_rus:
                new_letter.append(symbol)
# ввод новой переменной для получения послания в одну строку
new_list_join = ' '.join(new_letter)
print(new_list_join)

user_input = input('\nДля выхода из программы нажмите Enter!')
