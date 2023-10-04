input_data = input()

data = ''
for char in input_data:
    if char != ' ':
        data += char

temp_data = data
flag = False
for char in data:
    temp_data = temp_data[1::]
    if char in temp_data:
        flag = True
        break
print(flag)