from maths.jaccard_similarity import *
import pytest


def test_jaccard_similarity_with_sets():
    set_a = {"a", "b", "c", "d", "e"}
    set_b = {"c", "d", "e", "f", "h", "i"}

    # test normal union calculation
    result = jaccard_similarity(set_a, set_b)
    assert result == 0.375

    # test when both sets are equal
    result = jaccard_similarity(set_a, set_a)
    assert result == 1.0

    # test alternative union calculation when sets are equal
    result = jaccard_similarity(set_a, set_a, True)
    assert result == 0.5


def test_jaccard_similarity_with_list_and_tuple():
    set_a = ["a", "b", "c", "d", "e"]
    set_b = ("c", "d", "e", "f", "h", "i")

    # test normal union calculation
    result = jaccard_similarity(set_a, set_b)
    assert result == 0.375


def test_jaccard_similarity_with_invalid_types():
    set_a = 123
    set_b = 456

    # test invalid types
    result = jaccard_similarity(set_a, set_b)
    assert result == None
