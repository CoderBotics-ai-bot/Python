
import pytest
from matrix.matrix_operation import *
from typing import List


@pytest.fixture
def matrix_data() -> List[List[int]]:
    return [[1, 2], [3, 4]]


@pytest.fixture
def non_invertible_matrix_data() -> List[List[int]]:
    return [[1, 1], [1, 1]]


def test_inverse(matrix_data: List[List[int]]):
    result = inverse(matrix_data)
    assert result is not None


def test_inverse_non_invertible_matrix(non_invertible_matrix_data: List[List[int]]):
    result = inverse(non_invertible_matrix_data)
    assert result is None


def test_inverse_non_numeric_matrix():
    with pytest.raises(TypeError):
        inverse([[1, "2"], [3, 4]])
