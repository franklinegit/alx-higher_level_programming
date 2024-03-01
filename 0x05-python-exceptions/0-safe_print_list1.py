#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function that prints x elements of a list.
    
    Args:
        my_list: A list
        x: number of list elements to print
    
    Return:
        number of elements printed
        
    """
    if not isinstance(my_list, list):
        raise TypeError("Object my_list is not a list")
    
    printed = 0
    for i in range(x):
        try:
            print(my_list[i], end = "")
            printed += 1
        except IndexError:
            break
    print("")
    return (printed)