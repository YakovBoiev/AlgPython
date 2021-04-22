"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5,
(индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
"""

import random

SIZE = 10
MIN_EL = - 100
MAX_EL = 100
test_array = [random.randint(MIN_EL, MAX_EL) for _ in range(SIZE)]
print(test_array)

even_el_index = [index for index, value in enumerate(test_array) if value % 2 == 0]
print(even_el_index)
