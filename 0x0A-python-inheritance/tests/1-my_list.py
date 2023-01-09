#!/usr/bin/python3
""" Create a class inheritance of list class """

class MyList(list):
    """
	MyList class, a sub class of list 
	Arg:
            list: the super class list
    """

    def print_sorted(self):
        """ print sorted self in ascending order"""
        print(sorted(self))
