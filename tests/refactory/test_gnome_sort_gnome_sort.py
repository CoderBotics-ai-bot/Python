import pytest
from sorts.gnome_sort import *


def test_gnome_sort_type():
    """
    Test if the function gnome_sort is callable and doesn't throw any errors when it's executed
    """
    assert callable(gnome_sort)


def test_gnome_sort_return_value():
    """
    Test if the function gnome_sort return list, it shouldn't return None
    """
    assert gnome_sort([0, 5, 3, 2, 2]) is not None
    assert type(gnome_sort([0, 5, 3, 2, 2])) == list


def test_gnome_sort_edgecase1():
    """
    Test if the function gnome_sort is sorting properly with same values
    """
    assert gnome_sort([2, 2, 2, 2]) == [2, 2, 2, 2]


def test_gnome_sort_edgecase2():
    """
    Test if the function gnome_sort is sorting properly with an ordered list
    """
    assert gnome_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_gnome_sort_edgecase3():
    """
    Test if the function gnome_sort is sorting properly with an unordered list
    """
    assert gnome_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_gnome_sort_edgecase4():
    """
    Test if the function gnome_sort is sorting properly with a list of negative integers
    """
    assert gnome_sort([-5, -4, -3, -2, -1]) == [-5, -4, -3, -2, -1]
