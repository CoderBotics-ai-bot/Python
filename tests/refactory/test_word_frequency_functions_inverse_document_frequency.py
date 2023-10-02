from machine_learning.word_frequency_functions import *
import pytest


import pytest


def test_inverse_document_frequency_returns_value():
    result = inverse_document_frequency(3, 100)
    assert result is not None


def test_inverse_document_frequency_with_smoothing_returns_value():
    result = inverse_document_frequency(0, 100, smoothing=True)
    assert result is not None


def test_inverse_document_frequency_df_zero_raises_exception():
    with pytest.raises(ZeroDivisionError):
        inverse_document_frequency(0, 100)


def test_inverse_document_frequency_n_zero_raises_exception():
    with pytest.raises(ValueError):
        inverse_document_frequency(3, 0)


def test_inverse_document_frequency_n_zero_with_smoothing_raises_exception():
    with pytest.raises(ValueError):
        inverse_document_frequency(3, 0, smoothing=True)


def test_inverse_document_frequency_both_zero_without_smoothing_raises_exception():
    with pytest.raises(ZeroDivisionError):
        inverse_document_frequency(0, 0)
