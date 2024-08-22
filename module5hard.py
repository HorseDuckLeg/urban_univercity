import hashlib
import time

class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, age, hash_password):
        self.data[username] = [hash_password, age]
        #self.data[username] = age
        #self.data[username] = hash_password


class User:
    """""
    Класс пользователя, содержащий атрибуты: логин, пароль
    """""

    def __init__(self, username, password, password_confirm, age):
        self.username = username
        if password == password_confirm:
            self.password = password
        self.age = age

    def __hash__(self):
        return hash((self.password))


class Video:
    """""
    Класс видео, содержащий атрибуты: Заголовок, продолжительность видео, секунда остановки, а так же ограничением по 
    возрасту для конкретного видео
    """""


    def __init__(self, title, duration, adult_mode):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


    def time_now(self):
        time_now_sec = 0
        time_now_min = 0
        time_now_hour = 0
        while True:
            time_now_sec += 1
            time.sleep(1)
            # if time_now_sec = 60
            #     time_now_min =+ 1
            #     time_now_sec = 0
            #     if time_now_min = 60
            #         time_now_hour += 1
            #         time_now_min = 0





if __name__ == '__main__':
    #user = User(alex, qwerty123, qwerty123, 23)
    #print('the hast is: %d' %hash(user))

    database = Database()
    while True:
        choise = int(input('Для авторизации выберите действие: \n1 - Вход\n2 - Регистрация\n'))
        if choise ==1:
            login = input('Введите логин: ')
            password = input('Введите пароль:')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Добро пожаловать', {login})
                    break
                else:
                    print('Наверный пароль.')
            else:
                print('Пользователь не найден')
        if choise == 2:
            user = User(input('name: '), password := input('pass: '), password_confirm := input('confirm: '),
                        input('age: '))
            if password != password_confirm:
                print('Пароли не совпадают, попробуйте еще раз.')
                continue
        database.add_user(user.username, user.age, user.__hash__())
        print(database.data)

        print('the hast is: %d' % hash(user))

    
