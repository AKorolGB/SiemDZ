# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
n = int(input('vvedite czislo N '))
k = 0
two = 1
while two <= n:
    k = k + 1
    two = 2 ** k

    print(two)

