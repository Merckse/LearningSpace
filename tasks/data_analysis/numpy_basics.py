"""
NumPy Basics Tasks

Practice fundamental NumPy operations for numerical computing.
"""

import numpy as np


def create_array_from_list(lst):
    """
    Convert a Python list to a NumPy array.
    
    Args:
        lst (list): Python list
        
    Returns:
        np.ndarray: NumPy array
        
    Example:
        >>> arr = create_array_from_list([1, 2, 3, 4, 5])
        >>> type(arr).__name__
        'ndarray'
    """
    # TODO: Convert list to numpy array
    pass


def create_zeros_array(shape):
    """
    Create an array filled with zeros.
    
    Args:
        shape (tuple): Shape of the array
        
    Returns:
        np.ndarray: Array of zeros
        
    Example:
        >>> create_zeros_array((2, 3)).shape
        (2, 3)
    """
    # TODO: Create zeros array
    pass


def create_range_array(start, stop, step):
    """
    Create an array with evenly spaced values.
    
    Args:
        start (int): Start value
        stop (int): Stop value (exclusive)
        step (int): Step size
        
    Returns:
        np.ndarray: Array of values
        
    Example:
        >>> list(create_range_array(0, 10, 2))
        [0, 2, 4, 6, 8]
    """
    # TODO: Create range array using np.arange
    pass


def reshape_array(arr, new_shape):
    """
    Reshape an array to a new shape.
    
    Args:
        arr (np.ndarray): Input array
        new_shape (tuple): New shape
        
    Returns:
        np.ndarray: Reshaped array
        
    Example:
        >>> arr = np.array([1, 2, 3, 4, 5, 6])
        >>> reshape_array(arr, (2, 3)).shape
        (2, 3)
    """
    # TODO: Reshape the array
    pass


def array_statistics(arr):
    """
    Calculate basic statistics of an array.
    
    Args:
        arr (np.ndarray): Input array
        
    Returns:
        dict: Dictionary with 'mean', 'median', 'std', 'min', 'max'
        
    Example:
        >>> stats = array_statistics(np.array([1, 2, 3, 4, 5]))
        >>> stats['mean']
        3.0
    """
    # TODO: Calculate and return statistics
    pass


def matrix_multiplication(a, b):
    """
    Perform matrix multiplication.
    
    Args:
        a (np.ndarray): First matrix
        b (np.ndarray): Second matrix
        
    Returns:
        np.ndarray: Result of a @ b
        
    Example:
        >>> a = np.array([[1, 2], [3, 4]])
        >>> b = np.array([[5, 6], [7, 8]])
        >>> matrix_multiplication(a, b).tolist()
        [[19, 22], [43, 50]]
    """
    # TODO: Perform matrix multiplication
    pass


def normalize_array(arr):
    """
    Normalize an array to range [0, 1].
    
    Formula: (x - min(x)) / (max(x) - min(x))
    
    Args:
        arr (np.ndarray): Input array
        
    Returns:
        np.ndarray: Normalized array
        
    Example:
        >>> normalize_array(np.array([10, 20, 30, 40, 50])).tolist()
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # TODO: Normalize the array
    pass


def boolean_indexing(arr, threshold):
    """
    Return elements greater than threshold using boolean indexing.
    
    Args:
        arr (np.ndarray): Input array
        threshold (float): Threshold value
        
    Returns:
        np.ndarray: Elements > threshold
        
    Example:
        >>> boolean_indexing(np.array([1, 5, 3, 8, 2, 9]), 4).tolist()
        [5, 8, 9]
    """
    # TODO: Use boolean indexing to filter array
    pass
