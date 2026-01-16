#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculates the factorial of a given non-negative integer using recursion.
    
    Parameters:
    n (int): The integer number to calculate the factorial of.
    
    Returns:
    int: The factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    # Ajout d'une sécurité pour éviter une erreur si aucun argument n'est passé
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
