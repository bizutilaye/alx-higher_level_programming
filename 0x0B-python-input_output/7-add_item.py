#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file.

This script imports two functions from other modules:
    - save_to_json_file(filename, my_obj)
    - load_from_json_file(filename)

It creates a list containing all command line arguments passed to the script.
The list is then loaded from a JSON file if it exists, or created if it doesn't.
The command line arguments are added to the list, which is then saved to the JSON file.

The script does not manage file permissions or exceptions.

Example:
    ```
    $ cat add_item.json
    cat: add_item.json: No such file or directory
    $ ./7-add_item.py
    $ cat add_item.json ; echo ""
    []
    $ ./7-add_item.py Best School
    $ cat add_item.json ; echo ""
    ["Best", "School"]
    $ ./7-add_item.py 89 Python C
    $ cat add_item.json ; echo ""
    ["Best", "School", "89", "Python", "C"]
    ```
"""

import sys
from os import path
from typing import List
from json import dump, load
from pathlib import Path


def load_from_json_file(filename: str) -> any:
    """Creates an object from a JSON file.

    Args:
        filename: A string representing the filename of the JSON file.

    Returns:
        The deserialized JSON object.

    """
    with open(filename, mode='r', encoding='utf-8') as f:
        return load(f)


def save_to_json_file(filename: str, my_obj: any) -> None:
    """Saves an object to a JSON file.

    Args:
        filename: A string representing the filename of the JSON file.
        my_obj: The object to be serialized to JSON and saved.

    """
    with open(filename, mode='w', encoding='utf-8') as f:
        dump(my_obj, f)


if __name__ == '__main__':
    filename = "add_item.json"

    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(filename, my_list)
