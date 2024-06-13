#Диапазон чисел для сверки от 3 до 20
#для числа 9 из первой вставки пароль:
#1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
#first_insert - первая вставка
#second_insert - вторая вставка
#first_insert_fu - функция для отпределения случайного числа первой вставки в диапазоне 3-20
#pair_part_1 - первая часть пары
#pair_part_2 - вторая часть пары
#password - пароль для числа из первой вставки

import random


def first_insert_fu():
    first_insert_range = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    first_insert = random.choice(first_insert_range)
    return first_insert


print('Число из первой вставки: ', first_insert_fu())
pair_part_1 = []
pair_part_2 = []
#m = first_insert_fu()
for c in range(first_insert_fu()):
    a = c + 1  # присваиваем переменной число что бы начать перебор с 1 для первой части пары
    print('тест - выводим значение a:', a)
    pair_part_1.append(a)  # записываем число в первую часть пары
    print('числа из первой части парыЖ', pair_part_1)
    for i in range(first_insert_fu()):
        print('тест - выводим значение i:', i)
        if first_insert_fu() % (a + (i + 1)) == 0:
            print('Остаток от деления ноль, сумма пары кратна')
            b = (i + 1) #записываем значение второй части пары удовлетворяющее условиям кратности
            pair_part_2.append(b)
            print('числа из второй части пары: ', pair_part_2)
        else:
            print('Остаток от деления не равен нулю, либо первая часть пары больше половины числа нет смысла вести дальше перебор')
            continue
print(first_insert_fu())
print('список первой части пар:', pair_part_1)
print('список второй части пар:', pair_part_2)
for i in pair_part_1:
    password.append(i)
    for j in pair_part_2:
        if first_insert_fu() % (pair_part_1[i] + pair_part_2[j]):
            password.append(j)
        else:
            continue

print('Код для числа:', first_insert_fu(), ' : ', password)
