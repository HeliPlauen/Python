
# Pretty print

from pprint import pprint


user = {"result":[{"gender":"male", "name":{"title":"Mr", "first":"Justin", "last": "Oliver"}, "location":{"street":"Charles_de_Gaull", "city": "Paris"}},]}

print(user)
pprint(user)