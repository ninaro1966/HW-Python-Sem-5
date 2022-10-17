# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
line1 = input("Введите текст через пробел:\n")
print(f"Исходный текст: {line1}")
find_line2 = "абв"
lst = [i for i in line1.split() if find_line2 not in i]
print(f'Результат: {" ".join(lst)}')
# ЗАГОТОВКА ДЛЯ ДЗ  СЛЕДУЮЩЕГО СЕМИНАРА
# line1 = 'Дети любятабв играть абвс буквами в "абвгд-ейку"'
# def del_some_words(line1):
#     line1 = list(filter(lambda x: 'абв' not in x, line1.split()))
#
#     return " ".join(line1)
#
# line1 = del_some_words(line1)
# print(f'Результирующая строка:{line1}')
