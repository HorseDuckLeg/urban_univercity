data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# типы данных:
# list
# tuple
# dict
# set
# int
# str
result = 0


def calculate_structure_sum(*data_structure):
    global result
    # if isinstance(k)
    for i in data_structure:
#        print(type(i))
        if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set):  # проверяем, является ли элемент данных списком/кортежем/множеством
            for k in i: #рекурсивно перебираем все элементы списка/кортежа/множества
                calculate_structure_sum(k)
        elif isinstance(i, dict):   #проверяем, является ли элемент словарём
            for k in i: #рекурсивно перебираем все элементы словаря вычленяя ключи и их значения
                value = i[k]
                calculate_structure_sum(k, value)
        else:
            if isinstance(i, str):  # проверяем, явзяется ли значение строкой
                result += len(i)
            elif isinstance(i, int):  # проверяем, явзяется ли значение числом
                result += i
    return result


result = calculate_structure_sum(*data_structure)
print('Сумма всех цифр и букв в списке =', result)

