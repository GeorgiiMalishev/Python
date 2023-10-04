side_length = int(input())

perimeter = 4 * side_length

area = side_length ** 2

diagonal = (2 * side_length ** 2) ** 0.5

perimeter = round(perimeter, 2)
area = round(area, 2)
diagonal = round(diagonal, 2)

print(f"{perimeter:.2f}, {area:.2f}, {diagonal:.2f}")