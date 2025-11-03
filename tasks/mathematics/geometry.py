"""
Geometry Tasks

Practice geometric calculations and problems.
"""

import math


def distance_2d(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points in 2D space.
    
    Args:
        x1, y1 (float): Coordinates of first point
        x2, y2 (float): Coordinates of second point
        
    Returns:
        float: Distance between the points
        
    Example:
        >>> distance_2d(0, 0, 3, 4)
        5.0
    """
    # TODO: Implement 2D distance calculation
    pass


def triangle_area(base, height):
    """
    Calculate the area of a triangle given base and height.
    
    Args:
        base (float): Length of base
        height (float): Height of triangle
        
    Returns:
        float: Area of triangle
        
    Example:
        >>> triangle_area(10, 5)
        25.0
    """
    # TODO: Implement triangle area calculation
    pass


def circle_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius (float): Radius of circle
        
    Returns:
        float: Area of circle
        
    Example:
        >>> round(circle_area(5), 2)
        78.54
    """
    # TODO: Implement circle area calculation
    pass


def circle_circumference(radius):
    """
    Calculate the circumference of a circle.
    
    Args:
        radius (float): Radius of circle
        
    Returns:
        float: Circumference of circle
        
    Example:
        >>> round(circle_circumference(5), 2)
        31.42
    """
    # TODO: Implement circle circumference calculation
    pass


def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): Length of rectangle
        width (float): Width of rectangle
        
    Returns:
        float: Area of rectangle
        
    Example:
        >>> rectangle_area(5, 3)
        15
    """
    # TODO: Implement rectangle area calculation
    pass


def is_right_triangle(a, b, c):
    """
    Check if three sides can form a right triangle (Pythagorean theorem).
    
    Args:
        a, b, c (float): Three side lengths
        
    Returns:
        bool: True if sides form a right triangle, False otherwise
        
    Example:
        >>> is_right_triangle(3, 4, 5)
        True
        >>> is_right_triangle(5, 12, 13)
        True
        >>> is_right_triangle(1, 2, 3)
        False
    """
    # TODO: Implement right triangle checking
    pass


def polygon_area_shoelace(vertices):
    """
    Calculate area of a polygon using the Shoelace formula.
    
    Args:
        vertices (list): List of (x, y) tuples representing vertices
        
    Returns:
        float: Area of polygon
        
    Example:
        >>> polygon_area_shoelace([(0, 0), (4, 0), (4, 3), (0, 3)])
        12.0
    """
    # TODO: Implement Shoelace formula
    pass


def angle_between_vectors(v1, v2):
    """
    Calculate the angle between two 2D vectors in degrees.
    
    Args:
        v1 (tuple): First vector (x, y)
        v2 (tuple): Second vector (x, y)
        
    Returns:
        float: Angle in degrees
        
    Example:
        >>> round(angle_between_vectors((1, 0), (0, 1)), 2)
        90.0
    """
    # TODO: Implement angle calculation between vectors
    pass
