#!/usr/bin/python3
''' module: 7-base_geometry
'''


class BaseGeometry:
    '''base geometry class
    '''

    def area(self):
        '''area method raises exception "area() is not implemented"
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates value:
        you can assume name is ith the message <name> must be greater than 0
        '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
