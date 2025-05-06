#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): Non-negative integer for which to compute the factorial.

    Returns:
    int: Factorial of n; returns 1 if n == 0, otherwise returns n * factorial(n-1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    # Read the command-line argument and convert it to an integer
    num = int(sys.argv[1])
    # Compute and print the factorial of the given number
    print(factorial(num))
