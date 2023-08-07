# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randrange

first_value = int(input("Insert 1: "))
second_value = int(input("Insert 2: "))

a = [randrange(1, 10) for i in range(1, 10)]
print(a)
b = []
for i in a:
    if i >= first_value and i <= second_value:
        b.append(i)
    elif i <= first_value and i >= second_value:
        b.append(i)
    i += 1

print(b)