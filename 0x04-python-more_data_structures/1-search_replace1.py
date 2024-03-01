#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """"function that replaces all occurrences of an element by another in a new list.
    
    Args:
        my_list: A list
        search: Element to search and replace
        replace: Element to take up search's place
        
    Return:
        new list with search replced by replace
        
    """
    
    new_list = [replace if my_list[i] == search else my_list[i] for i in range(len(my_list))]
    return (new_list)