import math

TEST_CONSTANT = 1  # For constants

value1 = {'tes': 1, 'key': 2, 'value': 3}
value2 = [1, 2, 3, 4]
value3 = pow(2, 10)


class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """Returns full name of user using first_name, last_name concat."""
        return ''.format(self.first_name, self.last_name)

    def short_name(self):
        """
        Returns short name of user using first_name, last_name's first letter.
        Example:
            >>> self.short_name()
        :return: str - concatenated first and last names
        """
        return ''.format(self.first_name, self.last_name[0])

    def send_mail(self):
        """instance.send_mail() -> list"""
        return ''.format(self.first_name, self.last_name[0])


tuple1 = (1,)  # without whitespace
tuple2 = (1,)  # without whitespace

result1 = '1234567'[1:3]
#result2 = '1234567'[1 : 3]
result3 = '1234567'[1 + tuple1[0] : 5 + 10]


user1 = User('t1', 't2')
user1.send_mail()
value1['key'] = tuple1[0]


def test_function(argument: str) -> str:
    return argument[:10]


value4 = dict(t=1, p=2)

if value4['t'] == 1: 
    test_function('*' * 10)

# test_function('0' * 10); test_function('+' * 10); test_function('-' * 10)
test_function('0' * 10) 
test_function('+' * 10) 
test_function('-' * 10)


values = [
    1, 
    902, 
    312, 
    431, 
    521, 
    619, 
    722, 
    8209, 
    912
]


class SuperInstructor:

    def test_name(self):
        pass

    def test_name_value(self):
        pass

    def test_name_value1(self):
        pass

    def test_name_value2(self):
        pass


def foo(x):
    if x >= 0:
        return math.sqrt(x)
    return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

"""
if type(value1) is type(value2):
    print('Done')
"""

if isinstance(value1, int) and isinstance(value2, int):
    print('Done')
