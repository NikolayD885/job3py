# Напишите программу, которая найдёт произведение пар чисел списка (Список создаем как в предыдущем задании).
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
#         [2, 3, 5, 6] => [12, 15]


import random

n = int(input("Введите размер списка: "))
ListA = []


def FillArray(List):
    for i in range(n):
        List.append(random.randint(-10, 10))
    return List


FillArray(ListA)

if len(ListA) % 2 == 0:
    n = len(ListA) // 2
else:
    n = len(ListA) // 2 + 1

ListB = []

for i in range(n):
    ListB.append(ListA[i]*ListA[-i - 1])

print(F"Созданный список {ListA} произведение пар чисел списка {ListB}")
