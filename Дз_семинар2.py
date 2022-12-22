"""Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр."""

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

"""Задача 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N."""

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

"""Задача 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. """

# n = int(input('Введите количество чисел в списке: '))
#
# def sequence(n):
#     return [round((1 + 1 / x) ** x, 2) for x in range(1, n + 1)]
#
#
# print(sequence(n))
# print(round(sum(sequence(n)), 2))

"""Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
 Найдите произведение элементов на указанных позициях.
 Позиции хранятся в файле file.txt в одной строке одно число."""
# import random
#
# n = int(input("Введите количество чисел в списке: "))
#
# my_list = []
#
# for i in range(n):
#     my_list.append(random.randint(-n,n))
#
# pos_1 = random.randint(0, n-1)
# pos_2 = random.randint(0, n-1)
#
# # print(pos_1, pos_2)
# # print(my_list)
# print(my_list[pos_1] * my_list[pos_2])

"""Задача 5. Реализуйте алгоритм перемешивания списка."""
import random

n = list(map(int, input("Введите через пробел значения элементов списка: ").split()))
print(n)
def random_list(n):
    for i in range(len(n)):
        pos_1 = random.randint(0, len(n) - 1)
        pos_2 = random.randint(0, len(n) - 1)
        n[pos_1], n[pos_2] = n[pos_2], n[pos_1]
    return n
print(random_list(n))