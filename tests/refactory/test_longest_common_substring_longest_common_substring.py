from dynamic_programming.longest_common_substring import *
import pytest


import pytest


def test_longest_common_substring_base_case():
    assert longest_common_substring("", "") is not None


def test_longest_common_substring_invalid_input():
    with pytest.raises(ValueError):
        longest_common_substring(1, 1)


def test_longest_common_substring_case1():
    assert longest_common_substring("abcdef", "bcd") is not None


def test_longest_common_substring_case2():
    assert longest_common_substring("abcdef", "xabded") is not None


def test_longest_common_substring_case3():
    assert longest_common_substring("abcdxyz", "xyzabcd") is not None


def test_longest_common_substring_case4():
    assert longest_common_substring("zxabcdezy", "yzabcdezx") is not None


def test_longest_common_substring_case5():
    assert (
        longest_common_substring("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
        is not None
    )
