#!/usr/bin/python3
"""if the object is an instance of, or if the object is an instance
of a class that inherited from, the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance

    Args:
        obj (object): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instanc, False otherwise.
    """
    return isinstance(obj, a_class)
