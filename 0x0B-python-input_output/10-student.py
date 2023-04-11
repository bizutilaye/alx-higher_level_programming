#!/usr/bin/python3
"""
Module for Student class.
"""


class Student:
    """
    Defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings representing the attributes to
                retrieve. If None, all attributes will be retrieved.

        Returns:
            A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    filtered_dict[key] = value
            return filtered_dict
