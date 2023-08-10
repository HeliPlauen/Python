
# Parent class
class Cat:

	def __init__(self, color, cat_type):
		self.color = color
		self.cat_type = cat_type
		self.size = self.set_size()

	def set_size(self):
		if self.cat_type == "indoor":
			self.size = "small"			
		else:
			self.size = "undefined"
		return self.size


cat1 = Cat("red", "indoor")
print(cat1.set_size())

cat2 = Cat("black", "street")
print(cat2.set_size())


# Child class
class Tiger(Cat):
	def set_size(self):
		if self.cat_type == "wild":
			self.size = "big"			
		else:
			self.size = "undefined"
		return self.size


tiger1 = Tiger("orange", "wild")
print(tiger1.set_size())

tiger2 = Tiger("orange", "homestic")
print(tiger2.set_size())