#!/usr/bin/python3

"""prints the ASCII alphabet, in lowercase, not followed by a new line."""
for letter in range(97, 123):
    if chr(letter) == "q" or "e":
        continue
    else:
        print("{}".format(chr(letter)), end="")