# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список
# должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
my_list = [i for i in range(100, 1000) if i % 2 == 0]


def my_func(list):
    res = 1
    for x in list:
        res = res * x
    print(res)


print(reduce(my_func, my_list))
