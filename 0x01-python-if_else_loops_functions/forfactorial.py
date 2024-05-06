#!/usr/bin/python3

import sys

def factorial(num):
    """
    This functions finds the factorial of the given input
    
    Parameters:
    num (int): The integer whose factorial value is to be calculated
    
    Returns:
    int: the factorial of num
    
    Raises:
    ValueError: If the value is below zero
    TypeError: If the input is not an integer
    """
    if num == 0:
        return (1)
    
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return (fact)

def calculate_factorial():
    
    try:
        num = int(input("Enter number whose factorial to calculate: "))
        if num < 0:
            print("Please enter a positive integer", file=sys.stderr)
            print("")
            return
        else:
            fact = factorial(num)
            print(f"Factorial of {num} is {fact}")
            print("")
    
    except (ValueError, TypeError) as e:
        print("Invalid input: {}" .format(e), file=sys.stderr)

def exit_program():
    print("Exiting the program...")
    sys.exit


menu = {
    '1': calculate_factorial,
    '2': exit_program
}
    
while True:
    print("====MENU====")
    print("1: Calculate Factorial of a number")
    print("2: Exit proram.")
    
    choice = int(input("Enter your choice: "))
    if isinstance(choice, int):
        if choice in menu:
            menu[choice]()
            break
        else:
            print("Invalid choice. Please choose between '1' and '2'")
            print("")
    else:
        print("Invalid input. Please enter a positive integer.")
        print("")