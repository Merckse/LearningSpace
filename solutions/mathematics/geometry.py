"""
Geometry Solutions
"""

import math


def distance_2d(x1, y1, x2, y2):
    """Calculate Euclidean distance in 2D."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def triangle_area(base, height):
    """Calculate triangle area."""
    return 0.5 * base * height


def circle_area(radius):
    """Calculate circle area."""
    return math.pi * radius ** 2


def circle_circumference(radius):
    """Calculate circle circumference."""
    return 2 * math.pi * radius


def rectangle_area(length, width):
    """Calculate rectangle area."""
    return length * width


def is_right_triangle(a, b, c):
    """Check if sides form a right triangle."""
    sides = sorted([a, b, c])
    return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-9


def polygon_area_shoelace(vertices):
    """Calculate polygon area using Shoelace formula."""
    n = len(vertices)
    area = 0
    
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]
    
    return abs(area) / 2


def angle_between_vectors(v1, v2):
    """Calculate angle between two 2D vectors in degrees."""
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    
    cos_angle = dot_product / (magnitude1 * magnitude2)
    # Clamp to avoid floating point errors
    cos_angle = max(-1, min(1, cos_angle))
    
    angle_rad = math.acos(cos_angle)
    return math.degrees(angle_rad)
