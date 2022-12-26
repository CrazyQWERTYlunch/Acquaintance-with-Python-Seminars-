"""Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции."""

# def Sum_odd(list):
#     sum = 0
#     i = 1
#     while i <= len(list) - 1:
#         sum += list[i]
#         i += 2
#     return sum
#
# print(Sum_odd(list(map(int, input("Введите через пробел значения элементов списка: ").split()))))

"""Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д."""
# import random
# import math
#
# size = int(input("Введите желаемую длину списка: "))
#
# test_list = [random.randint(-100, 100) for i in range(size)]
# new_list = [test_list[i] * test_list[- i - 1] for i in range(math.ceil(len(test_list)/2))]
#
# print(test_list)
# print(new_list)

# new_list = [round(i % 1, 2) for i in test_list if i % 1 != 0]
# print(max(new_list) - min(new_list))
"""Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов."""

# test_list = list(map(float, input("Введите через пробел значения элементов списка: ").split()))
#
# new_list = [round(i % 1, 2) for i in test_list if i % 1 != 0]
#
# # print(test_list)
# # print(new_list)
#
# print(f"Разница между максимальным и минимальным значением дробной части элементов составляет {max(new_list) - min(new_list)}")

"""Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное."""

# def binary_conversion(number):
#     result = ''
#     while number != 0:
#         result += str(number % 2)
#         number //= 2
#     return result
#
# number = int(input("Введите число для преобразовывания десятичного числа в двоичное: "))
#
# print(binary_conversion(number))

"""Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов."""


n = int(input('Введите число: '))

def fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums


fibo_nums = fibonacci(n)
print(fibo_nums)
