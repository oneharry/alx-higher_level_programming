#!/usr/bin/python3
""" Modules checks for the max int value in a list"""
import math


def max_integer(list):
    """
        Function returns maximun number in a list
        Args:
            list: list object
    """
    if list == None or list == []:
        return None

    return max(list)
print(max_integer("Hello"))
