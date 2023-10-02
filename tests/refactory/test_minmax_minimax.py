
import pytest
from backtracking.minmax import *
import math
from typing import List


def test_minimax():
    scores = [90, 23, 6, 33, 21, 65, 123, 34423]
    height = math.log(len(scores), 2)
    result = minimax(0, 0, True, scores, height)

    assert result is not None


def test_minimax_negative_depth():
    scores = [3, 5, 2, 9, 12, 5, 23, 23]
    height = math.log(len(scores), 2)
    with pytest.raises(ValueError):
        minimax(-1, 0, True, scores, height)


def test_minimax_empty_scores():
    with pytest.raises(ValueError):
        minimax(0, 0, True, [], 2)


@pytest.mark.parametrize(
    "scores, height, expected",
    [
        ([90, 23, 6, 33, 21, 65, 123, 34423], math.log(8, 2), 65),
        ([3, 5, 2, 9, 12, 5, 23, 23], math.log(8, 2), 12),
    ],
)
def test_minimax_various_scores(scores: List[int], height: float, expected: int):
    result = minimax(0, 0, True, scores, height)

    assert result == expected
