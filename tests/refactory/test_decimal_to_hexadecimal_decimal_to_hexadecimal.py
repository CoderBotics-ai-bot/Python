import pytest
from conversions.decimal_to_hexadecimal import *


def test_decimal_to_hexadecimal_positive_integers():
    assert decimal_to_hexadecimal(5) == "0x5"
    assert decimal_to_hexadecimal(15) == "0xf"
    assert decimal_to_hexadecimal(37) == "0x25"
    assert decimal_to_hexadecimal(255) == "0xff"


def test_decimal_to_hexadecimal_large_input():
    assert decimal_to_hexadecimal(4096) == "0x1000"
    assert decimal_to_hexadecimal(999098) == "0xf3eba"


def test_decimal_to_hexadecimal_negatives():
    assert decimal_to_hexadecimal(-256) == "-0x100"


def test_decimal_to_hexadecimal_float_integer_equivalent():
    assert decimal_to_hexadecimal(17.0) == "0x11"


def test_decimal_to_hexadecimal_comparison_python_hex():
    assert decimal_to_hexadecimal(-256) == hex(-256)


def test_decimal_to_hexadecimal_exceptions():
    with pytest.raises(AssertionError):
        decimal_to_hexadecimal(16.16)
    with pytest.raises(AssertionError):
        decimal_to_hexadecimal("0xfffff")
