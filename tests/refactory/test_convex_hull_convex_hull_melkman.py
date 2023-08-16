from divide_and_conquer.convex_hull import *
import pytest


def test_convex_hull_melkman():
    # Test 1: Normal case, 3 disparate points
    result = convex_hull_melkman([Point(0, 0), Point(1, 0), Point(10, 1)])
    assert result == [
        Point(0.0, 0.0),
        Point(1.0, 0.0),
        Point(10.0, 1.0),
    ], "Test 1 failed."

    # Test 2: Normal case, points on the same line
    result = convex_hull_melkman([Point(0, 0), Point(1, 0), Point(10, 0)])
    assert result == [Point(0.0, 0.0), Point(10.0, 0.0)], "Test 2 failed."

    # Test 3: Complex case, multiple points
    result = convex_hull_melkman(
        [
            Point(-1, 1),
            Point(-1, -1),
            Point(0, 0),
            Point(0.5, 0.5),
            Point(1, -1),
            Point(1, 1),
            Point(-0.75, 1),
        ]
    )
    assert result == [
        Point(-1.0, -1.0),
        Point(-1.0, 1.0),
        Point(1.0, -1.0),
        Point(1.0, 1.0),
    ], "Test 3 failed."

    # Test 4: Complex case, multiple points with negative y-coordinate
    result = convex_hull_melkman(
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
    )
    assert result == [
        Point(0.0, 0.0),
        Point(0.0, 3.0),
        Point(1.0, -3.0),
        Point(2.0, -4.0),
        Point(3.0, 0.0),
        Point(3.0, 3.0),
    ], "Test 4 failed."
