#import random
#from searches.quick_select import *
#
#import pytest
#from typing import List, Tuple
#
#
#@pytest.fixture
#def data():
#    return [random.randint(0, 100) for _ in range(10)]
#
#
#def test_partition_no_errors(data):
#    pivot = random.choice(data)
#    result = _partition(data, pivot)
#    assert result is not None
#
#
#def test_partition_basic(data):
#    pivot = random.choice(data)
#    less, equal, greater = _partition(data, pivot)
#    assert all(x < pivot for x in less)
#    assert all(x == pivot for x in equal)
#    assert all(x > pivot for x in greater)
#
#
#def test_partition_partitioning():
#    data = [i for i in range(10)]
#    pivot = 5
#    less, equal, greater = _partition(data, pivot)
#    assert less == [i for i in range(5)]
#    assert equal == [5]
#    assert greater == [i for i in range(6, 10)]
#
#
#@pytest.mark.parametrize(
#    "data,pivot,expected",
#    [
#        ([], 1, ([], [], [])),
#        ([1, 1, 1, 1, 1], 1, ([], [1, 1, 1, 1, 1], [])),
#        ([1, 2, 3, 4, 5], 3, ([1, 2], [3], [4, 5])),
#    ],
#)
#def test_partition_edge_cases(
#    data: List[int], pivot: int, expected: Tuple[List[int], List[int], List[int]]
#):
#    assert (
#        _partition(data, pivot) == expected
#    ), f"Expected {expected}, but got {_partition(data, pivot)}"
#