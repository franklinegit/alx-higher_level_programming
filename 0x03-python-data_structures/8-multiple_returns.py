#!/usr/bin/python3


def multiple_returns(sentence):
    """Function returns tuple with length and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
