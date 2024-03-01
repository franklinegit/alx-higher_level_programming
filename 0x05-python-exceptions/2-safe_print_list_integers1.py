#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """function that prints the first x elements of a list and only integers.
    
    Args:
        my_list: A list
        x: Number of elemnts to print
    
    Return:
        Actual number of integers printed
        
    """
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            # Handled the index error exception also
            break
    print()
    return(printed)