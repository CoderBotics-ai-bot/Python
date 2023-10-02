import pytest
from sorts.iterative_merge_sort import *


def test_iter_merge_sort_no_errors():
    result = iter_merge_sort([5, 9, 8, 7, 1, 2, 7])
    assert result is not None


def test_iter_merge_sort_simple_cases():
    assert iter_merge_sort([]) == []
    assert iter_merge_sort([1]) == [1]
    assert iter_merge_sort([-1]) == [-1]
    assert iter_merge_sort(["a"]) == ["a"]


def test_iter_merge_sort_typical_cases():
    assert iter_merge_sort([5, 9, 8, 7, 1, 2, 7]) == [1, 2, 5, 7, 7, 8, 9]
    assert iter_merge_sort(["z", "a", "b", "x", "y"]) == ["a", "b", "x", "y", "z"]


def test_iter_merge_sort_edge_cases():
    assert iter_merge_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert iter_merge_sort(list(range(10000, 0, -1))) == list(range(1, 10001))


@pytest.mark.parametrize(
    "input_list", [["string", None, 42], [iter_merge_sort, iter_merge_sort]]
)
def test_iter_merge_sort_invalid_input(input_list):
    with pytest.raises(TypeError):
        iter_merge_sort(input_list)
