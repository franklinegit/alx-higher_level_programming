#!/usr/bin/python3
import sys
def add_tuple(tuple_a=(), tuple_b=()):
    """function that adds 2 tuples.
    
    Args:
        tuple_a: First tuple
        tuple_b: Second tuple
        
    Return:
        added tuple
        
    """
    tuple_list = (tuple_a, tuple_b)
    for my_tuple in tuple_list:
        if all(isinstance(element, int) for element in my_tuple):
            if len(tuple_a) == 0:
                tuple_a = (0, 0)
            if len(tuple_a) == 1:
                tuple_a = (tuple_a[0], 0)
            if len(tuple_b) == 0:
                tuple_b = (0, 0)
            if len(tuple_b) == 1:
                tuple_b = (tuple_b[0], 0)
            return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        
        else:
            sys.exit(1)