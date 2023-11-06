#!/usr/bin/python3
"""An inherited list class MyList."""


class MyList(list):
    """Subclass that inherits from list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
