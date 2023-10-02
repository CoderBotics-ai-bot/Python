import random
import string

import pytest
from sorts.insertion_sort import *
from typing import List, Union


def test_insertion_sort_exists():
    collection = random.sample(range(-50, 50), 100)
    assert insertion_sort(collection) is not None


def test_insertion_sort_with_numbers():
    collection = [0, 5, 3, 2, 2]
    assert insertion_sort(collection) == [0, 2, 2, 3, 5]


def test_insertion_sort_with_empty_list():
    collection = []
    assert insertion_sort(collection) == sorted(collection)


def test_insertion_sort_with_negative_numbers():
    collection = [-2, -5, -45]
    assert insertion_sort(collection) == sorted(collection)


def test_insertion_sort_with_strings():
    collection = ["d", "a", "b", "e", "c"]
    assert insertion_sort(collection) == sorted(collection)


def test_insertion_sort_with_random_num_list():
    collection = random.sample(range(-50, 50), 100)
    assert insertion_sort(collection) == sorted(collection)


def test_insertion_sort_with_random_mix_list():
    collection = random.choices(string.ascii_letters + string.digits, k=100)
    assert insertion_sort(collection) == sorted(collection)
