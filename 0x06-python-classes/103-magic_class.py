#!/usr/bin/python3
""" Magic class implemented from bytecode"""


class MagicClass:
    """
    Representation of the class
    """

    def __init__(self, radius):
        """ initialize attributes """
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ calculates the area """
        return self.__radius ** math.pi

    def circumference(self):
        """ calculates the circumference """
        return math.pi * self.__radius
