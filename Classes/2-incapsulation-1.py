
# Incapsulation
class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # Using simple functions
    def get_age(self):
        return self.__age

    def set_age(self, number):
        if number >= 0:            
            self.__age = number
            print(f"Age changed: {self.__age}")
        else:
            print(f"Age was not changed: {self.__age}")

    # Using decorators
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, number):
        if number >= 0:            
            self.__age = number
            print(f"Age changed: {self.__age}")
        else:
            print(f"Age was not changed: {self.__age}")


# Using simple functions
user1 = User("Oleg", 41)
print(user1.name)
print(user1.get_age())
user1.set_age(42)
print(user1.get_age())
user1.set_age(-2)
print(user1.get_age())

# Using standart decorators @
user2 = User("Yaroslava", 10)
print(user2.name)
print(user2.age)
user2.age = 11
print(user2.age)
user2.age = -1
print(user2.age)
