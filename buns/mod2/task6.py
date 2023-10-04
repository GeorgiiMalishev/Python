data = input()
current_domain = ''
result = ''
for char in data:
    if char == '.':
        result = current_domain + '\n' + result;
        current_domain = ''
    else:
        current_domain += char
result = current_domain + '\n' + result;
print(result)