#!/usr/bin/python3
def common_elements(set_1, set_2):
    for x in set_1:
        el = [y for y in set_2 if y == x]
    return el
