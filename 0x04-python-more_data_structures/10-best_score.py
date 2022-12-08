#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = 0
    key = ""
    for k, v in a_dictionary.items():
        if v > max:
            max = v
            key = k
    return key
