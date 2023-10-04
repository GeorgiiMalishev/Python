data = input()
count_consonants, count_vowels = 0, 0
for char in data:
    if char in 'бвгджзйклмнпрстфхцчшщ':
        count_consonants += 1
    elif char in 'аеёиоуыэюя':
        count_vowels += 1

print(str(count_vowels) + " " + str(count_consonants))