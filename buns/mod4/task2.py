def power(a, n):
    if a == 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 0:
        return power(a * a, n / 2)
    return a * power(a, n - 1)


print(power(int(input()), int(input())))
