#!/usr/bin/python3

def element_at(my_list, idx):
    """function that retrieves an element from a list like in C.
    
    Args:
        my_list: A list of elements
        idx: index of element in the list
        
    Return:
        If idx is negative, return None, otherwise return the element at idx
    
    """
    max_idx = len(my_list) - 1
    if idx < 0 or idx > max_idx:
        return (None)
    
    return (my_list[idx])
    