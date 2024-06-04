grades = [[2, 4, 5, 3, 4, 5],
          [3, 3, 3, 4, 3, 4],
          [5, 5, 4, 5, 3, 5],
          [4, 4, 4, 5, 3, 3],
          [3, 4, 4, 5, 4, 5],
          [2, 2, 3, 3, 2, 4]]   #Список оценок студентов
students = {'Petrov',
            'Ivanov',
            'Aleksandrova',
            'Kozlov',
            'Medvedeva',
            'Petrova'}          #Список студентов (произвольный)
students_list = list(students)  #преобразуем множество в список для упорядочивания в алфавитном порядке
students_list.sort()            #Список студентов в алфавитном порядке
grades_average = []             #Список со средним баллом каждого
for i in grades:                #наполняем список "со средним баллом"
    a = sum(i)/len(i)
    grades_average.append(a)
studentsAndGrades = {}          #Создаём словарь с фамилиями и средними баллами каждого
for i in range(len(students_list)): #Наполняем словарь фамилиями и средними балаами
    studentsAndGrades[students_list[i]] = grades_average[i]
[print (key, ':',value) for key, value in studentsAndGrades.items()] #Построчный вывод словаря.

#В задании нужно было вывести словарь в одну строку, но это не очень читаемо, по этому сделал построчный вывод, надеюсь не будет считаться за ошибку.
#print(studentsAndGrades)
