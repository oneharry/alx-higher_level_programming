#!/usr/bin/python3
""" Module returns description of class object"""


def class_to_json(obj):
    """
        Function returns the dictionary description with data structure
        Args:
            obj: object instance of a class
    """
    return obj.__dict__
