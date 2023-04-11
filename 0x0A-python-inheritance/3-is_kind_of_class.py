#!/usr/bin/python3
"""
This module contains a function that returns True if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class; otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or any of its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
