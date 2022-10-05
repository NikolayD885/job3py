# Задайте рандомно список из чисел размером N, где N число с клавиатуры.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random

n = int(input("Введите размер списка: "))
ListA = []

def FillArray(List):
    for i in range(n):
        List.append(random.randint(-10, 10))
    return List

FillArray(ListA)

summ = 0
for i in range(1, len(ListA), 2):
    summ += ListA[i]

print(F"{ListA}  сумма элементов на нечётных позициях: {summ}")
