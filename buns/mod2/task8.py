input_data = input()
s, i = "", ""
flag = False
for char in input_data:
    if char == ',':
        flag = True
    elif not flag:
        s += char
    else:
        i += char

count = 0

for char in s:
    if char == i:
        count += 1
    else:
        break

print(count)