from matrix.count_negative_numbers_in_sorted_matrix import *
import pytest


def test_count_negatives_brute_force_no_errors():
    assert count_negatives_brute_force([[1, -1], [2, -2]]) is not None


def test_count_negatives_brute_force_all_positive():
    assert count_negatives_brute_force([[1, 2, 3], [4, 5, 6]]) == 0


def test_count_negatives_brute_force_all_negative():
    assert count_negatives_brute_force([[-1, -2, -3], [-4, -5, -6]]) == 6


def test_count_negatives_brute_force_mixed_elements():
    assert count_negatives_brute_force([[1, -1], [2, -2]]) == 2


def test_count_negatives_brute_force_multiple_negative_elements():
    assert count_negatives_brute_force([[-1, -1, -1], [-2, -2, -2]]) == 6


def test_count_negatives_brute_force_no_elements():
    assert count_negatives_brute_force([[]]) == 0
