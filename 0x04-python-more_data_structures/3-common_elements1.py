#!/usr/bin/python3

def common_elements(set_1, set_2):
    """function that returns a set of common elements in two sets.
    
    Args:
        set_1: First set
        set_2: Second set
    
    Reurn:
        new set with common elements
    """
    c_set = set_1.intersection(set_2)
    return (c_set)