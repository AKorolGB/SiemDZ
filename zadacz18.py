# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. В последующих  строках записаны N целых чисел
# Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
import random

list = []
n = int(input('Введите количество элементов в списке: '))
for i in range(n):
    list.append(random.randint(1, 100))
    i = i + 1
print(list)
given_number = int(input('Введите число: '))
difference_one = 0
difference_save = list[1] - given_number
search_element = list[1]
position = 0
for i in range(n):
    if given_number == list[i]:
        search_element = list[i]
        position = i
        break
    elif given_number > list[i]:
        difference_one = given_number - list[i]
    elif given_number < list[i]:
        difference_one = list[i] - given_number
    if difference_one <= difference_save:
        difference_save = difference_one
        search_element = list[i]
        position = i

    else:
        i = i + 1
print(f'Искомый элемент х={search_element} на позиция {position+1}')
