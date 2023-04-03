#!/usr/bin/python3
""" Module that defines a rectangle """


class Rectangle:
    """ Rectangle class """
    
    def __init__(self, width=0, height=0):
        """ Initializes a new instance of a rectangle
        
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """ Gets the width of the rectangle """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle
        
        Args:
            value (int): The value to set the width to
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """ Gets the height of the rectangle """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle
        
        Args:
            value (int): The value to set the height to
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
