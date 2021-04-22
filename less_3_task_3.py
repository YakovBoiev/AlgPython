"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


import random

SIZE = 10
MIN_NUM = - 100
MAX_NUM = 100
test_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(test_array)

index_min = 0
min_el = test_array[0]
index_max = 0
max_el = test_array[0]
for index, value in enumerate(test_array):
    if value > max_el:
        max_el = value
        index_max = index
    if value < min_el:
        min_el = value
        index_min = index
test_array[index_min], test_array[index_max] = test_array[index_max], test_array[index_min]
print(test_array)
