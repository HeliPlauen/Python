
# Generator

def generator():
    num = 5                  # Returns when called for the 1-st time
    while True:
        resp = (yield num)   # Returns num and get the new value
        if resp:
            num = resp       # Check and save the new value in num


a = generator()
print(next(a))

a.send(200)
print(next(a))

a.send(300)
print(next(a))
