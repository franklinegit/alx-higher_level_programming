#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elememts of a list.

    Args:
        my_list (list): list of integer elements to print.
        x (int): The number of elements to print.

    Returns:
        Number of elements printed.
    """
    ret = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
