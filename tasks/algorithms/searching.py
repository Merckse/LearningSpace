"""
Searching Algorithms Tasks

Practice implementing various searching algorithms.
"""


def linear_search(arr, target):
    """
    Implement linear search algorithm.
    
    Linear search sequentially checks each element of the list until
    the target is found or the list ends.
    
    Args:
        arr (list): List of elements to search
        target: Element to find
        
    Returns:
        int: Index of target if found, -1 otherwise
        
    Example:
        >>> linear_search([4, 2, 7, 1, 9, 5], 7)
        2
        >>> linear_search([4, 2, 7, 1, 9, 5], 10)
        -1
    """
    # TODO: Implement linear search
    pass


def binary_search(arr, target):
    """
    Implement binary search algorithm.
    
    Binary search finds the position of a target value within a sorted array
    by repeatedly dividing the search interval in half.
    
    Args:
        arr (list): Sorted list of elements to search
        target: Element to find
        
    Returns:
        int: Index of target if found, -1 otherwise
        
    Example:
        >>> binary_search([1, 2, 4, 5, 7, 9], 7)
        4
        >>> binary_search([1, 2, 4, 5, 7, 9], 10)
        -1
    """
    # TODO: Implement binary search
    pass


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Implement binary search using recursion.
    
    Args:
        arr (list): Sorted list of elements to search
        target: Element to find
        left (int): Left boundary index
        right (int): Right boundary index
        
    Returns:
        int: Index of target if found, -1 otherwise
        
    Example:
        >>> binary_search_recursive([1, 2, 4, 5, 7, 9], 7)
        4
    """
    # TODO: Implement recursive binary search
    pass


def find_first_occurrence(arr, target):
    """
    Find the first occurrence of target in a sorted array with duplicates.
    
    Args:
        arr (list): Sorted list (may contain duplicates)
        target: Element to find
        
    Returns:
        int: Index of first occurrence, -1 if not found
        
    Example:
        >>> find_first_occurrence([1, 2, 2, 2, 3, 4, 5], 2)
        1
    """
    # TODO: Implement finding first occurrence
    pass
