#!/usr/bin/python3
""" Define a class Base with only init func"""


class Base:
    """
        A class Base
        Has one private class attribute and id instance attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """ Initialize an instance of the class Base"""
        __class__.__nb_objects += 1
        try:
            if id is None and self:
                self.id = __class__.__nb_objects
            elif int(id) <= 0 or type(int(id)) is not int:
                raise TypeError("Inavlid!")
            elif int(id) > 0 and int(id) < __class__.__nb_objects:
                raise TypeError("Invalid!")
            else:
                self.id = int(id)
        except (ValueError, TypeError):
            self.id = __class__.__nb_objects
