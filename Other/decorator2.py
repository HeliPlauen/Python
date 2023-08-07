
def decorate(func):
	def wrapper(value):
		print("wrapper")
		func(value)
	return wrapper


# test = decorate(test)
@decorate
def test(value):
	print(f"test, value: {value}")


test("Value in test")