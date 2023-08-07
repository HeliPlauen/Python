
class T0:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        pass


class T:
    def __init__(self, name):
        self.name = name

a = T("Alex")

exm = T.__new__(T)   # Here we omit __init__ method
print(exm)


# -------------------------------------------------------------------------------------
# Use metaclasses!!!

class Singleton(type):    # It can exist the only this class object
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Python 2
"""
class Logger(object):
    __metaclass__ = Singleton
"""

# Python 3
class Logger(metaclass=Singleton):
    pass

a = Logger()
b = Logger()
print(a)       # The same object!!!
print(b)       # The same object!!!

# No Singleton!!!!
class Logger():
    pass

a = Logger()
b = Logger()
print(a)       # Different!!!
print(b)       # Different!!!


# -------------------------------------------------------------------------------------
# Inherit class!!!

class Singleton(object):    # It can exist the only this class object
    _instances = {}
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]

class Logger(Singleton):
    pass

a = Logger()
b = Logger()
print(a)       # The same object!!!
print(b)       # The same object!!!


# -------------------------------------------------------------------------------------

class Example:
    def __new__(cls, *args, **kwargs):
        print(f"{cls=}")
        return super(Example, cls).__new__(cls)

    def __init__(self, name):
        self.name = name
        print(f"{self.name=}")

a = Example("Alex")


# -------------------------------------------------------------------------------------

class Example(tuple):    
    def __new__(cls, urls):
        urls_tuple = tuple(f"http://{url}" for url in urls)
        return super().__new__(cls, urls_tuple)

    def __init__(self, urls):
        for num, url in enumerate(urls):
            self.num = f"http://{url}"
        print(self)

a = Example(['doamin.com', 'example.com'])
print(f"{a=}")