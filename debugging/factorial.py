#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    i = n  # Utilisation d'une nouvelle variable pour l'itération
    while i > 1:
        result *= i
        i = i - 1
    return result

f = factorial(int(sys.argv[1]))
print(f)
