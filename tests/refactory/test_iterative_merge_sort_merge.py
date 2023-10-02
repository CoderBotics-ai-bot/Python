from sorts.iterative_merge_sort import *

import pytest
from typing import List


def test_merge_simple():
    assert merge([4, 1, 3, 2], 0, 2, 3) is not None


@pytest.mark.parametrize(
    "input_list, low, mid, high, expected",
    [
        ([1, 2, 3, 4], 0, 2, 3, [1, 2, 3, 4]),
        ([], 0, 0, 0, []),
        ([1], 0, 0, 0, [1]),
        ([1, 1, 1, 1], 0, 2, 3, [1, 1, 1, 1]),
    ],
)
def test_merge_various(
    input_list: List[int], low: int, mid: int, high: int, expected: List[int]
):
    assert merge(input_list, low, mid, high) == expected
