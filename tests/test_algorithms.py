"""
Tests for algorithm solutions
"""

import pytest
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'solutions'))

from algorithms import sorting, searching, recursion, dynamic_programming


class TestSorting:
    """Test sorting algorithms"""
    
    def test_bubble_sort(self):
        assert sorting.bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
        assert sorting.bubble_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
        assert sorting.bubble_sort([1]) == [1]
        assert sorting.bubble_sort([]) == []
    
    def test_merge_sort(self):
        assert sorting.merge_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
        assert sorting.merge_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
        assert sorting.merge_sort([1]) == [1]
        assert sorting.merge_sort([]) == []
    
    def test_quick_sort(self):
        assert sorting.quick_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
        assert sorting.quick_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]
        assert sorting.quick_sort([1]) == [1]
        assert sorting.quick_sort([]) == []
    
    def test_insertion_sort(self):
        assert sorting.insertion_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
        assert sorting.insertion_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]


class TestSearching:
    """Test searching algorithms"""
    
    def test_linear_search(self):
        assert searching.linear_search([4, 2, 7, 1, 9, 5], 7) == 2
        assert searching.linear_search([4, 2, 7, 1, 9, 5], 10) == -1
        assert searching.linear_search([1, 2, 3], 1) == 0
    
    def test_binary_search(self):
        assert searching.binary_search([1, 2, 4, 5, 7, 9], 7) == 4
        assert searching.binary_search([1, 2, 4, 5, 7, 9], 10) == -1
        assert searching.binary_search([1, 2, 3, 4, 5], 1) == 0
    
    def test_binary_search_recursive(self):
        assert searching.binary_search_recursive([1, 2, 4, 5, 7, 9], 7) == 4
        assert searching.binary_search_recursive([1, 2, 4, 5, 7, 9], 10) == -1
    
    def test_find_first_occurrence(self):
        assert searching.find_first_occurrence([1, 2, 2, 2, 3, 4, 5], 2) == 1
        assert searching.find_first_occurrence([1, 1, 1, 1], 1) == 0


class TestRecursion:
    """Test recursion functions"""
    
    def test_fibonacci(self):
        assert recursion.fibonacci(0) == 0
        assert recursion.fibonacci(1) == 1
        assert recursion.fibonacci(5) == 5
        assert recursion.fibonacci(10) == 55
    
    def test_factorial(self):
        assert recursion.factorial(0) == 1
        assert recursion.factorial(5) == 120
        assert recursion.factorial(10) == 3628800
    
    def test_power(self):
        assert recursion.power(2, 3) == 8
        assert recursion.power(5, 0) == 1
        assert recursion.power(3, 4) == 81
    
    def test_sum_digits(self):
        assert recursion.sum_digits(123) == 6
        assert recursion.sum_digits(9875) == 29
        assert recursion.sum_digits(0) == 0
    
    def test_reverse_string(self):
        assert recursion.reverse_string("hello") == "olleh"
        assert recursion.reverse_string("Python") == "nohtyP"
        assert recursion.reverse_string("a") == "a"
    
    def test_tower_of_hanoi(self):
        moves = recursion.tower_of_hanoi(2, 'A', 'C', 'B')
        assert moves == [('A', 'B'), ('A', 'C'), ('B', 'C')]
        assert len(recursion.tower_of_hanoi(3, 'A', 'C', 'B')) == 7


class TestDynamicProgramming:
    """Test dynamic programming solutions"""
    
    def test_fibonacci_dp(self):
        assert dynamic_programming.fibonacci_dp(10) == 55
        assert dynamic_programming.fibonacci_dp(50) == 12586269025
    
    def test_knapsack(self):
        assert dynamic_programming.knapsack_01([1, 2, 3], [10, 15, 40], 5) == 55
        assert dynamic_programming.knapsack_01([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
    
    def test_longest_common_subsequence(self):
        assert dynamic_programming.longest_common_subsequence("AGGTAB", "GXTXAYB") == 4
        assert dynamic_programming.longest_common_subsequence("ABC", "ABC") == 3
    
    def test_coin_change(self):
        assert dynamic_programming.coin_change([1, 2, 5], 11) == 3
        assert dynamic_programming.coin_change([2], 3) == -1
        assert dynamic_programming.coin_change([1], 0) == 0
    
    def test_longest_increasing_subsequence(self):
        assert dynamic_programming.longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    
    def test_edit_distance(self):
        assert dynamic_programming.edit_distance("kitten", "sitting") == 3
        assert dynamic_programming.edit_distance("", "abc") == 3
