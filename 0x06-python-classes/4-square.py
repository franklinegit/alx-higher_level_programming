#!/usr/bin/python3
"""_summary_

Raises:
    TypeError: If size is not of type int
    ValueError: If size is not >= 0
"""


class Square:
    """class Square that defines a square

    methods:
        def area(self):
            Finds area of the square
    """

    def __init__(self, size=0):
        """constructor method

        Args:
            size (int ): Size of square side
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Function that finds area of the square

        Returns:
            int: Area
        """
        return (self.__size ** 2)
