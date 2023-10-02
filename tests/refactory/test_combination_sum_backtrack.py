from backtracking.combination_sum import *
import pytest


def test_backtrack_no_errors():
    """Check if the function runs without errors with valid inputs"""
    candidates = [2, 3, 6, 7]
    path = []
    answer = []
    target = 7
    previous_index = 0
    try:
        backtrack(candidates, path, answer, target, previous_index)
    except Exception as e:
        pytest.fail(f"backtrack() raised {type(e).__name__} with message {str(e)}")

    assert isinstance(answer, list)


def test_backtrack_empty_candidates():
    """Check if the function runs and correctly handles an empty candidates list"""
    candidates = []
    path = []
    answer = []
    target = 7
    previous_index = 0
    backtrack(candidates, path, answer, target, previous_index)

    assert answer == []


def test_backtrack_zero_target():
    """Check if the function correctly handles a zero target value"""
    candidates = [2, 3, 6, 7]
    path = []
    answer = []
    target = 0
    previous_index = 0
    backtrack(candidates, path, answer, target, previous_index)

    assert isinstance(answer, list)
    assert answer == [[]]
