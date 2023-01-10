#!/usr/bin/python3
""" Module writing to a text file """


def write_file(filename="", text=""):
    """
        Function writes to filename
        Args:
            text: the text content to be written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        n_text = f.write(text)
        return (n_text)
