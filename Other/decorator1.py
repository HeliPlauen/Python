
def decorate(func):
	def wrapper():
		print("wrapper")
		func()
	return wrapper


# test = decorate(test)
@decorate
def test():
	print("test")


test()