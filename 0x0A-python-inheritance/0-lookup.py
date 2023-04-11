#!/usr/bin/python3
''' function that returns the list
'''


def lookup(obj):
    ''' function: lookup()
    Returns a list object
    '''
    return [attr for attr in dir(obj)]
