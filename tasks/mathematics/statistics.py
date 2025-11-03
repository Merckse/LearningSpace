"""
Statistics Tasks

Practice statistical calculations and analysis.
"""


def mean(numbers):
    """
    Calculate the arithmetic mean (average) of a list of numbers.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Mean of the numbers
        
    Example:
        >>> mean([1, 2, 3, 4, 5])
        3.0
    """
    # TODO: Implement mean calculation
    pass


def median(numbers):
    """
    Calculate the median of a list of numbers.
    
    The median is the middle value when numbers are sorted.
    For even-length lists, return the average of the two middle values.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Median of the numbers
        
    Example:
        >>> median([1, 2, 3, 4, 5])
        3
        >>> median([1, 2, 3, 4])
        2.5
    """
    # TODO: Implement median calculation
    pass


def mode(numbers):
    """
    Calculate the mode (most frequent value) of a list.
    
    If multiple modes exist, return the smallest one.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        int/float: Mode of the numbers
        
    Example:
        >>> mode([1, 2, 2, 3, 4])
        2
        >>> mode([1, 1, 2, 2, 3])
        1
    """
    # TODO: Implement mode calculation
    pass


def variance(numbers):
    """
    Calculate the population variance.
    
    Variance measures how far numbers are spread from their mean.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Variance of the numbers
        
    Example:
        >>> variance([2, 4, 4, 4, 5, 5, 7, 9])
        4.0
    """
    # TODO: Implement variance calculation
    pass


def standard_deviation(numbers):
    """
    Calculate the population standard deviation.
    
    Standard deviation is the square root of variance.
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float: Standard deviation of the numbers
        
    Example:
        >>> standard_deviation([2, 4, 4, 4, 5, 5, 7, 9])
        2.0
    """
    # TODO: Implement standard deviation calculation
    pass


def correlation(x, y):
    """
    Calculate Pearson correlation coefficient between two lists.
    
    Returns a value between -1 and 1 indicating linear correlation.
    
    Args:
        x (list): First list of numbers
        y (list): Second list of numbers (same length as x)
        
    Returns:
        float: Correlation coefficient
        
    Example:
        >>> round(correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]), 2)
        1.0
    """
    # TODO: Implement correlation calculation
    pass


def z_score(value, numbers):
    """
    Calculate the z-score of a value in a dataset.
    
    Z-score indicates how many standard deviations a value is from the mean.
    
    Args:
        value (float): Value to calculate z-score for
        numbers (list): Dataset
        
    Returns:
        float: Z-score
        
    Example:
        >>> z_score(5, [1, 2, 3, 4, 5])
        1.414...
    """
    # TODO: Implement z-score calculation
    pass


def percentile(numbers, p):
    """
    Calculate the p-th percentile of a dataset.
    
    Args:
        numbers (list): List of numbers
        p (float): Percentile to calculate (0-100)
        
    Returns:
        float: Value at the p-th percentile
        
    Example:
        >>> percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50)
        5.5
    """
    # TODO: Implement percentile calculation
    pass
