# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите количество элементов списка: '))
str = input("Введите через пробел элементы списка: ").split()
list = []
for i in str:
    list.append(int(i))
x = int(input('Введите число x, которое необходимо найти в списке: '))
count = 0
for i in range(n):
    if x == list[i]:
        count += 1
print(f'Число {x} встречается в списке {count} раз')