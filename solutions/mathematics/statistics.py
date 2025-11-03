"""
Statistics Solutions
"""

import math
from collections import Counter


def mean(numbers):
    """Calculate mean."""
    return sum(numbers) / len(numbers)


def median(numbers):
    """Calculate median."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if n % 2 == 1:
        return sorted_nums[n // 2]
    else:
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        return (mid1 + mid2) / 2


def mode(numbers):
    """Calculate mode."""
    counts = Counter(numbers)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    return min(modes)


def variance(numbers):
    """Calculate population variance."""
    avg = mean(numbers)
    return sum((x - avg) ** 2 for x in numbers) / len(numbers)


def standard_deviation(numbers):
    """Calculate standard deviation."""
    return math.sqrt(variance(numbers))


def correlation(x, y):
    """Calculate Pearson correlation coefficient."""
    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)
    
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    sum_sq_x = sum((xi - mean_x) ** 2 for xi in x)
    sum_sq_y = sum((yi - mean_y) ** 2 for yi in y)
    
    denominator = math.sqrt(sum_sq_x * sum_sq_y)
    
    if denominator == 0:
        return 0
    
    return numerator / denominator


def z_score(value, numbers):
    """Calculate z-score."""
    avg = mean(numbers)
    std = standard_deviation(numbers)
    
    if std == 0:
        return 0
    
    return (value - avg) / std


def percentile(numbers, p):
    """Calculate p-th percentile."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    if p == 100:
        return sorted_nums[-1]
    
    index = (p / 100) * (n - 1)
    lower = int(index)
    upper = lower + 1
    
    if upper >= n:
        return sorted_nums[lower]
    
    weight = index - lower
    return sorted_nums[lower] * (1 - weight) + sorted_nums[upper] * weight
