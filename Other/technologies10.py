
# Unpack list into new variablees

seq = [1, 2, 3, 4]

*a, b, c = seq
print(a, b, c)

a, *b, c = seq
print(a, b, c)

a, b, *c = seq
print(a, b, c)

a, b, c, *d = seq
print(a, b, c, d)

a, b, c, d, *e = seq
print(a, b, c, d, e)


# Unpack tupples into new variablees

some_tupples = [
    (1, 2, 3), 
    (4, 5, 5, 1), 
    (6, 7, 8, 9, 0)
]

for (a, *b, c) in some_tupples:
    print(a, b, c)