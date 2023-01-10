#!/usr/bin/python3
""" Module to access files """


def read_file(filename=""):
    """
       Function prints the contents of a file
       Args:
           filename: the name of file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        my_file = f.readlines()
        for line in my_file:
            print(line)
