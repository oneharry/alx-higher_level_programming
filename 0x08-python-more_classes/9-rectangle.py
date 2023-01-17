#!/usr/bin/python3
""" Define an empty Rectangle class """


class Rectangle:
    """
        A Rectangle class defines a rectangle
        Private attributes: height, weight
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            Initializes an object of the class
        """
        try:
            if type(width) is not int:
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            if type(height) is not int:
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = height
            self.__width = width
        except (ValueError, TypeError):
            raise
        else:
            type(self).number_of_instances += 1

    @property
    def width(self):
        """ Returns the value of width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of private attr with the value of 'value'"""
        try:
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        except (ValueError, TypeError):
            raise

    @property
    def height(self):
        """ Returns the value of intanc private attribute 'height'"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the value of height inst attribut with 'value'"""
        try:
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        except (ValueError, TypeError):
            raise

    def area(self):
        """ Returns the area of the instance
            Area = h * w
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            Returns the perimeter of onject instance
            Perimeter = 2 * (h + w)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ Returns the unofficial string represntation of the object"""
        h = self.__height
        w = self.__width
        s = self.print_symbol
        text = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for i in range(h):
            text += (w * str(s))
            if i != h - 1:
                text += "\n"
        return text

    def __repr__(self):
        """ Return string representation of the rectangle to be
            able to recreate new instance by using eval()
        """
        return f"{__class__.__name__}({self.__width}, {self.__height})"

    def __del__(self):
        """ Prints goodbye message when instance is deleted """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Static method
            Compares the area of two instance of Rectangle class
            Args:
                rect_1, rect_2 are instances of Rectangle
        """
        try:
            if not isinstance(rect_1, Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            if not isinstance(rect_2, Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
        except (TypeError):
            raise

    @classmethod
    def square(cls, size=0):
        """
            Class method
            Returns a new instance of Rectangle class
            with width==height==size
        """
        if cls.__name__ == "Rectangle":
            return cls(size, size)
