#!/usr/bin/python3
"""Definition."""


def text_indentation(text):
    """function prints 2 new lines after the characters: ., ? and :.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lt = 0
    while lt < len(text) and text[lt] == ' ':
        lt += 1

    while lt < len(text):
        print(text[lt], end="")
        if text[lt] == "\n" or text[lt] in ".?:":
            if text[lt] in ".?:":
                print("\n")
            lt += 1
            while lt < len(text) and text[lt] == ' ':
                lt += 1
            continue
        lt += 1
