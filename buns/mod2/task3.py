flag1 = False
flag2 = False
input_str = input()

a_str, b_str, c_str = "", "", ""

for char in input_str:
    if char == ' ':
        if not flag1:
            flag1 = True
        else:
            flag2 = True
    elif not flag1:
        a_str += char
    elif flag1 and not flag2:
        b_str += char
    else:
        c_str += char

a = int(a_str)
b = int(b_str)
c = int(c_str)

if a == b or a == c:
    print(a)
elif b == c:
    print(b)
elif b < a < c or c < a < b:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else:
    print(c)
