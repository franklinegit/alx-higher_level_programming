def prime(n):
    """Functions checks if the number n is a prime number or not starting from two"""
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
    
    
n = int(input("Enter number to check if it's prime: "))
prime(n)