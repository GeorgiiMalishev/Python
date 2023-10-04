data = input()
result = ''
i = 0
for char in data:
    if char == ' ':
        result += data[i-1]
    i += 1
result += data[i-1]
print(result)