
# The way to silence the basic Exceptions!!!

import sys


# The function does nthing and misses all the Exceptions
def exception_handler(exctype, value, traceback): ...
sys.excepthook = exception_handler      # Created our exception type (we call it every time when the exception occures)


# Variables contain Errors !!!
a = 1 / 0
b = blablabla() + 0x10 + test_funct()


# Class with errors !!!!
class Test:
    lambda x: ttt() - Test + sys


# The code works and does not break!!! The program ignores all the exceptions!!!!!