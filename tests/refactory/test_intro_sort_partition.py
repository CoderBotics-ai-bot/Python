from sorts.intro_sort import *
import pytest


def test_partition_no_throw():
    array = [1, 2, 3, 4]
    assert partition(array, 0, len(array), 2) is not None


def test_partition_pivot_in_array():
    array = [4, 2, 6, 8, 1, 7, 8]
    assert partition(array, 0, len(array) - 1, 2) == 1


def test_partition_empty_array():
    array = []
    with pytest.raises(IndexError):
        partition(array, 0, len(array) - 1, 2)


def test_partition_pivot_not_in_array():
    array = [4, 7, 6, 8, 1, 7, 9]
    assert partition(array, 0, len(array) - 1, 5) is not None
