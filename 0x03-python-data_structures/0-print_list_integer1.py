#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """function that prints all integers of a list.
    
    Args:
        my_list: A list of elements
    
    Return:
        Returns None
    
    """
    for i in my_list:
        if isinstance(i, int):
            print("{}".format(i))