"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень
"""


def my_func(x, y):
    st = 1
    res = x
    while st < abs(y):
        res *= x
        st += 1
    return res
    # return x ** y


print(my_func(2, -100))
