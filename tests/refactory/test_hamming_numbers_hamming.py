import pytest


import pytest
from maths.hamming_numbers import *


def test_hamming():
    assert hamming(5) == [1, 2, 3, 4, 5]
    assert hamming(10) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
    assert hamming(15) == [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24]


def test_hamming_edge_cases():
    with pytest.raises(ValueError):
        hamming(-1)

    with pytest.raises(ValueError):
        hamming(0)

    assert hamming(1) == [1]
