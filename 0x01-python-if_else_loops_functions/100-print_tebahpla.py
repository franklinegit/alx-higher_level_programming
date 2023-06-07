#!/usr/bin/python3
# 100-print_tebahpla.py


""""Print the alphabet in reverse order and alternating case."""
i = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - i)), end="")
    i = 32 * (i == 0)
