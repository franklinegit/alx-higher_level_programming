#!/usr/bin/python3
"""Module definition"""


def max_integer(list=[]):
    """Unittests """
    if len(list) == 0:
        return None
    res = list[0]
    j = 1
    while j < len(list):
        if list[j] > res:
            res = list[j]
        j += 1
    return res

