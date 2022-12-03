#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    new_in_list - replace element at index to make a new copy of list
    """
    le = len(my_list) - 1
    if idx < 0 or idx > le:
        return my_list
    new_list = my_list[:idx + 1]
    new_list[len(new_list) - 1] = element
    new_list += my_list[idx + 1:]

    return new_list
