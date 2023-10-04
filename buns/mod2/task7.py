data = input()
count0, count1 = 0, 0
for char in data:
    if char == '0':
        count0 += 1
    else:
        count1 += 1
if count1 == count0:
    print("yes")
else:
    print("no")