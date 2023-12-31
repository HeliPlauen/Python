# chars = []
# for char in "abcde":
#     chars.append(char)
# print(chars)
chars = [char for char in "abcde"]
print(chars)

names = ['make', 'john', 'sally']
capitalized_names = [name.capitalize() for name in names]
print(capitalized_names)

numbers = [1, 2, 3, 4, 5, 6]
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

# unique_values = set()
# for value in [1, 3, 5, 5, 2, 2, 1, 7]:
#     unique_values.add(value ** 2)
# print(unique_values)
unique_values = {value ** 2 for value in [1, 3, 5, 5, 2, 2, 1, 7]}
print(unique_values)

# name_age_dict = {}
# data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
# for v in data:
#     name_age_dict[v.split('_')[0]] = v.split('_')[1]
# print(name_age_dict)
data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
print(name_age_dict)

values_squares = {value: value ** 2 for value in range(10)}
print(values_squares)

m = tuple(n for n in range(12))
print(m)

