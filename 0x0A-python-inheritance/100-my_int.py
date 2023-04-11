#!/usr/bin/python3
"""
Module 100-my_int

Contains a rebel MyInt class.
"""


class MyInt(int):
    """
    Class MyInt.

    Inherits from int and has == and != operators inverted.
    """

    def __eq__(self, other):
        """Method __eq__"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Method __ne__"""
        return super().__eq__(other)
