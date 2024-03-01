#!/usr/bin/python3

def safe_print_integer(value):
    """function that prints an integer with "{:d}".format().
    
    Args:
        value: Item to be printed
        
    Return:
        True, otherwise False
        
    """
    
    try:
        print("{:d}".format(value))
        return (True)
    
    except (TypeError, ValueError):
        return (False)