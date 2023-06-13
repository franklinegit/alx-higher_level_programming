#!/usr/bin/python3


def max_integer(my_list=[]):
    """Function finds and returns the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    maxm = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxm:
            maxm = my_list[i]

    return (maxm)
