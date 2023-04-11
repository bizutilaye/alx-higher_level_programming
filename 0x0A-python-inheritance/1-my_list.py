#!/usr/bin/python3
"""This module defines a MyList class that inherits from the list class."""

class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
