#!/usr/bin/python3
"""
Defines a square

Raises:
    TypeError: If type of size is not int
    ValueError: If value of size is less than zero
"""


class Square:
    """
    a class for square
    """
    def __init__(self, size=0):
        """_summary_

        Args:
            size (int): Size of square. Defaults to 0.

        Raises:
            TypeError: If type of size is not int
            ValueError: If value of size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
