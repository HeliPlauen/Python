
# Using templates in loops

some_tupples = [
    ((1, 2), 3), 
    ((4, 5), 6), 
    ((7, 8), 9)
]

for ((a, b), c) in some_tupples:
    print(a, b, c)


# Use map for turning list elements into string from int

some_list = [1, 2, 3]

print(', '.join(map(str, some_list)))


# Play with anagrams

from collections import Counter

print(Counter("test") == Counter("tets"))


# Rearrangement of values

data = [
    (1, 2), 
    (3, 4), 
    (5, 6)
]

print(*data)
result = zip(*data)
print(list(result))
