def euclidean_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclidean_gcd(b, a % b)


num1 = int(input())
num2 = int(input())

result = euclidean_gcd(num1, num2)
print(f"Наибольший общий делитель чисел {num1} и {num2} равен {result}")