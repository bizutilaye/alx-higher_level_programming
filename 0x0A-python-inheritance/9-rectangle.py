#!/usr/bin/python3
''' module: 9-rectangle
'''


class BaseGeometry:
    '''A class BaseGeometry.
    '''

    def area(self):
        '''Method that raises an exception.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method that validates a value.
        name: string
        value: integer
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''A class Rectangle that inherits from BaseGeometry.
    '''

    def __init__(self, width, height):
        '''Initializer method.
        width: private, positive integer
        height: private, positive integer
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method that returns the area of the rectangle.
        '''
        return self.__width * self.__height

    def __str__(self):
        '''Method that returns a string representation of the object.
        '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
