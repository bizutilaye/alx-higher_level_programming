#!/usr/bin/python3
'''module: 8-rectangle
'''


class BaseGeometry:
    '''class BaseGeometry
    '''

    def area(self):
        '''raises an Exception with the message area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    '''Rectangle class inherited from BaseGeometry class
    '''

    def __init__(self, width, height):
        '''initializes Rectangle instance
        width: width of rectangle
        height: height of rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''returns string representation of Rectangle
        '''
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        '''returns area of rectangle
        '''
        return self.__width * self.__height
