"""Uses the other two files and calls functions with global variables"""

__author__: str = "730771648"

from CQs.cq04.concatenation import concat

x: str = "123"
y: str = "abc"

print(concat(x, y))

from CQs.cq04.coordinates import get_coords

get_coords(x, y)
