#!/usr/bin/python3
"""
This module contains the function write_file
"""


def write_file(filename="", text=""):
    """Write text to file filename """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
