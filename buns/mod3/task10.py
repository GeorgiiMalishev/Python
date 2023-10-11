size = int(input())

matrix = [[1 + j for j in range(size)] for i in range(1, size + 1)]

for row in matrix:
    print(', '.join(map(str, row)))

print('\n')

for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(', '.join(map(str, row)))
