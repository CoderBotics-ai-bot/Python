import pytest
from project_euler.problem_077.sol1 import *


def test_partition():
    assert partition(10) == {32, 36, 21, 25, 30}
    assert partition(15) == {192, 160, 105, 44, 112, 243, 180, 150, 216, 26, 125, 126}
    assert len(partition(20)) == 26
    assert partition(0) == {1}
    assert partition(-1) == set()


def test_partition_with_special_case():
    assert partition(1) == set()
