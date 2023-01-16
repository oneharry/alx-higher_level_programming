#!/usr/bin/python3
""" Define a class Rectangle which is an inheritance
    of class Base
"""
from models.base import Base
import json


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
            if type(width) is not int:
                raise TypeError("width must be an integer")
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if type(x) is not int:
                raise TypeError("x must be an integer")
            if type(y) is not int:
                raise TypeError("y must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
            if height <= 0:
                raise ValueError("height must be > 0")
            if x < 0:
                raise ValueError("x must be >= 0")
            if y < 0:
                raise ValueError("y must be >= 0")
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
            if type(width) is not int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
            self.__width = width
        except (TypeError, ValueError) as exc:
            raise

    @property
    def height(self):
        """ Returns the value of height attr of instance"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the value of height attr """
        try:
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if height <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height
        except (ValueError, TypeError) as exc:
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
            if type(x) is not int:
                raise TypeError("x must be an integer")
            if x < 0:
                raise ValueError("x must be >= 0")
            self.__x = x
        except TypeError as exc:
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
            if type(y) is not int:
                raise TypeError("y must be an integer")
            if y < 0:
                raise ValueError("y must be >= 0")
            self.__y = y
        except TypeError as exc:
            raise

    def area(self):
        """
            Function calculates the area of class instance
            Returns the product of height and width
        """
        return self.__width * self.__height

    def display(self):
        """ Prints the character # to stdout
            height and width of instance
        """
        w = self.__width
        h = self.__height
        y = self.__y
        x = self.__x
        if y > 0:
            for a in range(y):
                print()
        for i in range(h):
            if x > 0:
                for b in range(x):
                    print(" ", end="")
            for j in range(w):
                print("#", end="")
            print()

    def __str__(self):
        """ Overriding the special __str__ function"""
        return ("[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
            Function takes in variable arguments and updates
            Instance attributes are updated
            Args:
                *args: Variable arguments
        """
        try:
            if not args or args == ():
                for key, val in kwargs.items():
                    if key == "id":
                        if val is None:
                            self.__init__(self.width, self.height, self.x,
                                          self.y)
                        self.id = val
                    if key == "width":
                        self.width = val
                    if key == "height":
                        self.height = val
                    if key == "x":
                        self.x = val
                    if key == "y":
                        self.y = val
            elif args:
                le = len(args)
                if args[0] is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                self.id = args[0]
                if le > 1:
                    self.width = args[1]
                if le > 2:
                    self.height = args[2]
                if le > 3:
                    self.x = args[3]
                if le > 4:
                    self.y = args[4]
        except Exception:
            raise

    def to_dictionary(self):
        """ Returns the dict representation of a Rectangle obj"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
