class User():
    def __init__(self, name, is_admin = False):
        self.name = name
        self.is_admin = is_admin

def admin_only(func):
        def wrapper(user):
                if user.is_admin == True:
                    func(user)
                else:
                     raise PermissionError("Доступ запрещен! Только админ может выполнять эту операцию")
        return wrapper

@admin_only
def delete_database(user):
    print("База данных удалена!")

admin = User("Kana", is_admin = True)
user = User("Batyr", is_admin = False)
# delete_database(user)
delete_database(admin)