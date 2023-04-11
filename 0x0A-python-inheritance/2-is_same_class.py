#!/usr/bin/python3
"""
module to check if an object is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    function to check if an object is exactly an instance of a specified class
    """
    return type(obj) == a_class
