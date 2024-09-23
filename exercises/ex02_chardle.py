"""A game inspired by Wordle that prompts the user for a five-character 
word and a single letter. Then it tests to see which indices of the word 
match the single letter."""

__author__: str = "730771648"


def input_word() -> str:
    """Takes input of a word and makes sure it's 5 characters"""
    word_input: str = str(input("Enter a 5-character word: "))
    if len(word_input) < 5 or len(word_input) > 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word_input


def input_letter() -> str:
    """Takes input of a letter and make sure it's just one letter"""
    letter_input: str = str(input("Enter a single character: "))
    if len(letter_input) < 1 or len(letter_input) > 1:
        print("Error: Character must be a single character.")
        exit()
    return letter_input


def contains_char(word: str, letter: str) -> None:
    """Checks if input character matches any of the characters in input word and says
    amount of instances the input character is found in the input word"""
    print("Searching for " + letter + " in " + word)
    count_match: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count_match += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count_match += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count_match += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count_match += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count_match += 1
    if count_match == 0:
        print("No instances of " + letter + " found in " + word)
    elif count_match == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count_match) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
