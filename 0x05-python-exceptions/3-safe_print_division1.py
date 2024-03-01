#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and prints the result.
    
    Args:
        a: An integer
        b: An integer
        
    Returns:
        Returns the value of the division, otherwise: None
        
    """
    result = None
    try:
        result = a / b
        return (result)
    except ZeroDivisionError:
        return (None)
    finally:
        if result is not None:
            print("Inside result:", result)
        else:
            print("Inside result: None")