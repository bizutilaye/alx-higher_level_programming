#!/usr/bin/python3
""" This module contains geometric shape classes """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ area method that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value argument as integer """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """ Rectangle class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Initializes an instance of Rectangle """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ Returns a formatted string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ Calculates the area of a Rectangle """
        return self.__width * self.__height


class Square(Rectangle):
    """ Square class that inherits from Rectangle """

    def __init__(self, size):
        """ Initializes an instance of Square """
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Returns a formatted string """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """ Calculates the area of a Square """
        return self.__size ** 2
