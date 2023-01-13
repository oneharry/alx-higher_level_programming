#!/usr/bin/python3
""" Define a class Rectangle which is an inheritance
    of class Base
"""
Base = __import__('base').Base

class Rectangle(Base):
    """
        A class Rectangle
	Inheritance of class Base
        Attributes private:
            width, height, x, y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize an instance of the class Rectangle"""
        try:
            if width is None or height is None:
                raise ValueError("width and height must be a positive int!")
            if type(width) is not float and type(width) is not int or width < 0:
                raise TypeError("width must be positive int!")
            if type(height) is not float and type(height) is not int or height < 0:
                raise TypeError("height must be a positive int")
            if type(x) is not float and type(x) is not int:
                raise TypeError("x must be an int")
            if type(y) is not float and type(y) is not int:
                raise TypeError("y must be an int")
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
        except (TypeError, ValueError) as exc:
            print(str(exc))
            raise
        else:
            super().__init__(id)

    @property
    def width(self):
        """ Returns the value of width attr of instance"""
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the value of width attr"""
        try:
            if type(width) is not float and type(width) is not int:
                raise TypeError("width must be positive integers!")
            elif width < 0:
                raise ValueError("width must be positive integers!")
            else:
                self.__width = width
        except (TypeError, ValueError) as exc:
            print(str(exc))
            raise

    @property
    def height(self):
        """ Returns the value of height attr of instance"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the value of height attr """
        try:
            if type(height) is not float and type(height) is not int:
                raise TypeError("height must be positive integers!")
            elif height < 0:
                raise ValueError("height must be positive integers!")
            else:
                self.__height = height
        except (ValueError, TypeError) as exc:
            print(str(exc))
            raise

    @property
    def x(self):
        """ Returns the value of x attribute of instance"""
        return self.__x

    @x.setter
    def x(self, x):
        """
            Sets the value of x attribute
        """
        try:
            if type(x) is not float and type(x) is not int:
                raise TypeError("x must be an integer")
            else:
                self.__x = x
        except TypeError as exc:
            print(str(exc))
            raise

    @property
    def y(self):
        """ Returns the value of y attr of instance """
        return self.__y

    @y.setter
    def y(self, y):
        """
            Sets the value of y attribute
        """
        try:
            if type(y) is not float and type(y) is not int:
                raise TypeError("y must be an integer")
            else:
                self.__y = y
        except TypeError as exc:
            print(str(exc))
            raise
