# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
n = int(input('Введите трехзначное чиcло:'))
if n/100>=1 and n/1000<1:
    s =(n//100) + ((n%100)//10) + ( n % 10)
    print(n)
    print(s)
else:
    print("Число не соответсвует условию")