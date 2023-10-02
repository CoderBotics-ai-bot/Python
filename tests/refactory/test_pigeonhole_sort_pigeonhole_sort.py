from sorts.pigeonhole_sort import *

import pytest
from typing import List


def test_pigeonhole_sort_execution() -> None:
    """
    Test whether the pigeonhole_sort function executes successfully
    without throwing any errors.
    """
    sequence = [8, 3, 2, 7, 4, 6, 8]
    pigeonhole_sort(sequence)


@pytest.mark.parametrize(
    "sequence, expected",
    [
        ([8, 3, 2, 7, 4, 6, 8], [2, 3, 4, 6, 7, 8, 8]),
        ([1], [1]),
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
    ],
)
def test_pigeonhole_sort_correct_output(
    sequence: List[int], expected: List[int]
) -> None:
    """
    Test whether the pigeonhole_sort function correctly sorts a list of
    integers in ascending order
    """
    pigeonhole_sort(sequence)
    assert sequence == expected
