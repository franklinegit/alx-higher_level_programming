#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix
    
    Args:
        matrix: A matrix(list of lists)
        
    Return:
        A matrix with squared elements
        
    """
    squared_matrix = []
    for row in matrix:
        squared_row = list(map(lambda x: x**2, row))
        squared_matrix.append(squared_row)
    
    return (squared_matrix)

def square_matrix_simple1(matrix=[]):
    """function that computes the square value of all integers of a matrix
    
    Args:
        matrix: A matrix(list of lists)
        
    Return:
        A matrix with squared elements
        
    """
    
    squared_matrix = [[x**2 for x in row]for row in matrix]
    return (squared_matrix)