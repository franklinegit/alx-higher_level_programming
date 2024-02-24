def fib(n):
    """Function that prints the Fibonacci series up to the boundary n"""
    a, b = 0, 1
    while a < n:
        print(a, end=(" "))
        a, b = b, a + b
    print()
    
    
bndry = int(input("Enter boundary of Fibonacci series: "))
fib(bndry)