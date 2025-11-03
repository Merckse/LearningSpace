"""
Recursion Tasks

Practice recursive problem-solving techniques.
"""


def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Each number is the sum of the two preceding ones.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> fibonacci(0)
        0
        >>> fibonacci(5)
        5
        >>> fibonacci(10)
        55
    """
    # TODO: Implement recursive fibonacci
    pass


def factorial(n):
    """
    Calculate factorial of n using recursion.
    
    Factorial of n (n!) is the product of all positive integers <= n.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: n! (factorial of n)
        
    Example:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
    """
    # TODO: Implement recursive factorial
    pass


def power(base, exponent):
    """
    Calculate base^exponent using recursion.
    
    Args:
        base (int/float): Base number
        exponent (int): Non-negative exponent
        
    Returns:
        int/float: base raised to the power of exponent
        
    Example:
        >>> power(2, 3)
        8
        >>> power(5, 0)
        1
    """
    # TODO: Implement recursive power calculation
    pass


def sum_digits(n):
    """
    Calculate sum of digits of a number using recursion.
    
    Args:
        n (int): Non-negative integer
        
    Returns:
        int: Sum of all digits
        
    Example:
        >>> sum_digits(123)
        6
        >>> sum_digits(9875)
        29
    """
    # TODO: Implement recursive digit sum
    pass


def reverse_string(s):
    """
    Reverse a string using recursion.
    
    Args:
        s (str): String to reverse
        
    Returns:
        str: Reversed string
        
    Example:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
    """
    # TODO: Implement recursive string reversal
    pass


def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solve Tower of Hanoi puzzle using recursion.
    
    Return a list of moves where each move is a tuple (from_rod, to_rod).
    
    Args:
        n (int): Number of disks
        source (str): Source rod name
        destination (str): Destination rod name
        auxiliary (str): Auxiliary rod name
        
    Returns:
        list: List of tuples representing moves
        
    Example:
        >>> tower_of_hanoi(2, 'A', 'C', 'B')
        [('A', 'B'), ('A', 'C'), ('B', 'C')]
    """
    # TODO: Implement Tower of Hanoi solution
    pass
