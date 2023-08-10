class Parallelogram:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_area(self):
        return self._width * self._length


p = Parallelogram(2, 3)
print(p.get_area())


class Square(Parallelogram):
    def get_area(self):
        return self._width * self._width


s = Square(2, 3)
print(s.get_area())


def function(data, new_value):
    if isinstance(data, list):
        data.append(new_value)
    elif isinstance(data, set):
        data.add(new_value)
    elif isinstance(data, str):
        if isinstance(new_value, str):
            data += new_value
    return data


print(function('{1, 5, 3}', '4'))
print(function(['1', '2'], '4'))
print(function({1, 2}, '4'))
