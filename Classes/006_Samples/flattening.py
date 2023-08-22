# matrix = []
# for i in range(3):
#     numbers = []
#     for j in range(2):
#         numbers.append(j)
#     matrix.append(numbers)
matrix = [[j for j in range(2)] for i in range(3)]
print(matrix)

# flatten_matrix = []
# for sublist in matrix:
#     for number in sublist:
#         flatten_matrix.append(number)
flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
