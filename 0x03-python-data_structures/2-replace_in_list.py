#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replace_in_list - replace list element at index idx
    """
    le = len(my_list) - 1
    if idx < 0 or idx > le:
        return my_list
    my_list[idx] = element
    return my_list
