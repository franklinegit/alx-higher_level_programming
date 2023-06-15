#!/usr/bin/python3

def number_keys(a_dictionary):
    """Function that returns the number of keys in a dictionary"""
    nm = 0
    keys = list(a_dictionary.keys())

    for i in keys:
        nm += 1

    return (nm)
