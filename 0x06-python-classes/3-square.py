#!/usr/bin/python3

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
            
    def area(self):
        """Function that finds area of the square
        
        Returns:
            int: Area
        """
        return(self.__size ** 2)