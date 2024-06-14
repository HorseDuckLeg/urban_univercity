#Диапазон чисел для сверки от 3 до 20
#для числа 9 из первой вставки пароль:
#1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
#first_insert - первая вставка
#first_insert_fu - функция для отпределения случайного числа первой вставки в диапазоне 3-20
#pair_part_1 - числовой ряд от 1 до случайного числа из первой вставки
#pair_part_2 - список пар во второй вставке
#password - пароль для числа из первой вставки
#result - результат

import random


def first_insert_fu():
    first_insert_range = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    first_insert = random.choice(first_insert_range)
    return first_insert


n = first_insert_fu()
#print('Число из первой вставки: ', n)
pair_part_1 = []
pair_part_2 = []
password = []
for c in range(1, n + 1):
    pair_part_1.append(c)
    #print('pair_part_1', pair_part_1)
for i in pair_part_1:
    if i <= ((n / 2) + 1):
        for j in pair_part_1:
            if j >= i:
                if n % (i + j) == 0:
                    pair_part_2.append(i)
                    pair_part_2.append(j)
                    #print('pair_part_2', pair_part_2)
                else:
                    #print('Сумма не кратна', n)
                    continue

print(n, ' - Число из первой вставки')
#print('список для перебора от 1 до числа из первой вставки:', pair_part_1)
#print('список пар сумма которых кратна числу из первой вставки:', pair_part_2)
password = (pair_part_2)
print(password)
result = "".join(str(i) for i in password)
print('Нужный пароль:', result)
