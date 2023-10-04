input_str = input()
a_str, b_str = '', ''

flag = False
for char in input_str:
    if char == ',':
        flag = True
    elif not flag:
        a_str += char
    else:
        b_str += char

a = float(a_str)
b = float(b_str)

remainder = a % b

print(remainder)