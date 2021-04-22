"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

list_num = [i for i in range(2, 10)]
for i in list_num:
    count = 0
    for j in range(2, 100):
        if j % i == 0:
            count += 1
    print(f'Числу {i} кратны {count} чисел')
