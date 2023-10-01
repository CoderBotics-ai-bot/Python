
import pytest
from typing import List, Tuple
from dynamic_programming.combination_sum_iv import *


@pytest.mark.parametrize(
    "n, array, target, expected",
    [
        (3, [1, 2, 5], 5, 9),  # test case from docstring
        (3, [1, 2, 3], 4, 7),  # more combinations
        (1, [2], 3, 0),  # no combinations
        (3, [1, 2, 5], 0, 1),  # target is 0
        (0, [], 5, 0),  # empty array
    ],
)
def test_combination_sum_iv_bottom_up(
    n: int, array: List[int], target: int, expected: int
):
    result = combination_sum_iv_bottom_up(n, array, target)
    assert result is not None
    assert type(result) is int
    assert result == expected
