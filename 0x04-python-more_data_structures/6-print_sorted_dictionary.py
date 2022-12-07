#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = dict(sorted(a_dictionary.items()))
    for key, val in dic.items():
        print("{}: {}".format(key, val))
