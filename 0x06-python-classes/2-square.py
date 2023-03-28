#!/usr/bin/python3
"""
module 2-square
define the class Square
"""


class Square:
    """
    class Square
    private instance attribute: size
    """
    def __init__(self, size=0):
        """
        Instantiation with optional size
        Args:
            size: size of the square (int)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
