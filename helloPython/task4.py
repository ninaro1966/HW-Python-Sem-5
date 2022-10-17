# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные  Пример:
#данные хранятся в отдельных текстовых файлах.
# На сжатие входные данные:  aaaaaaabbbbbbcccccccccd
# Выходные данные:7a6b9c1d

with open('file.txt', 'w') as data:
    data.write('aaaaaaaaaaabbbcccccccd')

with open('res.txt', 'r') as data:
    string = data.read()

def rle_encode(decoded_string):
    encoded_string = ''
    quantity = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            quantity += 1
        else:
            encoded_string = encoded_string + str(quantity) + char
            char = decoded_string[i]
            quantity = 1
            encoded_string = encoded_string + str(quantity) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i]. isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
            char_amount = ''
    print(decoded_string)

    return decoded_string

with open('file.txt', 'r') as data:
    decoded_string = data.read()

with open('res.txt', 'w') as data:
    encoded_string = rle_encode(decoded_string)
    data.write(encoded_string)

print('Длинная строка:\t' + decoded_string)
print('Сжатая строка: \t' + rle_encode(decoded_string))

