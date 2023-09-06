#!/usr/bin/python3
"""Definition."""


def print_square(size):
    """Function that prints a square with the character #.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for j in range(size):
        [print("#", end="") for k in range(size)]
        print("")
