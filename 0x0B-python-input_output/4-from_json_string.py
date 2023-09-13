#!/usr/bin/python3
"""Shebang line."""
import json


def from_json_string(my_str):
    """Function returns the Python object representation of a JSON string."""
    return json.loads(my_str)
