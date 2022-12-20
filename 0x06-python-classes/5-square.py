#!/usr/bin/python3
"""
Create a class Square
"""


class Square:
    """
    A class Square
    """
    def __init__(self, size=0):
        """
        initializing the class
        size must be an integer >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of square"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """Propert retrives value of size"""

        return self.__size

    @size.setter
    def size(self, value):
        """sets size attribute with value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        "prints to stdout the square with '#'"

        n = self.__size
        if n == 0:
            print("")
        for i in range(n):
            for x in range(n):
                print("#", end="")
            print("")
