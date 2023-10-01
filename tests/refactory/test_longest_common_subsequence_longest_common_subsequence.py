from dynamic_programming.longest_common_subsequence import *
import pytest


def test_longest_common_subsequence():
    assert longest_common_subsequence("programming", "gaming") is not None
    assert longest_common_subsequence("physics", "smartphone") is not None
    assert longest_common_subsequence("computer", "food") is not None


def test_longest_common_subsequence_same_input():
    result = longest_common_subsequence("shared", "shared")
    assert result == (6, "shared")


def test_longest_common_subsequence_no_overlap():
    result = longest_common_subsequence("abcd", "efgh")
    assert result == (0, "")


def test_longest_common_subsequence_empty_input():
    result = longest_common_subsequence("", "notempty")
    assert result == (0, "")

    result = longest_common_subsequence("notempty", "")
    assert result == (0, "")

    result = longest_common_subsequence("", "")
    assert result == (0, "")
