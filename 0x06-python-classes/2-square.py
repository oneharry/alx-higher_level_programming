#!/usr/bin/python3
class Square:
    """
    This is to simply define a Sqaure class
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
