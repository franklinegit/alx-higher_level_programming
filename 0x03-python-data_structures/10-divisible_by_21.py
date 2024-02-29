#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list.
    
    Args:
        my_list: A list of integers
        
    Return:
        new list with True or False
        
    """
    
    if isinstance(my_list, list):
        new_list = [True if i % 2 == 0 else False for i in my_list]
        return (new_list)
                