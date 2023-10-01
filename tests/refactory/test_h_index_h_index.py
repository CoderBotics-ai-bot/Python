from other.h_index import *
import pytest


import pytest


def test_h_index_no_error():
    citations = [3, 0, 6, 1, 5]
    assert h_index(citations) is not None


def test_h_index_sorted_input():
    citations = [1, 2, 3]
    assert h_index(citations) == 2


def test_h_index_unsorted_input():
    citations = [3, 2, 1]
    assert h_index(citations) == 2


def test_h_index_with_negative_number():
    citations = [1, 2, -3]
    with pytest.raises(ValueError):
        h_index(citations)


def test_h_index_with_string():
    citations = [1, 2, "3"]
    with pytest.raises(ValueError):
        h_index(citations)


def test_h_index_with_non_list_input():
    citations = "test"
    with pytest.raises(ValueError):
        h_index(citations)


def test_h_index_empty_list():
    citations = []
    assert h_index(citations) == 0
