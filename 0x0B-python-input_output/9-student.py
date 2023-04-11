#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
    A class representing a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student object with the given name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
        }
