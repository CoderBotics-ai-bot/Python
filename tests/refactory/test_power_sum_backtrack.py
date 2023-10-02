import pytest
from backtracking.power_sum import *


def test_backtrack_no_error():
    result = backtrack(100, 2, 1, 0, 0)
    assert result is not None


def test_backtrack_base_case():
    _, solution_count = backtrack(13, 2, 1, 0, 0)
    assert solution_count == 1


def test_backtrack_multiple_solutions():
    _, solution_count = backtrack(100, 2, 1, 0, 0)
    assert solution_count == 3


def test_backtrack_no_solution():
    _, solution_count = backtrack(1000, 10, 1, 0, 0)
    assert solution_count == 0


def test_backtrack_solution_difference():
    _, solution_count1 = backtrack(400, 2, 1, 0, 0)
    _, solution_count2 = backtrack(800, 2, 1, 0, 0)
    assert abs(solution_count2 - solution_count1) == 506


def test_backtrack_power_difference():
    _, solution_count1 = backtrack(100, 2, 1, 0, 0)
    _, solution_count2 = backtrack(100, 3, 1, 0, 0)
    assert solution_count1 > solution_count2
