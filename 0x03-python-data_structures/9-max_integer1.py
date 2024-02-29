#!/usr/bin/python3

def max_integer(my_list=[]):
    """function that finds the biggest integer of a list.
    
    Args:
        my_list: A list of int
        
    Return:
        The maximum value, otherise None
        
    """
    
    max_int = 0
    if len(my_list) != 0:
        for i in my_list:
            if i > max_int:
                max_int = i
                
        return (max_int)
    else:
        return (None)