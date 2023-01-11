#!/usr/bin/python3
""" Define a locked class, with restrictions to creating class"""


class LockedClass:
    """ A locked class
        It prevents creation of new instance attribute,
        except, the new attribute is called first_name
    """
    __slots__ = ['first_name']
