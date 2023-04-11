#!/usr/bin/python3
"""
module 1-my_list
inherits from list
"""


class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method that prints a sorted list
        """
        print(sorted(self))
