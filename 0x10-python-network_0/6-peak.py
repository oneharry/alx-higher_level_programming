#!/usr/bin/python3
""" Find the peak of a list"""


def find_peak(my_list):
    """ Returns the peak value in the list """
    if len(my_list) == 0:
        return None
    if len(my_list) == 1:
        return my_list[0]
    return max(my_list)
