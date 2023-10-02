from searches.quick_select import *


import random
import pytest


def test_quick_select_no_error():
    result = quick_select([2, 4, 5, 7, 899, 54, 32], 5)
    assert result is not None


def test_quick_select_with_negative_index():
    result = quick_select([2, 4, 5, 7, 899, 54, 32], -1)
    assert result is None


def test_quick_select_with_index_out_of_range():
    result = quick_select([2, 4, 5, 7, 899, 54, 32], 10)
    assert result is None


def test_quick_select_with_empty_list():
    result = quick_select([], 0)
    assert result is None


def test_quick_select_with_single_element_list():
    result = quick_select([1], 0)
    assert result is not None


def test_quick_select_execution():
    for _ in range(10):
        # random list with random index
        lst = [random.randint(1, 100) for _ in range(50)]
        idx = random.randint(0, 49)

        # the function shouldn't fail
        try:
            quick_select(lst, idx)
        except Exception:
            assert False, "The function failed"
