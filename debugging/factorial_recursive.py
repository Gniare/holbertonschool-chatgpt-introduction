#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
        n (int): The number for which factorial is calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the input from command line argument
f = factorial(int(sys.argv[1]))
print(f)
