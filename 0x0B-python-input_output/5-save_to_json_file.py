#!/usr/bin/python3
""" Module implemeting python object - JSON serialization"""
import json


def save_to_json_file(my_obj, filename):
    """
        Function writes an Object to a text file, from a JSON representation
        Args:
            my_obj: python objects
            filename: file name to be written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
