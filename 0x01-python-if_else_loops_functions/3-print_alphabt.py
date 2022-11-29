#!/usr/bin/python3
import string
for char in string.ascii_lowercase:
    if char == "q" or char == "e":
        continue
    print("{:s}".format(char), end="")
