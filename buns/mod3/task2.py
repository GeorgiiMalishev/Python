num = int(input())
print("Неверный ввод" if num < 0 else " ".join([bin(num), oct(num), hex(num)]))