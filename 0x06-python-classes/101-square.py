#!/usr/bin/python3
"""
Create a class Square
"""


class Square:
    """
    A class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializing the class: size , position
        size must be an integer >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        for a in range(self.__position[1]):
            print("")
        pos = self.__position[0]
        for i in range(n):
            for y in range(pos):
                print(" ", end="")
            for x in range(n):
                print("#", end="")
            print("")

    @property
    def position(self):
        """ Returns the value of position attribute """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position attribute with value
        input value must be a tuple
        """

        if (not isinstance(value, tuple) or value[0] < 0 or
                value[1] < 0 or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __str__(self):
        """ Prints square when class Square is printed """
        n = self.__size
        if n == 0:
            print("")
        for a in range(self.__position[1]):
            print("")
        pos = self.__position[0]
        for x in range(n):
            for y in range(pos):
                print(" ", end="")
            for z in range(n):
                print("#", end="")
            if (x != n - 1):
                print("")
        return ("")
