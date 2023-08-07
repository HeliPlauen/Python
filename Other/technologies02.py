
# Reloaduing p=operators

from functools import total_ordering


@total_ordering
class Euro:
    """
    Class the has to define one of:
    __lt__(), __le__(), __gt__() or __ge__()

    Besides, the class has to give __eq__() method
    """

    def __init__(self, value:int):
        self.__value = value

    # Orerator == 
    def __eq__(self, other):
        return self.__value == other.__value

    # Operator > (>==, <, <== class will define by itself using total_ordering)
    def __gt__(self, other):
        return self.__value > other.__value

    def hyperinflation(self):
        self.__value = 0


a = Euro(100)
b = Euro(200)

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

a.hyperinflation()
b.hyperinflation()
print(a == b)
