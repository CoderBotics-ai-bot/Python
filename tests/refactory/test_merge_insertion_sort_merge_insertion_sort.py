from sorts.merge_insertion_sort import *
import pytest


def test_merge_insertion_sort_no_errors(collection_fixture):
    try:
        merge_insertion_sort(collection_fixture)
    except Exception:
        pytest.fail("The function caused an error")


def test_merge_insertion_sort_return_value_not_none(collection_fixture):
    assert merge_insertion_sort(collection_fixture) is not None


def test_merge_insertion_sort_check_order(collection_fixture):
    sorted_collection = merge_insertion_sort(collection_fixture)
    assert sorted_collection == sorted(collection_fixture)


def test_merge_insertion_sort_single_element_list():
    single_element_list = [7]
    assert merge_insertion_sort(single_element_list) == single_element_list


def test_merge_insertion_sort_empty_list():
    assert merge_insertion_sort([]) == []


def test_merge_insertion_sort_negative_numbers():
    numbers = [-1, -3, -2, -5, -4]
    assert merge_insertion_sort(numbers) == sorted(numbers)


@pytest.fixture
def collection_fixture():
    return [5, 2, 1, 4, 3]
