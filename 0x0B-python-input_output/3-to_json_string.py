#!/usr/bin/python3
""" Working with JSON in python """
import json


def to_json_string(my_obj):
    """
        Function returns the JSON representation of an object
        Args:
            my_obj: the JSON object
    """
    return (json.dumps(my_obj))
