"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква
"""

print('Введите номер буквы в алфавите')
num = int(input())
if num < 1 or num > 26:
    print('Буквы с данным номером в алфавите нет')
else:
    shift = ord('a') - 1
    let = chr(num + shift)
    print(f'Под номером {num} в алфавите буква - {let}')
