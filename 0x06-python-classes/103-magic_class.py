#!/usr/bin/python3
""" Magic class implemented from bytecode"""

import math


class MagicClass:
    """
    Representation of the class
    """

    def __init__(self, radius=0):
        """ initialize attributes """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ calculates the area """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ calculates the circumference """
        return (2 * math.pi * self.__radius)
