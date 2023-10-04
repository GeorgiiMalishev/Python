input_data = input()
i, n = "", ""
flag = False
for char in input_data:
    if char == ',':
        flag = True
    elif not flag:
        i += char
    else:
        n += char
n = int(n)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index_i = alphabet.index(i)
shifted_index = (index_i + n) % 26
print(alphabet[shifted_index])
