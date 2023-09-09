import math


# python example1_indentation.py

# Tab!!!
def foo(value):
	if value == 10:
		raise ValueError('Incorrect value: {}'.format(value))
	return pow(10, value)

# 4 spaces!!!
def bar(value):
    return pow(10, value)


print(foo(1))
print(foo(9))
print(foo(11))