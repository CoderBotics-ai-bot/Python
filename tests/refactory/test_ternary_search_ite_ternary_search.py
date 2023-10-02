from searches.ternary_search import *
import pytest


def test_ite_ternary_search_no_error():
    array = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    target = 3
    result = ite_ternary_search(array, target)
    assert result is not None


def test_ite_ternary_search_positives():
    array = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    target = 13
    result = ite_ternary_search(array, target)
    assert result == 4


def test_ite_ternary_search_negatives():
    array = [-18, -2, -1, 0, 1, 2, 3, 4, 5]
    target = -2
    result = ite_ternary_search(array, target)
    assert result == 1


def test_ite_ternary_search_empty_list():
    array = []
    target = 10
    result = ite_ternary_search(array, target)
    assert result == -1


def test_ite_ternary_search_letters():
    array = ["a", "b", "c", "d", "e"]
    target = "c"
    result = ite_ternary_search(array, target)
    assert result == 2


def test_ite_ternary_search_not_found():
    array = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    target = 100
    result = ite_ternary_search(array, target)
    assert result == -1
