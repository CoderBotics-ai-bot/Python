from sorts.msd_radix_sort import *
import pytest


def test_msd_radix_sort_inplace_no_errors():
    lst = [4, 23, 78, 56, 1]
    try:
        msd_radix_sort_inplace(lst)
    except Exception as e:
        pytest.fail(f"msd_radix_sort_inplace raised exception {e}")


def test_msd_radix_sort_inplace_not_none():
    lst = [4, 23, 78, 56, 1]
    msd_radix_sort_inplace(lst)
    for item in lst:
        assert item is not None, "The function should not have None values."


def test_msd_radix_sort_inplace_empty_list():
    lst = []
    msd_radix_sort_inplace(lst)
    assert len(lst) == 0, "The list should still be empty after sorting"


def test_msd_radix_sort_inplace_single_element_list():
    lst = [4]
    msd_radix_sort_inplace(lst)
    assert len(lst) == 1, "The list should still contain one element after sorting"
    assert lst == [4], "The list should remain the same after sorting"


def test_msd_radix_sort_inplace_negative_elements():
    lst = [-1, -3, -2]
    with pytest.raises(ValueError):
        msd_radix_sort_inplace(lst)
