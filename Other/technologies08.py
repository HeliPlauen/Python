
# Make sum lists

values = [[1, 2], [3], [4, 5], [6, 7, 8, 9]]
print(sum(values, []))


import itertools

values = [[1, 2], [3], [4, 5], [6, 7, 8, 9]]
print(list(itertools.chain.from_iterable(values)))