def get_armstrong_numbers():
    num = 150
    while True:
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        if num == sum:
            yield num
        num += 1


temp = get_armstrong_numbers()

for _ in range(1000):
    print(next(temp), end=' ')
