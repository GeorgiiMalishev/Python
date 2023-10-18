def get_word_composition(word):
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    composition = {}
    middle_letter = ''

    for letter, count in letter_count.items():
        if count % 2 != 0:
            if middle_letter == '':
                middle_letter = letter
            else:
                return None, None
        composition[letter] = count // 2

    return composition, middle_letter


def create_palindrome(word):
    composition, middle_letter = get_word_composition(word)

    if composition is not None:
        left_half = ''.join([letter * count for letter, count in composition.items()])
        palindrome = left_half + middle_letter + left_half[::-1]
        return palindrome
    else:
        return None


word = input()
palindrome = create_palindrome(word)
if palindrome is not None:
    print(create_palindrome(word))


