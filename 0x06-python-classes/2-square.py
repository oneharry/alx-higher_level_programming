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
        try:
            if not isinstance(size, int):
                raise TypeError()
            if size < 0:
                raise ValueError()
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
