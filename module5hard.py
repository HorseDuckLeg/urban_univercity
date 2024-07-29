class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password



class User:
    """""
    Класс пользователя, содержащий атрибуты: логин, пароль
    """""
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password



if __name__ == '__main__':
    database = Database()
    while True:
        user = User(input("Введите логин: "), password := (input("Введите пароль: "), password_confirm := input("Введите подтверждение пароля: "))
        if password != password_confirm:
            print('Пароли не совпадают.')
            exit()
        database.add_user(user.username, user.password)
        print(database.data)


    
