import pytest
from maths.series.harmonic import *


def test_harmonic_series_valid():
    assert is_harmonic_series([1, 2 / 3, 1 / 2, 2 / 5, 1 / 3])
    assert is_harmonic_series([1 / 2, 1 / 3, 1 / 4])
    assert is_harmonic_series([2 / 5, 2 / 10, 2 / 15, 2 / 20, 2 / 25])


def test_harmonic_series_invalid():
    assert not is_harmonic_series([1, 2 / 3, 2 / 5, 1 / 3])
    assert not is_harmonic_series([1, 2, 3])


def test_harmonic_series_error_cases():
    with pytest.raises(ValueError):
        is_harmonic_series(4)
    with pytest.raises(ValueError):
        is_harmonic_series([])
    with pytest.raises(ValueError):
        is_harmonic_series([0])
    with pytest.raises(ValueError):
        is_harmonic_series([1, 2, 0, 6])
