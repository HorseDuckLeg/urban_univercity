def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



# 1 задание:
print_params()
print_params(b = 25, c = [1, 2, 3])

# 2 задание:
values_list = [1, '2.5', True]
values_dict = {'a' : 3, 'b' : 'строка', 'c' : False}
#print(values_dict)
print_params(*values_list)
print_params(**values_dict)

# 3 задание:
values_list_2 = [54.32, 'СТРОКА']
print_params(*values_list_2, 42)
