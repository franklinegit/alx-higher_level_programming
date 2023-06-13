#!/usr/bin/python3


def no_c(my_string):
    """Function removes all characters c and C from a string."""
    filtered_chars = []
    for char in my_string:
        if char != 'c' and char != 'C':
            filtered_chars.append(char)
    return "".join(filtered_chars)
