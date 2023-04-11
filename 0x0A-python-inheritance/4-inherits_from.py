#!/usr/bin/python3
"""
Module for inherits_from method.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a subclass of the specified cla

    Returns:
        bool: True if obj is an instance .
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    return False
