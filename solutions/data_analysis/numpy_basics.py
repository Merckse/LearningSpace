"""
NumPy Basics Solutions
"""

import numpy as np


def create_array_from_list(lst):
    """Convert list to numpy array."""
    return np.array(lst)


def create_zeros_array(shape):
    """Create zeros array."""
    return np.zeros(shape)


def create_range_array(start, stop, step):
    """Create range array."""
    return np.arange(start, stop, step)


def reshape_array(arr, new_shape):
    """Reshape array."""
    return arr.reshape(new_shape)


def array_statistics(arr):
    """Calculate array statistics."""
    return {
        'mean': float(np.mean(arr)),
        'median': float(np.median(arr)),
        'std': float(np.std(arr)),
        'min': float(np.min(arr)),
        'max': float(np.max(arr))
    }


def matrix_multiplication(a, b):
    """Perform matrix multiplication."""
    return np.matmul(a, b)


def normalize_array(arr):
    """Normalize array to [0, 1]."""
    min_val = np.min(arr)
    max_val = np.max(arr)
    return (arr - min_val) / (max_val - min_val)


def boolean_indexing(arr, threshold):
    """Filter array using boolean indexing."""
    return arr[arr > threshold]
