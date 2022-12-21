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

    def __eq__(self, other):
        """ buitlin instance equality """
        return self.__size == other.__size

    def __ne__(self, other):
        """ checks for non equality """
        return self.__size != other.__size

    def __gt__(self, other):
        """ checks for is greater than """
        return self.__size > other.__size

    def __ge__(self, other):
        """ checks greater or equal to """
        return self.__size >= other.__size

    def __lt__(self, other):
        """ checks for less than """
        return self.__size < other.__size

    def __le__(self, other):
        """ checks for less than or equal """
        return self.__size <= other.__size
