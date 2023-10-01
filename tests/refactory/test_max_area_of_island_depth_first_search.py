
import pytest
from matrix.max_area_of_island import *
import pytest


from typing import List, Set


def test_depth_first_search():
    valid_matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    seen = set()
    result = depth_first_search(0, 0, seen, valid_matrix)
    assert result is not None


def test_depth_first_search_with_unseen_location():
    valid_matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    seen = set()
    assert depth_first_search(2, 2, seen, valid_matrix) is not None


def test_depth_first_search_with_seen_location():
    valid_matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    seen = {(0, 0)}
    assert depth_first_search(0, 0, seen, valid_matrix) == 0


def test_depth_first_search_with_invalid_location():
    valid_matrix = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
    seen = set()
    assert depth_first_search(-1, -1, seen, valid_matrix) == 0
