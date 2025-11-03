"""
Dynamic Programming Tasks

Practice solving optimization problems using dynamic programming.
"""


def fibonacci_dp(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Use memoization or tabulation to avoid redundant calculations.
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Example:
        >>> fibonacci_dp(10)
        55
        >>> fibonacci_dp(50)
        12586269025
    """
    # TODO: Implement Fibonacci with dynamic programming
    pass


def knapsack_01(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem.
    
    Given weights and values of n items, put items in a knapsack of
    capacity W to get maximum total value. Each item can be used at most once.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values
        capacity (int): Maximum capacity of knapsack
        
    Returns:
        int: Maximum value that can be obtained
        
    Example:
        >>> knapsack_01([1, 2, 3], [10, 15, 40], 5)
        55
    """
    # TODO: Implement 0/1 Knapsack problem
    pass


def longest_common_subsequence(str1, str2):
    """
    Find the length of longest common subsequence of two strings.
    
    A subsequence is a sequence that appears in the same relative order,
    but not necessarily contiguous.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        int: Length of longest common subsequence
        
    Example:
        >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
        4
    """
    # TODO: Implement longest common subsequence
    pass


def coin_change(coins, amount):
    """
    Find minimum number of coins needed to make the given amount.
    
    You have an infinite supply of each coin denomination.
    Return -1 if amount cannot be made.
    
    Args:
        coins (list): List of coin denominations
        amount (int): Target amount
        
    Returns:
        int: Minimum number of coins needed, or -1 if impossible
        
    Example:
        >>> coin_change([1, 2, 5], 11)
        3
        >>> coin_change([2], 3)
        -1
    """
    # TODO: Implement coin change problem
    pass


def longest_increasing_subsequence(arr):
    """
    Find the length of the longest increasing subsequence.
    
    Args:
        arr (list): List of integers
        
    Returns:
        int: Length of longest increasing subsequence
        
    Example:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4
    """
    # TODO: Implement longest increasing subsequence
    pass


def edit_distance(str1, str2):
    """
    Calculate the minimum edit distance (Levenshtein distance) between two strings.
    
    Operations allowed: insert, delete, replace a character.
    
    Args:
        str1 (str): First string
        str2 (str): Second string
        
    Returns:
        int: Minimum number of operations needed
        
    Example:
        >>> edit_distance("kitten", "sitting")
        3
    """
    # TODO: Implement edit distance
    pass
