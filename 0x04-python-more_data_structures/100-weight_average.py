#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    avg = 0
    le = 0
    for tup in my_list:
        avg += (tup[0] * tup[1])
        le += tup[1]
    return (avg / le)
