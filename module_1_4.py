# Практическая работа по уроку "Организация программ и методы строк".
my_string = input('Введите текст: ')
character_count = len(my_string)
print('Количество символов введённого текста', character_count)
print('Верхний регистр: ', my_string.upper())
print('Нижний регистр: ', my_string.lower())
print('Удалены пробелы: ', my_string.replace(' ', ''))
print('Первый символ строки: ',my_string[0])
print('Последний символ строки: ',my_string[-1])