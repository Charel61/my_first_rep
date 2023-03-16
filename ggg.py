from classes___1 import User
def get_user_info(user: User):
    return f'Возраст пользователя {user.name} - {user.age}',\
        f'a e-mail - {user.email}'


user_1: User = User(42, 'Vasiliy',23,'vasya@mail.ru')
print(get_user_info(user_1))
