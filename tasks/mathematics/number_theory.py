"""
Number Theory Tasks

Practice mathematical operations and number theory problems.
"""


def is_prime(n):
    """
    Check if a number is prime.
    
    A prime number is a natural number greater than 1 that has no
    positive divisors other than 1 and itself.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is prime, False otherwise
        
    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    # TODO: Implement prime checking
    pass


def sieve_of_eratosthenes(n):
    """
    Find all prime numbers up to n using Sieve of Eratosthenes.
    
    Args:
        n (int): Upper limit
        
    Returns:
        list: List of all primes up to n
        
    Example:
        >>> sieve_of_eratosthenes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
    """
    # TODO: Implement Sieve of Eratosthenes
    pass


def gcd(a, b):
    """
    Calculate the Greatest Common Divisor using Euclidean algorithm.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: GCD of a and b
        
    Example:
        >>> gcd(48, 18)
        6
        >>> gcd(100, 35)
        5
    """
    # TODO: Implement GCD calculation
    pass


def lcm(a, b):
    """
    Calculate the Least Common Multiple.
    
    Args:
        a (int): First number
        b (int): Second number
        
    Returns:
        int: LCM of a and b
        
    Example:
        >>> lcm(12, 18)
        36
    """
    # TODO: Implement LCM calculation
    pass


def prime_factorization(n):
    """
    Find the prime factorization of a number.
    
    Args:
        n (int): Number to factorize (n > 1)
        
    Returns:
        list: List of prime factors (with repetition)
        
    Example:
        >>> prime_factorization(60)
        [2, 2, 3, 5]
        >>> prime_factorization(17)
        [17]
    """
    # TODO: Implement prime factorization
    pass


def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    
    A perfect number is a positive integer equal to the sum of its
    proper positive divisors (excluding itself).
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is perfect, False otherwise
        
    Example:
        >>> is_perfect_number(6)
        True
        >>> is_perfect_number(28)
        True
        >>> is_perfect_number(12)
        False
    """
    # TODO: Implement perfect number checking
    pass


def nth_fibonacci_modulo(n, mod):
    """
    Calculate the nth Fibonacci number modulo mod efficiently.
    
    Useful for large n values.
    
    Args:
        n (int): Position in sequence
        mod (int): Modulo value
        
    Returns:
        int: nth Fibonacci number mod mod
        
    Example:
        >>> nth_fibonacci_modulo(10, 1000)
        55
    """
    # TODO: Implement efficient Fibonacci modulo
    pass
