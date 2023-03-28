#!/usr/bin/python3
"""
Module 3-square
Defines class Square with private attribute size and public attribute area
"""


class Square:
    """
    Square class with private attribute size and public attribute area
    """
    def __init__(self, size=0):
        """
        Initializes square with size argument
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square
        """
        return self.__size ** 2
