"""Задача 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""

# text = input()
#
# text = list(filter(lambda el: "абв" not in el.lower(), text.split()))
# print(" ".join(text))


"""Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных."""

with open('decoded.txt', 'r') as data:
    my_text = data.read()

# text = "HHHHHHHHjKKKKKKKKKjllllll "
def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(my_text)
print(str_code)

with open('encoded.txt', 'r') as data:
    my_text2 = data.read()


def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(str_code)
print(str_decode)

