"""This is a simple number guessing game"""

__author__: str = "730771648"


def guess_a_number() -> None:
    secret: int = 7
    guess: str = input("Guess a number: ")
    print("Your guess was " + guess)
    if secret == int(guess):
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    if __name__ == "__main__":
        guess_a_number()
