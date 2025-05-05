#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <integer>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Error: the argument must be an integer")
        sys.exit(1)
    print(factorial(num))
