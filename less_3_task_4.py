"""
Определить, какое число в массиве встречается чаще всего
"""


import random

SIZE = 10
MIN_NUM = -3
MAX_NUM = 2
test_array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(test_array)


list_numb = [test_array[0]]
list_count = [1]
for i in range(1, len(test_array)):
    for j in range(len(list_numb)):
        if list_numb[j] == test_array[i]:
            list_count[j] += 1
            break
    else:
        list_numb.append(test_array[i])
        list_count.append(1)
index_max = 0
max_list_count = list_count[0]
for i in range(1, len(list_count)):
    if max_list_count < list_count[i]:
        max_list_count = list_count[i]
        index_max = i
print(f'Чаще всего в массиве встречается число {list_numb[index_max]} ')
