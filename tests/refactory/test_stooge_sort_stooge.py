from sorts.stooge_sort import *
import pytest


@pytest.fixture
def setup_data():
    return [4, 3, 2, 1]


def test_stooge_not_throwing_errors(setup_data):
    try:
        stooge(setup_data, 0, len(setup_data) - 1)
    except Exception as e:
        pytest.fail(f"Stooge function raised an exception: {e}")


def test_stooge_sorting_correctly(setup_data):
    stooge(setup_data, 0, len(setup_data) - 1)
    assert setup_data == [1, 2, 3, 4]


def test_stooge_with_single_element():
    single_element_list = [1]
    stooge(single_element_list, 0, len(single_element_list) - 1)
    assert single_element_list == [1]


def test_stooge_with_empty_list():
    empty_list = []
    stooge(empty_list, 0, len(empty_list) - 1)
    assert empty_list == []


def test_stooge_already_sorted_list():
    sorted_list = [1, 2, 3, 4]
    stooge(sorted_list, 0, len(sorted_list) - 1)
    assert sorted_list == [1, 2, 3, 4]
