#!/usr/bin/python3
"""
Module 101-add_attribute

Contains function add_attribute.
"""


def add_attribute(obj, attr, value):
    """Add attribute to object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
