#!/usr/bin/python3
"""Shebang line."""


def read_file(filename=""):
    """Function prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
