#!/bin/usr/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or if obj is an instance of a subclass of a_class.
    Otherwise, it returns False.
    """
    return isinstance(obj, a_class)
