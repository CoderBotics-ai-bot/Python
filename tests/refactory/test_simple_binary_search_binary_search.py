import pytest


import pytest
from searches.simple_binary_search import *


@pytest.mark.parametrize(
    "a_list, item, expected",
    [
        ([0, 1, 2, 8, 13, 17, 19, 32, 42], 3, False),
        ([0, 1, 2, 8, 13, 17, 19, 32, 42], 13, True),
        ([4, 4, 5, 6, 7], 4, True),
        ([4, 4, 5, 6, 7], -10, False),
        ([-18, 2], -18, True),
        ([5], 5, True),
        (["a", "c", "d"], "c", True),
        (["a", "c", "d"], "f", False),
        ([], 1, False),
        ([-0.1, 0.1, 0.8], 0.1, True),
        ([i for i in range(-5000, 5000, 10)], 80, True),
        ([i for i in range(-5000, 5000, 10)], 1255, False),
        ([i for i in range(0, 10000, 5)], 2, False),
    ],
)
def test_binary_search(a_list, item, expected):
    assert binary_search(a_list, item) == expected


def test_binary_search_no_throw():
    try:
        binary_search([0, 1, 2, 8, 13, 17, 19, 32, 42], 3)
    except Exception as e:
        pytest.fail(f"Test failed with exception: {e}")
    assert 1 == 1
