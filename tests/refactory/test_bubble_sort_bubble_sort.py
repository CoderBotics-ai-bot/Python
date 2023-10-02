import pytest
from sorts.bubble_sort import *


def test_bubble_sort_no_error():
    collection = [3, 2, 1, 5, 4]
    assert bubble_sort(collection) is not None


@pytest.mark.parametrize(
    "collection, expected",
    [
        ([0, 5, 2, 3, 2], [0, 2, 2, 3, 5]),
        ([], []),
        ([-2, -45, -5], [-45, -5, -2]),
        ([-23, 0, 6, -4, 34], [-23, -4, 0, 6, 34]),
        (["d", "a", "b", "e", "c"], ["a", "b", "c", "d", "e"]),
    ],
)
def test_bubble_sort_correctness(collection, expected):
    assert bubble_sort(collection) == expected


def test_bubble_sort_large_input():
    import random

    collection = random.sample(range(-50, 50), 100)
    assert bubble_sort(collection) == sorted(collection)


def test_bubble_sort_string_digits():
    import random
    import string

    collection = random.choices(string.ascii_letters + string.digits, k=100)
    assert bubble_sort(collection) == sorted(collection)
