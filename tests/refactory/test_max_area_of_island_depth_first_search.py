from typing import List, Set

import pytest
from matrix.max_area_of_island import *


@pytest.fixture
def matrix_fixture() -> List[List[int]]:
    return [[1, 1, 0, 0, 1], [0, 1, 0, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 5]]


def test_depth_first_search(matrix_fixture):
    seen = set()
    assert depth_first_search(0, 0, seen, matrix_fixture) is not None


def test_depth_first_search_with_unseen_location(matrix_fixture):
    seen = set()
    assert depth_first_search(2, 0, seen, matrix_fixture) != 0


def test_depth_first_search_with_seen_location(matrix_fixture):
    seen = set([(0, 0)])
    assert depth_first_search(0, 0, seen, matrix_fixture) == 0


def test_depth_first_search_with_unsafe_location(matrix_fixture):
    seen = set()
    assert depth_first_search(6, 4, seen, matrix_fixture) == 0


def test_depth_first_search_with_zero_element(matrix_fixture):
    seen = set()
    assert depth_first_search(1, 0, seen, matrix_fixture) == 0
