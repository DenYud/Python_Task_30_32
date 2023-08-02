# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите второй элемент: "))
n = int(input("Введите третий элемент: "))

progr = []
for i in range(n):
    ai = a1 + (i * d)
    progr.append(ai)
for element in progr:
    print(element)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)

def find_index(array, min, max):
    res = []
    for i in range(len(array)):
        if max >= array[i] >= min:
            res.append(i)
    return res


arr = [-5, 9, 0, 3, -1, -2, 1, 4, 2, 6, -4, 5, 6]

print(find_index(arr, 5, 10))
