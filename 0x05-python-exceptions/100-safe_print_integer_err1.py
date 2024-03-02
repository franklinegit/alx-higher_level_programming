#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """function that prints an integer.
    
    Args:
        value: item to be printed
        
    Returns:
        True if value has been correctly printed Otherwise, returns False

    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return (False)