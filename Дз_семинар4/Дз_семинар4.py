"""Задача 1. Вычислить число c заданной точностью d"""
# # Сделано на примере числа Пи
# import math
# number = input("Введите заданную точность числа: ")
#
# if not number.isdigit(): # Если вводится вещественное число - 0.001 и подобные
#     number_acc = len(number[number.find(".") + 1: ])
#     print(f"Число {math.pi} с заданной точностью равно {round(math.pi,number_acc)}")
# else: print(f"Число {math.pi} с заданной точностью равно {round(math.pi, int(number))}") # Для целых чисел

"""Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N."""


# def primfactors(n):
#     prime_fact = list()
#     divider = 2
#     while divider <= n:
#         if n % divider == 0:
#             prime_fact.append(divider)
#             n //= divider
#         else:
#             divider += 1
#     return prime_fact
#
# n = int(input("Введите натуральное число: "))
#
# print(f"Простыми множителями числа {n} являются {primfactors(n)}")

"""Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности."""
#
# def unique_numbers(seqnum):
#    uninum = list()
#    [uninum.append(seqnum[i]) for i in range(len(seqnum)) if seqnum.count(seqnum[i]) == 1]
#    return uninum
#
# seqnum = list(map(int,input("Введите последовательность чисел: ").split()))
#
# print(unique_numbers(seqnum))

#
# import random
# import itertools
#
# k = random.randint(2,7)
#
# def get_coefficients(k):
#    ratios = [random.randint(0,100) for i in range(k+1)]
#    return ratios
#
# def get_polynomial(k, ratios):
#    line = ['*x^'] * (k - 1) + ['*x']
#    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, line, range(k, 1, -1), fillvalue='') if a != 0]
#    for x in polynomial:
#       x.append(' + ')
#    polynomial = list(itertools.chain(*polynomial))
#    polynomial[-1] = ' = 0'
#    return "".join(map(str, polynomial)).replace(' 1*x', ' x')
#
#
# ratios = get_coefficients(k)
# polynomial = get_polynomial(k, ratios)
# print(polynomial)
#
# with open('К_4_заданию.txt', 'w') as file:
#    file.write(polynomial)
"""Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
записать в файл многочлен степени k."""


"""Задача 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов."""

# def get_polymonial(file):
#     with open(str(file),"r") as data:
#         poly = data.read()
#         return poly
#
# pol1,pol2 = get_polymonial("Задание_5_poly1.txt"),get_polymonial("Задание_5_poly2.txt")
#
#
# with open("Задание_5_poly_sum.txt", "w", encoding='utf-8') as file:
#     file.write(f"{pol1} + {pol2}")
#
# sum_of_poly = get_polymonial("Задание_5_poly_sum.txt")

import itertools

file1 = 'Задание_5_poly1.txt'
file2 = 'Задание_5_poly2.txt'

def get_polynomial(k, ratios):
   line = ['*x^'] * (k - 1) + ['*x']
   polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, line, range(k, 1, -1), fillvalue='') if a != 0]
   for x in polynomial:
      x.append(' + ')
   polynomial = list(itertools.chain(*polynomial))
   polynomial[-1] = ' = 0'
   return "".join(map(str, polynomial)).replace(' 1*x', ' x')

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def convert_pol(pol):
    pol.replace('= 0', '')
    pol = pol.split(' + ')
    pol = [i[0] for i in pol]
    for i in range(len(pol)):
        if pol[i] == 'x':
            pol[i] = '1'
    pol = pol[::-1]
    return pol

pol1 = read_pol(file1)
pol2 = read_pol(file2)

pol1_coef = list(map(int, convert_pol(pol1)))
pol2_coef = list(map(int, convert_pol(pol2)))

sum_coef = list(map(sum, itertools.zip_longest(pol1_coef, pol2_coef, fillvalue=0)))

sum_coef = sum_coef[::-1]

sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
print('Итоговый результат сложения полиномов: ', sum_pol)
with open('Задание_5_poly_sum.txt', 'w') as file_sum:
    file_sum.writelines(sum_pol)