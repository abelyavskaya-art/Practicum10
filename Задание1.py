
def find_letters(sentence: str) -> None:
    """
    Counts the number of vowels and consonants in a line.

    :param sentence: input string for analysis
    :type sentence: str
    :return: None
    """
    consonants = 'бвгджзйклмнпрстфхцчшщ'
    vowels = 'аеёиоуыэюя'
    count_vowels = 0
    count_consonants = 0
    for letter in sentence:
        if letter.isalpha() and letter.lower() in vowels:
            count_vowels += 1
        elif letter.isalpha and letter.lower() in consonants:
            count_consonants += 1

    print(f"Гласных: {count_vowels}")
    print(f"Согласных: {count_consonants}")

text = input()
find_letters(text)
