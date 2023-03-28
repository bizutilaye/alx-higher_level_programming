#!/usr/bin/python3
class Square:
    """
    This is a class Square that defines a square.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for Square class.

        Parameters:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        This is a getter for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is a setter for size attribute.

        Parameters:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        This method returns the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints the square to the stdout.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
