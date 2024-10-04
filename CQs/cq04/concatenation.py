"""A function that returns the concatenation of the two input strings!"""

__author__: str = "730771648"


def concat(a: str, b: str) -> str:
    """Function takes two strings and returns concatenation"""
    theconcat: str = str(a) + str(b)
    return theconcat


if __name__ == "__main__":
    """so function call still occurs when file is ran but not when imported"""
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
