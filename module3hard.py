data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
#типы данных:
# list
# tuple
# dict
# set
# int
# str
result = 0


def calculate_structure_sum(*data_structure):
    global result
    #if isinstance(k)
    for i in data_structure:
        print(type(i))
        if isinstance(i, list) or isinstance(i, tuple):  # проверяем, является ли элемент данных списком, кортежем
            for k in i:
                return calculate_structure_sum(k)
        else:
            if isinstance(i, str):  # проверяем, явзяется ли значение строкой
                result += len(i)
            else:
                if isinstance(i, int):  # проверяем, явзяется ли значение числом
                    result += i
                else:
                    continue
    return result






result = calculate_structure_sum(*data_structure)
print(result)
            if isinstance(i, dict):  # проверяем, является ли элемент словарём.
                for key in i:
                    key_value = i[key]  # получаем значение каждого ключа из словаря
                    if isinstance(key, str):
                        result += len(key)
                    elif isinstance(key, int):
                        result += key
                    else:
                        continue
                    if isinstance(key_value, str):
                        result += len(key_value)
                    elif isinstance(key_value, int):
                        result += key_value
                    else:
                        continue