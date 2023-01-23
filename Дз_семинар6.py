"""Семинар 2. Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр."""
# n = input()
#
# n = n.replace('-', '')
# n = n.replace('.', '')
# n = int(n)
# result = 0
#
# while n > 0:
#     result += n % 10
#     n = n // 10
#
# print(n)
# print(result)

"""NEW"""
n = input('Введите вещественное число: ')
new_sum = sum(map(int, n.replace('.', '')))
print (new_sum)

"""Задача 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""
#
# def find_sum(n):
#     if n == 1:
#         result.append(n)
#         return n
#     n = n * find_sum(n-1)
#     result.append(n)
#     return n
#
# n = int(input())
# result = []
#
# find_sum(n)
#
# print(result)

"""NEW"""
from math import factorial
n = int(input('Введите число: '))
print(list(map(lambda x: ((x == 1) and 1) or x * factorial(x -1),list(range(1,n+1)))))


"""Семинар 3. Задача 1. Задайте список из нескольких чисел.
 Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции."""

# def Sum_odd(list):
#     sum = 0
#     i = 1
#     while i <= len(list) - 1:
#         sum += list[i]
#         i += 2
#     return sum
#
# print(Sum_odd(list(map(int, input("Введите через пробел значения элементов списка: ").split()))))

"""NEW"""
my_list = list(map(int, input('Введите числа, через пробел: ').split()))
print(sum(my_list[1::2]))


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

"""NEW"""

number = int(input("Введите число для преобразования десятичного числа в двоичное: "))

binary = lambda n: n % 2
result = list()
while number != 0:
    result.append(str(binary(number)))
    number //=2
print("".join(result[::-1]))

