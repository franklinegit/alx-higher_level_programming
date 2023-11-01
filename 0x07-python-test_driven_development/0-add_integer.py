#!/usr/bin/python3
"""Definition."""


def add_integer(a, b=98):
    """Function adding 2 integers.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, float) and not isinstance(a, int))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, float) and not isinstance(b, int))):
        raise TypeError("b must be an integer")
    return (int(b) + int(a))
