#!/usr/bin/python3
"""Module 11-square.

Creates a Rectangle class and a Square class that inherits from it.
"""


class Rectangle:
    """Class Rectangle.

    Attributes:
        __width -- width of the rectangle
        __height -- height of the rectangle

    Methods:
        __init__(self, width, height)
        area(self)
        __str__(self)
    """
    def __init__(self, width, height):
        """Class constructor.

        Args:
            width -- the width of the rectangle
            height -- the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method area.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Method __str__.

        Returns:
            The following rectangle description: [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square.

    Attributes:
        __size -- size of the square

    Methods:
        __init__(self, size)
        area(self)
        __str__(self)
    """
    def __init__(self, size):
        """Class constructor.

        Args:
            size -- the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Method __str__.

        Returns:
            The following square description: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
