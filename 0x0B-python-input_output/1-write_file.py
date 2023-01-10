#!/usr/bin/python3
""" Module writing to a text file """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        n_text = f.write(text)
        print(len(text))
        return (n_text)
