#!/usr/bin/python3
"""
Module that contains a function that writes an Object to a text file, 
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (obj): The Python object to write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
