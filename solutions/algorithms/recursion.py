"""
Recursion Solutions
"""


def fibonacci(n):
    """Recursive fibonacci implementation."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):
    """Recursive factorial implementation."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def power(base, exponent):
    """Recursive power calculation."""
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


def sum_digits(n):
    """Recursive sum of digits."""
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def reverse_string(s):
    """Recursive string reversal."""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


def tower_of_hanoi(n, source, destination, auxiliary):
    """Tower of Hanoi solution."""
    if n == 1:
        return [(source, destination)]
    
    moves = []
    # Move n-1 disks from source to auxiliary
    moves.extend(tower_of_hanoi(n - 1, source, auxiliary, destination))
    # Move the largest disk from source to destination
    moves.append((source, destination))
    # Move n-1 disks from auxiliary to destination
    moves.extend(tower_of_hanoi(n - 1, auxiliary, destination, source))
    
    return moves
