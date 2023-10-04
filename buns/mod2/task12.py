input_data = input()

data = ''
for char in input_data:
    if char not in ' ()-':
        data += char
print(data)