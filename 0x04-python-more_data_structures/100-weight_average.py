#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if not my_list:
        return 0

    denom = 0
    nm = 0

    for tup in my_list:
        nm += tup[0] * tup[1]
        denom += tup[1]

    return (nm / denom)

