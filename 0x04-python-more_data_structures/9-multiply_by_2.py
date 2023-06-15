#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2"""
    newdr = a_dictionary.copy()
    keys = list(newdr.keys())

    for i in keys:
        newdr[i] *= 2

    return (newdr)
