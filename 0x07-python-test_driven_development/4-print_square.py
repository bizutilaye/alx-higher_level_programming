#!/usr/bin/python3

"""
This module defines the print_square function
"""


def print_square(size):
    """
    Print a square of size size using the '#' character.

    Args:
        size (int): the size length of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
