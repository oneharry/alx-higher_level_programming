#!/usr/bin/python3
""" Look up attributes of an object """


def lookup(obj):
    """ Prints tihe available attributes of an object
        Args:
            obj - object parameter
    """
    return (dir(obj))
