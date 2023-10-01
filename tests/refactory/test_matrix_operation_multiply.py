from matrix.matrix_operation import *
import pytest


def test_multiply_does_not_throw_errors(
    matrix_a: List[List[int]], matrix_b: List[List[int]]
):
    try:
        multiply(matrix_a, matrix_b)
        assert True
    except:
        assert False, "multiply function threw an error"


def test_multiply_return_result(matrix_a: List[List[int]], matrix_b: List[List[int]]):
    result = multiply(matrix_a, matrix_b)
    assert result is not None, "multiply function returned None"


def test_multiply_with_incompatible_matrix_dimensions(
    matrix_a: List[List[int]], matrix_b_3by2: List[List[int]]
):
    with pytest.raises(ValueError):
        multiply(matrix_a, matrix_b_3by2)


@pytest.fixture
def matrix_a() -> List[List[int]]:
    return [[1, 2], [3, 4]]


@pytest.fixture
def matrix_b() -> List[List[int]]:
    return [[5, 5], [7, 5]]


@pytest.fixture
def matrix_b_3by2() -> List[List[int]]:
    return [[1, 2], [3, 4], [5, 6]]
