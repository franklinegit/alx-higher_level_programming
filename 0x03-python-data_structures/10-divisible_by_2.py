#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """Function finds and appends all multiples of 2 in a list."""
    multp2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multp2.append(True)
        else:
            multp2.append(False)

    return (multp2)
