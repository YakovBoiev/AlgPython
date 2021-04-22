"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""
import random

SIZE = 3
MIN_NUM = -100
MAX_NUM = 100

test_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(test_array)

for index, value in enumerate(test_array):
    if value < 0:
        max_neg_el = value
        index_neg_max = index
        for i in range(index + 1, len(test_array)):
            if 0 > test_array[i] > max_neg_el:
                max_neg_el = test_array[i]
                index_neg_max = i
        print(f'Максимальный отрицательный элеметн {max_neg_el} позиция {index_neg_max}')
        break
else:
    print("В массиве нет отрицательных элементов")
