#!/usr/bin/python3
import json
""" Working with JSON in python """


def to_json_string(my_obj):
    """
        Function returns the JSON representation of an object
        Args:
            my_obj: the JSON object
    """
    return (json.dumps(my_obj))
