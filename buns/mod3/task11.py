first_line = input()
k = len(first_line)
matrix = [['' for _ in range(k)] for _ in range(k)]
matrix[0] = list(first_line)

for i in range(1, k):
    input_line = input()
    matrix[i] = list(input_line)

result = ''

for i in range(k):
    if all(matrix[i][j] == 'X' for j in range(k)):
        result = 'X'
    elif all(matrix[i][j] == 'O' for j in range(k)):
        result = 'O'
    elif all(matrix[j][i] == 'X' for j in range(k)):
        result = 'X'
    elif all(matrix[j][i] == 'O' for j in range(k)):
        result = 'O'

if all(matrix[i][i] == 'X' for i in range(k)) or all(matrix[i][k - i - 1] == 'X' for i in range(k)):
    result = 'X'
if all(matrix[i][i] == 'O' for i in range(k)) or all(matrix[i][k - i - 1] == 'O' for i in range(k)):
    result = 'O'

print(result)
