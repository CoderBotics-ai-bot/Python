"""
This is a pure Python implementation of the merge-insertion sort algorithm
Source: https://en.wikipedia.org/wiki/Graham_scan

For doctests run following command:
python3 -m doctest -v graham_scan.py
"""

from __future__ import annotations

from collections import deque
from enum import Enum
from math import atan2, degrees
from sys import maxsize


from typing import List, Tuple


# traversal from the lowest and the most left point in anti-clockwise direction
# if direction gets right, the previous point is not the convex hull.
class Direction(Enum):
    left = 1
    straight = 2
    right = 3

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


def angle_comparer(point: tuple[int, int], minx: int, miny: int) -> float:
    """Return the angle toward to point from (minx, miny)

    :param point: The target point
           minx: The starting point's x
           miny: The starting point's y
    :return: the angle

    Examples:
    >>> angle_comparer((1,1), 0, 0)
    45.0

    >>> angle_comparer((100,1), 10, 10)
    -5.710593137499642

    >>> angle_comparer((5,5), 2, 3)
    33.690067525979785
    """
    # sort the points accorgind to the angle from the lowest and the most left point
    x, y = point
    return degrees(atan2(y - miny, x - minx))


def check_direction(
    starting: tuple[int, int], via: tuple[int, int], target: tuple[int, int]
) -> Direction:
    """Return the direction toward to the line from via to target from starting

    :param starting: The starting point
           via: The via point
           target: The target point
    :return: the Direction

    Examples:
    >>> check_direction((1,1), (2,2), (3,3))
    Direction.straight

    >>> check_direction((60,1), (-50,199), (30,2))
    Direction.left

    >>> check_direction((0,0), (5,5), (10,0))
    Direction.right
    """
    x0, y0 = starting
    x1, y1 = via
    x2, y2 = target
    via_angle = degrees(atan2(y1 - y0, x1 - x0))
    via_angle %= 360
    target_angle = degrees(atan2(y2 - y0, x2 - x0))
    target_angle %= 360
    # t-
    #  \ \
    #   \ v
    #    \|
    #     s
    # via_angle is always lower than target_angle, if direction is left.
    # If they are same, it means they are on a same line of convex hull.
    if target_angle > via_angle:
        return Direction.left
    elif target_angle == via_angle:
        return Direction.straight
    else:
        return Direction.right

def graham_scan(points: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Pure implementation of graham scan algorithm in Python.

    :param points: The unique points on coordinates.
    :return: The points on convex hull.
    """
    # guard conditions for small input
    if len(points) <= 2:
        raise ValueError("graham_scan: argument must contain more than 2 points.")
    if len(points) == 3:
        return points

    # find min point and sort points by angle
    start = min(points, key=lambda p: (p[1], p[0]))
    points.remove(start)
    sorted_points = sorted(points, key=lambda p: (-p[1] / p[0], p[0]))
    sorted_points.insert(0, start)

    # main algorithm
    stack = [sorted_points[i] for i in range(3)]
    for i in range(3, len(sorted_points)):
        while is_clockwise(stack[-2], stack[-1], sorted_points[i]):
            stack.pop()
        stack.append(sorted_points[i])
    return list(stack)


def is_clockwise(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    """Check if three points makes a clockwise turn"""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) < 0
