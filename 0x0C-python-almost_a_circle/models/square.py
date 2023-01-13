#!/usr/bin/python3
""" Define Square class, an inheritance of Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Define Square class
        A subclass of Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the object when an instance is created"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns info about the object """
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__,
                self.id, self.x, self.y, self.width))
