def get_multiplied_digits(number):
    str_number = str(number)            #переводим значение number из числового в строковое
    first = int(str(str_number[0]))     #забираем первый символ из str_number
    len_number = len(str_number)        #измеряем количество цифр в нашем числе
    if len_number == 1:                 #если число состоит из одной цифры, выводим сразу это число
        return first
    else:                               #рекурсивно вычисляем произведение  всех цифр числа
        return first * get_multiplied_digits(int(str_number[1:]))




print(get_multiplied_digits(40203))
print(get_multiplied_digits(3))
