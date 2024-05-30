immutable_var = ('Кортеж', 1, 2, 3, 5.5, False)
print('Immutable tuple: ',immutable_var)
mutable_list = ["Список", 1,2,3,'a','b','c']
print('Mutable list before modified: ',mutable_list)
mutable_list.append('Modified')
mutable_list.extend('qwerty')
print('Mutable list after modified: ',mutable_list)
