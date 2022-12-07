#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    num = 0
    for x in my_list:
        if x in new_list:
            continue
        new_list.append(x)
        num += x
    return num
