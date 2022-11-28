#!/usr/bin/python3
import sys


def print_str():
    str = "and that piece of art is useful - Dora Korpar, 2015-10-19"
    sys.stderr.write(str)
    sys.stderr.write("\n")
    sys.exit(1)


print_str()
