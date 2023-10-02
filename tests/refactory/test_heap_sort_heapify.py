import pytest
from sorts.heap_sort import *


def test_heapify_no_error():
    sample_unsorted_list = [7, 2, 1, 6, 8, 5, 3, 4]
    index = 1
    heap_size = len(sample_unsorted_list)

    # validate function doesn't throw any error
    try:
        heapify(sample_unsorted_list, index, heap_size)
    except Exception as e:
        pytest.fail(f"Heapify function threw an error: {e}")


def test_heapify_return_none():
    sample_unsorted_list = [7, 2, 1, 6, 8, 5, 3, 4]
    index = 1
    heap_size = len(sample_unsorted_list)
    assert heapify(sample_unsorted_list, index, heap_size) is None


def test_heapify_empty_list():
    sample_unsorted_list = []
    index = 0
    heap_size = len(sample_unsorted_list)
    try:
        heapify(sample_unsorted_list, index, heap_size)
    except Exception as e:
        pytest.fail(f"Heapify function threw an error with empty list: {e}")


def test_heapify_negative_index():
    sample_unsorted_list = [7, 2, 1, 6, 8, 5, 3, 4]
    index = -1
    heap_size = len(sample_unsorted_list)
    try:
        heapify(sample_unsorted_list, index, heap_size)
    except Exception as e:
        pytest.fail(f"Heapify function threw an error with negative index: {e}")
