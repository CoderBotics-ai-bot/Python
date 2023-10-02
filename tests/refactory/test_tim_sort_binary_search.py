

from typing import List

import pytest
from sorts.tim_sort import *
from typing import List


@pytest.fixture
def generate_list():
    return [7, 15, 23, 31, 39, 47, 55, 63, 71, 79]


def test_binary_search_without_errors(generate_list: List[int]):
    item = 55
    start = 0
    end = len(generate_list) - 1
    result = binary_search(generate_list, item, start, end)
    assert result is not None


def test_binary_search_item_not_in_the_list(generate_list: List[int]):
    item = 100
    start = 0
    end = len(generate_list) - 1
    expected = 10
    result = binary_search(generate_list, item, start, end)
    assert result == expected


def test_binary_search_with_single_element_higher():
    item = 6
    result = binary_search([4], item, 0, 0)
    assert result == 1


def test_binary_search_with_single_element_lower():
    item = 2
    result = binary_search([10], item, 0, 0)
    assert result == 0


def test_binary_search_with_empty_list():
    item = 4
    result = binary_search([], item, 0, -1)
    assert result == 0
