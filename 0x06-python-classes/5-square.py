#!/usr/bin/python3
class Square:
    """
    Represents a square
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance

        Args:
            size (int): the size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size

        Args:
            value (int): the new size of the square

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print('#' * self.__size)
