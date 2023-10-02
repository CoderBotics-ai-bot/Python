from sorts.binary_insertion_sort import *
import random
import string

import pytest
from typing import List, Union


# We are going to use binary_insertion_sort on different datatypes, so we create a fixture that will provide us the function.
@pytest.fixture
def sorting_function():
    return binary_insertion_sort


def test_binary_insertion_sort_no_throw_no_return_None_positive_integers(
    sorting_function,
):
    collection = [4, 123, 56, 1, 90, 32]
    result = sorting_function(collection)
    assert result is not None


def test_binary_insertion_sort_no_throw_no_return_None_negative_integers(
    sorting_function,
):
    collection = [-12, -44, -56, -89, -2]
    result = sorting_function(collection)
    assert result is not None


def test_binary_insertion_sort_no_throw_no_return_None_empty_list(sorting_function):
    collection = []
    result = sorting_function(collection)
    assert result is not None


def test_binary_insertion_sort_no_throw_no_return_None_string_elements(
    sorting_function,
):
    collection = ["a", "h", "d", "x", "y", "q"]
    result = sorting_function(collection)
    assert result is not None


def test_binary_insertion_sort_no_throw_no_return_None_mixed_elements(sorting_function):
    with pytest.raises(Exception):
        collection = [1, "h", 34, "y", 23]
        result = sorting_function(collection)


def test_binary_insertion_sort_sorts_correctly(sorting_function):
    collection = [4, 2, 9, 1, 5, 7, 3, 0]
    result = sorting_function(collection)
    assert result == sorted(collection)


def test_binary_insertion_sort_sorts_correctly_large_random_list(sorting_function):
    collection = random.sample(range(-10000, 10000), 10000)
    result = sorting_function(collection)
    assert result == sorted(collection)


def test_binary_insertion_sort_sorts_correctly_random_chars(sorting_function):
    collection = random.choices(string.ascii_letters + string.digits, k=100)
    result = sorting_function(collection)
    assert result == sorted(collection)
