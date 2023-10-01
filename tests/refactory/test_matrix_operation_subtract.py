from matrix.matrix_operation import *
from typing import List, Tuple

import pytest


@pytest.fixture
def valid_matrices() -> Tuple[List[List[int]], List[List[int]]]:
    matrix_a: List[List[int]] = [[1, 2], [3, 4]]
    matrix_b: List[List[int]] = [[2, 3], [4, 5]]
    return matrix_a, matrix_b


@pytest.fixture
def single_element_matrices() -> Tuple[List[List[int]], List[List[int]]]:
    matrix_a: List[List[int]] = [[5]]
    matrix_b: List[List[int]] = [[3]]
    return matrix_a, matrix_b


@pytest.fixture
def matrices_with_negative_numbers() -> Tuple[List[List[int]], List[List[int]]]:
    matrix_a: List[List[int]] = [[-1, 2], [-3, 4]]
    matrix_b: List[List[int]] = [[2, -3], [4, -5]]
    return matrix_a, matrix_b


def test_subtract_correct_execution(
    valid_matrices: Tuple[List[List[int]], List[List[int]]]
) -> None:
    assert subtract(*valid_matrices) is not None


def test_subtract_with_single_element_matrix(
    single_element_matrices: Tuple[List[List[int]], List[List[int]]]
) -> None:
    assert subtract(*single_element_matrices) is not None


def test_subtract_with_negative_numbers(
    matrices_with_negative_numbers: Tuple[List[List[int]], List[List[int]]]
) -> None:
    assert subtract(*matrices_with_negative_numbers) is not None
