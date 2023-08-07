
# Reload operators

class Summary:
    def __init__(self, number):
        self.__number = number

    def __gt__(self, other):                     # operator >
        return self.__number > other.__number

    def __lt__(self, other):                     # operator <
        return self.__number < other.__number

    def __eq__(self, other):                     # operator ==
        return self.__number == other.__number

a = Summary(10)
b = Summary(20)

print(a > b)
print(a < b)
print(a == b)

# __mul__
# __add__
# __sub__