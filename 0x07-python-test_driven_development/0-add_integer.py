#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Returns the sum of two integers

    Args:
    a (int or float): The first number to add
    b (int or float): The second number to add. Default value is 98.

    Raises:
    TypeError: If a or b is not an integer or a float

    Returns:
    int: The sum of a and b, cast to an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
