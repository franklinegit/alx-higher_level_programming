#!/usr/bin/python3

if __name__ == "__main__":
    """program that imports all functions from the file calculator_1.py and handles basic operations."""
    import sys
    from calculator_1 import add, sub, div, mul
    
    no_args = len(sys.argv)
    if no_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    else:
    
        if sys.argv[2] not in {"+", "*", "-", "/"}:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        
        a, b = int(sys.argv[1]), int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a,b)))
        
        elif sys.argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a,b)))
        
        elif sys.argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a,b)))
        
        else:
            print("{} / {} = {}".format(a, b, div(a,b)))