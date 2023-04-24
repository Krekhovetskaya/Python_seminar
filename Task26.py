# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a = int(input("Введите число "))
# b = int(input("Введите степень числа(целое неотрицательно число) "))

# def a_pow_b(a, b):
#     if b == 0:
#         return 1

#     return a * a_pow_b(a, b - 1)

# print(a_pow_b(a, b))


a = int(input("Введите число "))
b = int(input("Введите степень числа "))

def a_pow_b(a, b):
    if b == 0:
        return 1
    if b < 0:
        return (1/a) * a_pow_b(a, b + 1)
    return a * a_pow_b(a, b - 1)

print(a_pow_b(a, b))


