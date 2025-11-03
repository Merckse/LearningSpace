"""
Number Theory Solutions
"""


def is_prime(n):
    """Check if number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """Find all primes up to n using Sieve of Eratosthenes."""
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]


def gcd(a, b):
    """Calculate GCD using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Calculate LCM."""
    return abs(a * b) // gcd(a, b)


def prime_factorization(n):
    """Find prime factorization of n."""
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def is_perfect_number(n):
    """Check if number is perfect."""
    if n < 2:
        return False
    
    divisor_sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:
                divisor_sum += n // i
    
    return divisor_sum == n


def nth_fibonacci_modulo(n, mod):
    """Calculate nth Fibonacci number modulo mod efficiently."""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod
    
    return b
