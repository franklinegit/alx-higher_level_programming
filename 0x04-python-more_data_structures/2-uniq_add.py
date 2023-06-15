#!/usr/bin/python3

def uniq_add(my_list=[]):
   nm = 0
   uniq = set(my_list)

    for i in uniq:
        nm += i

    return (nm)
