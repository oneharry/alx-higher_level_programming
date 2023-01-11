#!/usr/bin/python3
"""Class definition of a student """


class Student:
    """ class Student defines a student """
    def __init__(self, first_name, last_name, age):
        """ Instantiate class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and not attrs == []:
            attr_list = []
            for attr in attrs:
                getattr(self, attr)
            return attr_list
        return (dir(self))
