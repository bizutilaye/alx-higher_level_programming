#!/usr/bin/python3
"""
Module that defines a Square class.

This module contains only one class, Square. The Square class represents a
geometric square with a given size. The class has a private instance attribute,
__size, that stores the size of the square.

Example:
    Create a Square object with a size of 3:
    >>> my_square = Square(3)

"""

class Square:
    """
    Represents a square with a given size.

    The size of the square is stored privately as an instance attribute.
    """

    def __init__(self, size):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
