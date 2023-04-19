# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка
# содержит число X

n = int(input('Введите количество элементов списка: '))
str = input("Введите через пробел элементы списка: ").split()
list = []
for i in str:
    list.append(int(i))
x = int(input('Введите число x, c которым нужно сравнить элементы в списке: '))
dif_min = abs(x - list[0])
close_element = list[0]
for item in range(n):
    if list[item] == x:
        break
    if abs(x - list[item]) < dif_min:
        dif_min = abs(x - list[item])
        close_element = list[item]
print(f'Самый близкий по величине элемент {close_element}')
