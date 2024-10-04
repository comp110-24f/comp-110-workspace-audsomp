"""Imports concat function and prints the formatted pairs of each character in the two input strings."""

__author__: str = "730771648"

from CQs.cq04.concatenation import concat


def get_coords(xs: str, ys: str) -> None:
"""Outer loop iterates over every character in 
xs and inner loop iterates over every character in 
ys and contains the print statement."""
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):

            pair = concat("(", xs[i])
            pair = concat(pair, ",")
            pair = concat(pair, ys[j])
            pair = concat(pair, ")")
            print(pair)
            j += 1
        i += 1
