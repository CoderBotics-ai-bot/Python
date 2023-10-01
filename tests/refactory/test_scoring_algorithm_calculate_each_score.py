from other.scoring_algorithm import *
import pytest


import pytest


def test_calculate_each_score_no_errors():
    data = [[20.0, 23.0, 22.0], [60.0, 90.0, 50.0], [2012.0, 2015.0, 2011.0]]
    weights = [0, 0, 1]
    assert calculate_each_score(data, weights) is not None


def test_calculate_each_score_output_type():
    data = [[20.0, 30.0], [50.0, 60.0], [80.0, 90.0]]
    weights = [0, 1, 1]
    result = calculate_each_score(data, weights)
    assert isinstance(result, list)
    assert isinstance(result[0], list)
    assert isinstance(result[0][0], float)


def test_calculate_each_score_invalid_weight():
    data = [[20.0, 22.0], [50.0, 60.0]]
    weights = [0, 2]
    with pytest.raises(ValueError):
        calculate_each_score(data, weights)


def test_calculate_each_score_zero_division():
    data = [[20.0, 20.0], [50.0, 50.0]]
    weights = [0, 1]
    result = calculate_each_score(data, weights)
    # When denominator is zero, score for weight=0 should be 1 and for weight=1 it should be 0
    assert result == [[1.0, 1.0], [0.0, 0.0]]
