def count_letter_frequency(input_filename, output_filename):
    with open(input_filename, 'r', encoding="utf-8") as file:
        text = file.read()

    letter_frequency = {}

    for char in text:
        if char.isalpha():
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1

    sorted_letter_frequency = sorted(letter_frequency.items(), key=lambda item: item[1])

    with open(output_filename, 'w', encoding="utf-8") as output_file:
        for char, count in sorted_letter_frequency:
            output_file.write(f"{char}: {count}\n")


input_filename = input("Введите имя файла ")
output_filename = "output.txt"
count_letter_frequency(input_filename, output_filename)