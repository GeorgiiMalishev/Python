decimal_num = float(input())
if decimal_num <= 0 or decimal_num % 1 != 0:
    print("Неверный ввод")
else:
    decimal_num = int(decimal_num)
    binary_str = ""
    octal_str = ""
    hexadecimal_str = ""

    binary_num = decimal_num
    while binary_num > 0:
        remainder = binary_num % 2
        binary_str = str(remainder) + binary_str
        binary_num //= 2

    octal_num = decimal_num
    while octal_num > 0:
        remainder = octal_num % 8
        octal_str = str(remainder) + octal_str
        octal_num //= 8

    hexadecimal_chars = "0123456789ABCDEF"
    hexadecimal_num = decimal_num
    while hexadecimal_num > 0:
        remainder = hexadecimal_num % 16
        hexadecimal_str = hexadecimal_chars[remainder] + hexadecimal_str
        hexadecimal_num //= 16

    print(f"{binary_str}, {octal_str}, {hexadecimal_str}")
