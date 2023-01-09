#!/usr/bin/python3
""" a function that checks class """


def is_same_class(obj, a_class):
    """
        checks is an object is of same class as a_class
        Args:
            obj: object,
            a_class: class
    """
    if type(obj) == a_class:
        return True
    return False
