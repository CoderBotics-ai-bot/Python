from sorts.msd_radix_sort import *
import pytest


import pytest


def test_msd_radix_sort_no_errors():
    try:
        msd_radix_sort([40, 12, 1, 100, 4])
    except Exception as e:
        pytest.fail(f"Test failed because an error was thrown: {e}")


def test_msd_radix_sort_not_none():
    assert msd_radix_sort([5, 40, 12, 1, 100, 4]) is not None


def test_msd_radix_sort_empty_list():
    sorted_list = msd_radix_sort([])
    assert sorted_list == []


def test_msd_radix_sort_single_element_list():
    single_element_list = [3]
    assert msd_radix_sort(single_element_list) == single_element_list


def test_msd_radix_sort_negative_number():
    with pytest.raises(ValueError, match="All numbers must be positive"):
        msd_radix_sort([-1, 34, 45])
