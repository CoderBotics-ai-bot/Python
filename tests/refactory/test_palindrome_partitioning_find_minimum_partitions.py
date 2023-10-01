import pytest
from dynamic_programming.palindrome_partitioning import *


def test_find_minimum_partitions_no_error():
    result = find_minimum_partitions("ababbbabbababa")
    assert result is not None


def test_find_minimum_partitions():
    assert find_minimum_partitions("aab") == 1
    assert find_minimum_partitions("aaa") == 0
    assert find_minimum_partitions("ababbbabbababa") == 3


def test_find_minimum_partitions_edge_single_char():
    assert find_minimum_partitions("a") == 0


def test_find_minimum_partitions_edge_non_palindrome():
    assert find_minimum_partitions("abcd") == 3
