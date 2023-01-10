#!/usr/bin/python3
""" Module appending content to file """


def append_write(filename="", text=""):
    """
        Function appends text to a text file
        Args:
            filename: name of file
            text: content to be appended to the file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
