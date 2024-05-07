#!/usr/bin/python3
"""
_summary_

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

    def __init__(self, size=0, position=(0, 0)):
        """constructor method

        Args:
            size (int ): Length of square side
            position (tuple): Position
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) for x in value) or not all(x > 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function that finds area of the square

        Returns:
            int: Area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints to stdout

        Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
