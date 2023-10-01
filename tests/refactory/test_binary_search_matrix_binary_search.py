import pytest
from matrix.binary_search_matrix import *


def test_binary_search_no_errors():
    matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert binary_search(matrix, 0, len(matrix) - 1, 1) is not None


def test_binary_search_non_existing_element():
    matrix = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert binary_search(matrix, 0, len(matrix) - 1, 99) == -1


def test_binary_search_on_single_element_list():
    matrix = [1]
    assert binary_search(matrix, 0, len(matrix) - 1, 1) == 0
