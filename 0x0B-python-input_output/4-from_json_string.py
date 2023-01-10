#!/usr/bin/python3
import json
""" Module accessing python object to JSON representation """


def from_json_string(my_str):
    """
        Function returns python object from its JSON representation
        Args:
            my_str: JSON represntation of object
    """
    return (json.loads(my_str))
