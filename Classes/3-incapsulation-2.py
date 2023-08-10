
# Polymorphysm
class User:
    def __init__(self, name, age, user_type=None):
        self.__name = name
        self.__age = age
        self.__user_type = user_type

    def access_database(self):
        if self.__user_type == "superuser":
            print("access granted")
        else:
            print("access denies")


class SuperUser(User):
    def access_database(self):
        print("access granted")         


super = SuperUser("Oleg", 41)
user1 = User("Yaroslava", 10, "superuser")
user2 = User("Murka", 3, "simpleuser")

for usr in (super, user1, user2):
    usr.access_database()


