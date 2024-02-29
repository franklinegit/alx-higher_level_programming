#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """function that prints all integers of a list, in reverse order.
    
    Args:
        my_list: A list
        
    Return:
        None
        
    """
    if isinstance(my_list, list):
        for i in reversed(my_list):
            # reversed(my_list) returns a reverse iterator for the list my_list
            # reversed() is not a function that directly returns a reversed list; instead, it returns an iterator
            print("{}".format(i))