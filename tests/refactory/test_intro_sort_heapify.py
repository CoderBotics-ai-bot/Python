from sorts.intro_sort import *
import pytest


def test_heapify_no_throw():
    array = [4, 2, 3, 1, 5]
    heapify(array, 0, len(array))
    assert True


@pytest.mark.parametrize(
    "array, index, heap_size, output",
    [
        ([1], 0, 1, [1]),
        ([2, 1], 0, 2, [2, 1]),
        ([1, 3, 5, 7, 2, 0], 0, 6, [5, 3, 1, 7, 2, 0]),
    ],
)
def test_heapify_varied(array, index, heap_size, output):
    heapify(array, index, heap_size)
    assert array == output
