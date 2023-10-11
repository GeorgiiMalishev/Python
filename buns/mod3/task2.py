num = int(input())
print("Неверный ввод" if num <= 0 else ", ".join([bin(num)[2:], oct(num)[2:], hex(num)[2:]]))