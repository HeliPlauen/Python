
# Using args
def test(*args):
    print(args)

test(1, 2, 3, 4, 5)   # Create function with 5 arguments

a=[1, 2, 3]           # Using list for arguments

test(a)               # Here we have only 1 argument (list)
test(a, a)            # Here we have only 2 arguments (both lists)
test(*a)              # Unpack list and turn it into 3 arguments



# Using kwargs
def test2(**kwargs):
    print(kwargs)

a = {"1": "1"}         # Using dictionary for arguments

test2(**a)             # Unpack dictionary 



# Using args and kwargs
def test3(*args, **kwargs):
    print(kwargs)

a = {"1": "1"}         # Using dictionary for arguments

test3(1, **a)          # Unpack dictionary 
test3(1, a)            # DO NOT Unpack dictionary 

b = {"2": "2"}

test3(5, 6, **a, **b)  # !!!!!!