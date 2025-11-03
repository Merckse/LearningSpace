"""
Tests for mathematics solutions
"""

import pytest
import sys
from pathlib import Path

# Add solutions directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'solutions'))

from mathematics import number_theory, geometry, statistics


class TestNumberTheory:
    """Test number theory functions"""
    
    def test_is_prime(self):
        assert number_theory.is_prime(7)
        assert not number_theory.is_prime(10)
        assert number_theory.is_prime(2)
        assert not number_theory.is_prime(1)
        assert number_theory.is_prime(13)
    
    def test_sieve_of_eratosthenes(self):
        assert number_theory.sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
        assert number_theory.sieve_of_eratosthenes(10) == [2, 3, 5, 7]
    
    def test_gcd(self):
        assert number_theory.gcd(48, 18) == 6
        assert number_theory.gcd(100, 35) == 5
        assert number_theory.gcd(17, 19) == 1
    
    def test_lcm(self):
        assert number_theory.lcm(12, 18) == 36
        assert number_theory.lcm(4, 5) == 20
    
    def test_prime_factorization(self):
        assert number_theory.prime_factorization(60) == [2, 2, 3, 5]
        assert number_theory.prime_factorization(17) == [17]
        assert number_theory.prime_factorization(100) == [2, 2, 5, 5]
    
    def test_is_perfect_number(self):
        assert number_theory.is_perfect_number(6)
        assert number_theory.is_perfect_number(28)
        assert not number_theory.is_perfect_number(12)
    
    def test_nth_fibonacci_modulo(self):
        assert number_theory.nth_fibonacci_modulo(10, 1000) == 55
        assert number_theory.nth_fibonacci_modulo(100, 100) == 75


class TestGeometry:
    """Test geometry functions"""
    
    def test_distance_2d(self):
        assert geometry.distance_2d(0, 0, 3, 4) == 5.0
        assert abs(geometry.distance_2d(0, 0, 1, 1) - 1.414213) < 0.001
    
    def test_triangle_area(self):
        assert geometry.triangle_area(10, 5) == 25.0
        assert geometry.triangle_area(6, 4) == 12.0
    
    def test_circle_area(self):
        assert abs(geometry.circle_area(5) - 78.54) < 0.01
        assert abs(geometry.circle_area(1) - 3.14159) < 0.001
    
    def test_circle_circumference(self):
        assert abs(geometry.circle_circumference(5) - 31.42) < 0.01
    
    def test_rectangle_area(self):
        assert geometry.rectangle_area(5, 3) == 15
        assert geometry.rectangle_area(10, 10) == 100
    
    def test_is_right_triangle(self):
        assert geometry.is_right_triangle(3, 4, 5)
        assert geometry.is_right_triangle(5, 12, 13)
        assert not geometry.is_right_triangle(1, 2, 3)
    
    def test_polygon_area_shoelace(self):
        assert geometry.polygon_area_shoelace([(0, 0), (4, 0), (4, 3), (0, 3)]) == 12.0
        assert geometry.polygon_area_shoelace([(0, 0), (2, 0), (2, 2), (0, 2)]) == 4.0
    
    def test_angle_between_vectors(self):
        assert abs(geometry.angle_between_vectors((1, 0), (0, 1)) - 90.0) < 0.01
        assert abs(geometry.angle_between_vectors((1, 0), (1, 0)) - 0.0) < 0.01


class TestStatistics:
    """Test statistics functions"""
    
    def test_mean(self):
        assert statistics.mean([1, 2, 3, 4, 5]) == 3.0
        assert statistics.mean([10, 20, 30]) == 20.0
    
    def test_median(self):
        assert statistics.median([1, 2, 3, 4, 5]) == 3
        assert statistics.median([1, 2, 3, 4]) == 2.5
    
    def test_mode(self):
        assert statistics.mode([1, 2, 2, 3, 4]) == 2
        assert statistics.mode([1, 1, 2, 2, 3]) == 1
    
    def test_variance(self):
        assert statistics.variance([2, 4, 4, 4, 5, 5, 7, 9]) == 4.0
    
    def test_standard_deviation(self):
        assert statistics.standard_deviation([2, 4, 4, 4, 5, 5, 7, 9]) == 2.0
    
    def test_correlation(self):
        result = statistics.correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        assert abs(result - 1.0) < 0.001
    
    def test_z_score(self):
        result = statistics.z_score(5, [1, 2, 3, 4, 5])
        assert abs(result - 1.414) < 0.01
    
    def test_percentile(self):
        assert statistics.percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50) == 5.5
