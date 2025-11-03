#!/usr/bin/env python
"""
Example runner script to test your implementations.

Usage:
    python run_example.py

This script demonstrates how to import and test your task implementations.
"""

import sys
from pathlib import Path

# You can test your implementations by importing from tasks
# When you implement the functions, uncomment these lines:

# Example 1: Testing sorting algorithms
# from tasks.algorithms.sorting import bubble_sort
# result = bubble_sort([64, 34, 25, 12, 22, 11, 90])
# print(f"Bubble sort result: {result}")
# expected = [11, 12, 22, 25, 34, 64, 90]
# print(f"Expected: {expected}")
# print(f"Correct: {result == expected}\n")

# Example 2: Testing recursion
# from tasks.algorithms.recursion import fibonacci
# result = fibonacci(10)
# print(f"Fibonacci(10) = {result}")
# print(f"Expected: 55")
# print(f"Correct: {result == 55}\n")

# Example 3: Testing number theory
# from tasks.mathematics.number_theory import is_prime
# print(f"Is 7 prime? {is_prime(7)}")
# print(f"Is 10 prime? {is_prime(10)}\n")

# Example 4: Testing NumPy basics
# from tasks.data_analysis.numpy_basics import create_array_from_list
# import numpy as np
# arr = create_array_from_list([1, 2, 3, 4, 5])
# print(f"Created array: {arr}")
# print(f"Array type: {type(arr)}\n")


def run_solution_examples():
    """
    Run examples using the provided solutions.
    This shows you what the expected behavior looks like.
    """
    print("=" * 60)
    print("SOLUTION EXAMPLES")
    print("=" * 60 + "\n")
    
    # Add solutions to path
    sys.path.insert(0, str(Path(__file__).parent / 'solutions'))
    
    # Example 1: Sorting
    print("1. Sorting Algorithms")
    print("-" * 40)
    from algorithms.sorting import bubble_sort, quick_sort
    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {data}")
    print(f"Bubble sort: {bubble_sort(data)}")
    print(f"Quick sort: {quick_sort(data)}\n")
    
    # Example 2: Recursion
    print("2. Recursion")
    print("-" * 40)
    from algorithms.recursion import fibonacci, factorial
    print(f"Fibonacci(10) = {fibonacci(10)}")
    print(f"Factorial(5) = {factorial(5)}\n")
    
    # Example 3: Number Theory
    print("3. Number Theory")
    print("-" * 40)
    from mathematics.number_theory import is_prime, gcd, lcm
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    print(f"LCM(12, 18) = {lcm(12, 18)}\n")
    
    # Example 4: Statistics
    print("4. Statistics")
    print("-" * 40)
    from mathematics.statistics import mean, median, standard_deviation
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    print(f"Data: {data}")
    print(f"Mean: {mean(data)}")
    print(f"Median: {median(data)}")
    print(f"Std Dev: {standard_deviation(data)}\n")
    
    # Example 5: NumPy
    print("5. NumPy Operations")
    print("-" * 40)
    from data_analysis.numpy_basics import create_array_from_list, normalize_array
    import numpy as np
    data = [10, 20, 30, 40, 50]
    arr = create_array_from_list(data)
    print(f"Original: {data}")
    print(f"Array: {arr}")
    print(f"Normalized: {normalize_array(arr)}\n")
    
    # Example 6: Pandas
    print("6. Pandas Operations")
    print("-" * 40)
    from data_analysis.pandas_basics import create_dataframe_from_dict, filter_dataframe
    import pandas as pd
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
    df = create_dataframe_from_dict(data)
    print(f"DataFrame:\n{df}")
    print(f"\nFiltered (Age > 28):\n{filter_dataframe(df, 'Age', 28)}\n")
    
    # Example 7: Dynamic Programming
    print("7. Dynamic Programming")
    print("-" * 40)
    from algorithms.dynamic_programming import fibonacci_dp, coin_change
    print(f"Fibonacci(50) using DP = {fibonacci_dp(50)}")
    print(f"Min coins for 11 cents with [1,2,5]: {coin_change([1, 2, 5], 11)}\n")
    
    print("=" * 60)
    print("TIP: Try implementing these in the tasks/ directory!")
    print("Run 'python -m pytest tests/' to test your implementations")
    print("=" * 60)


if __name__ == "__main__":
    print("\n")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║         Welcome to LearningSpace Examples!              ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print("\n")
    
    run_solution_examples()
    
    print("\n")
    print("Next Steps:")
    print("1. Open a task file in the tasks/ directory")
    print("2. Implement the function")
    print("3. Test it: python -m pytest tests/")
    print("4. Compare with solutions/ if needed")
    print("\nHappy Learning! 🐍\n")
