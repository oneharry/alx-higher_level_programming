#!/usr/bin/python3
""" Module returns description of class object"""
import json


def class_to_json(obj):
    """
        Function returns the dictionary description with data structure
        Args:
            obj: object instance of a class
    """
    return json.dumps(obj.__dict__)
