from divide_and_conquer.convex_hull import *
import pytest
from divide_and_conquer.convex_hull import Point


def test_convex_hull_bf():
    # Test common cases

    assert convex_hull_bf([Point(0, 0), Point(1, 0), Point(10, 1)]) == [
        Point(0.0, 0.0),
        Point(1.0, 0.0),
        Point(10.0, 1.0),
    ]

    assert convex_hull_bf([Point(0, 0), Point(1, 0), Point(10, 0)]) == [
        Point(0.0, 0.0),
        Point(10.0, 0.0),
    ]

    assert convex_hull_bf(
        [
            Point(-1, 1),
            Point(-1, -1),
            Point(0, 0),
            Point(0.5, 0.5),
            Point(1, -1),
            Point(1, 1),
            Point(-0.75, 1),
        ]
    ) == [Point(-1.0, -1.0), Point(-1.0, 1.0), Point(1.0, -1.0), Point(1.0, 1.0)]

    assert convex_hull_bf(
        [
            Point(0, 3),
            Point(2, 2),
            Point(1, 1),
            Point(2, 1),
            Point(3, 0),
            Point(0, 0),
            Point(3, 3),
            Point(2, -1),
            Point(2, -4),
            Point(1, -3),
        ]
    ) == [
        Point(0.0, 0.0),
        Point(0.0, 3.0),
        Point(1.0, -3.0),
        Point(2.0, -4.0),
        Point(3.0, 0.0),
        Point(3.0, 3.0),
    ]

    # Edge case: 2 points
    assert convex_hull_bf([Point(1, 1), Point(2, 2)]) == [
        Point(1.0, 1.0),
        Point(2.0, 2.0),
    ]

    # Edge case: 3 points in a line
    assert convex_hull_bf([Point(1, 1), Point(2, 2), Point(3, 3)]) == [
        Point(1.0, 1.0),
        Point(3.0, 3.0),
    ]
