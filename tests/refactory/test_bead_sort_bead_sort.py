import pytest
from sorts.bead_sort import *


def test_bead_sort_no_errors():
    sequence = [6, 11, 12, 4, 1, 5]
    assert bead_sort(sequence) is not None


def test_bead_sort_return_type():
    sequence = [6, 11, 12, 4, 1, 5]
    assert isinstance(bead_sort(sequence), list)


def test_bead_sort_valid_case():
    sequence = [6, 11, 12, 4, 1, 5]
    expected = [1, 4, 5, 6, 11, 12]
    assert bead_sort(sequence) == expected


def test_bead_sort_all_reverse_order_case():
    sequence = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert bead_sort(sequence) == expected


def test_bead_sort_containing_zero_case():
    sequence = [5, 0, 4, 3]
    expected = [0, 3, 4, 5]
    assert bead_sort(sequence) == expected


def test_bead_sort_negative_cases():
    with pytest.raises(TypeError):
        bead_sort([1, 0.9, 0.0, 0, -1, -0.9])

    with pytest.raises(TypeError):
        bead_sort("Hello world")
