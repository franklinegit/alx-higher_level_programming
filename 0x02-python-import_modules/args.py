#!/usr/bin/python3
if __name__ == "__main__":
    """Program that prints the number of and list of arguments."""
    import sys

    def noargs():
        """The function prints the number of arguments passed to the script"""
        
        print("Finding number of arguments")
        if len(sys.argv) == 1:
            print("No arguments.")
        
        elif len(sys.argv) == 2:
            print("{} argument.".format(len(sys.argv) - 1))
        
        else:
            print("{} arguments.".format(len(sys.argv) - 1))

        print("")
            
    def printargs():
        """The function prints the actual arguments passed to the script"""
        
        print("Finding number of arguments and printing them as a list")
        no = len(sys.argv)
        
        if len(sys.argv) - 1 == 0:
            print("No arguments.")
            
        elif len(sys.argv) - 1 == 1:
            print("{} argument.".format(no - 1))
            
        else:
            print("{} arguments.".format(no - 1))
        
        for i in range(1, no):
            print("{} {}".format(i, sys.argv[i]))

        print("")
    
    def sumargs():
        """The funtions prints the sum of all arguments"""
        lstargs = [int(arg) for arg in sys.argv[1:]]
        print("The sum of the command line arguments is: ", sum(lstargs))

    noargs()
    printargs()
    sumargs()