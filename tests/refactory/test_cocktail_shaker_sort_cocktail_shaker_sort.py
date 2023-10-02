from sorts.cocktail_shaker_sort import *
import pytest


def test_cocktail_shaker_sort():
    assert cocktail_shaker_sort([4, 5, 2, 1, 2]) == [1, 2, 2, 4, 5]
    assert cocktail_shaker_sort([-4, 5, 0, 1, 2, 11]) == [-4, 0, 1, 2, 5, 11]
    assert cocktail_shaker_sort([0.1, -2.4, 4.4, 2.2]) == [-2.4, 0.1, 2.2, 4.4]
    assert cocktail_shaker_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert cocktail_shaker_sort([-4, -5, -24, -7, -11]) == [-24, -11, -7, -5, -4]


def test_cocktail_shaker_sort_empty():
    assert cocktail_shaker_sort([]) == []


def test_cocktail_shaker_sort_single_item():
    """Function should not throw errors when single item list is passed"""
    assert cocktail_shaker_sort([1]) == [1]
    assert cocktail_shaker_sort([-1]) == [-1]


def test_cocktail_shaker_sort_same_items():
    """Function should not throw errors when all items in the list are same"""
    assert cocktail_shaker_sort([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert cocktail_shaker_sort(["a", "a"]) == ["a", "a"]
