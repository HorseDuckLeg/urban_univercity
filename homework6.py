#работа со словарями
my_dict = {'Вася': 1974, 'Петя': 1985, 'Игорь': 1999, 'Юля': 1990}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Юля'])
print('Not existing value: ', my_dict.get('Жора'))
my_dict.update({'Маша': 2001,
               'Кристина': 2002})
pop_1 = my_dict.pop('Игорь')                               #забираем из словаря ключ и его значение и отдаём эти данные переменной
print('Deleted value: ', pop_1)                            #выводим значение забранного из словаря ключа на экран
print('Modified dictionary: ', my_dict)
#работа с множествами
my_set = {1, 2, 3, 4, 5, 6, 8, 1, 4, 3, 2, 6, 9, 5, 1, 4, 3, 6, 9, 'текст', 5.2, 'еще текст', 5.2, True, (1, 2, 3)}
print('Set: ', my_set)
my_set.update([7, 0, 'NEW TEXT'])
print('Modified set: ', my_set)

