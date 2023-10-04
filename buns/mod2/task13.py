input_data = input()
a, b = 0, 0
for char in range(0, len(input_data), 2):
    a += int(char)

for char in range(1, len(input_data), 2):
    b += int(char)

if ((a + b * 3) % 10 == 0):
    print('yes')
else:
    print('no')