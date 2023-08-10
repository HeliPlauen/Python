
# Polymorpysm
class User:
    def __init__(self, name, age, user_type):
        self.__name = name
        self.__age = age
        self.__user_type = user_type

    def access_database(self):
        pass


class SuperUser(User):
    def access_database(self):
        return "access granted"


class SimplerUser(User):
    def access_database(self):
        return "access denies"


super = SuperUser("Oleg", 41, "superuser")
simple = SimplerUser("Murka", 3, "simpleuser")

for user in (super, simple):
    print(user.access_database())


