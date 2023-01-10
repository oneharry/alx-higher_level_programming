#!/usr/bin/python3
""" Module creates a python object from JSON representation file """
import json


def load_from_json_file(filename):
    """
        Function creates an object from a JSON file
        Args:
            filename: JSON file name
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
