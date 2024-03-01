#!/usr/bin/python3

def uniq_add(my_list=[]):
    """function that adds all unique integers in a list
    
    Args:
        my_list: A list of integers
    
    Return:
        sum of unique elements in the list
    
    """
    sum  = 0
    for i in set(my_list):
        sum += i
    return (sum)