"""This program replicated the game Wordle. The player makes six guesses for the secret
word and the program gives an emoji representation of how accurate each guess is"""

__author__: str = "730771648"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    max_turns: int = 6

    while turn <= max_turns:
        """While they haven't ran out of turns"""
        print(f"=== Turn {turn}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))

        if guess == secret:
            """If the guess is correct, they win"""
            print(f"You won in {turn}/{max_turns} turns!")
            quit()
        turn += 1
    """If they ran out of guesses and lost"""
    print(f"X/{max_turns} - Sorry, try again tomorrow!")


def input_guess(secret_word_len) -> str:
    """Asks for a word that is the correct length"""
    guess: str = str(input(f"Enter a {secret_word_len} character word: "))
    while len(guess) != secret_word_len:
        guess: str = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the secret word contains the character"""
    assert len(char_guess) == 1
    for char in secret_word:
        if char == char_guess:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emojis of squares showing how correct the guess is"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_result: str = ""

    for idx in range(len(guess)):
        """Loops through each character of guess"""
        if guess[idx] == secret[idx]:
            emoji_result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
    return emoji_result


if __name__ == "__main__":
    main(secret="codes")
