from compression.run_length_encoding import *
import pytest


def test_run_length_encode_base():
    assert run_length_encode("AAAABBBCCDAA") is not None
    assert run_length_encode("A") is not None
    assert run_length_encode("AA") is not None
    assert run_length_encode("AAADDDDDDFFFCCCAAVVVV") is not None


def test_run_length_encode_some_values():
    run_length_encode_result = run_length_encode("AAAABBBCCDAA")
    assert len(run_length_encode_result) == 5
    assert run_length_encode_result[-1][0] == "A"
    assert run_length_encode_result[-1][1] == 2


def test_run_length_encode_single_character():
    run_length_encode_result = run_length_encode("A")
    assert len(run_length_encode_result) == 1
    assert run_length_encode_result[0] == ("A", 1)


def test_run_length_encode_empty_string():
    assert run_length_encode("") == []


def test_run_length_encode_long_sequence():
    run_length_encode_result = run_length_encode("AA" * 100)
    assert len(run_length_encode_result) == 1
    assert run_length_encode_result[0] == ("A", 200)


@pytest.mark.parametrize(
    "text",
    [
        "AAA",
        "BB",
        "CCCC",
        "DDDD",
        "E",
    ],
)
def test_run_length_encode_repeated_single_char(text):
    run_length_encode_result = run_length_encode(text)
    assert len(run_length_encode_result) == 1
    assert run_length_encode_result[0] == (text[0], len(text))


@pytest.mark.parametrize(
    "text, expected",
    [
        ("AB", [("A", 1), ("B", 1)]),
        ("ABC", [("A", 1), ("B", 1), ("C", 1)]),
        ("AABBCC", [("A", 2), ("B", 2), ("C", 2)]),
        ("AAABBBCCC", [("A", 3), ("B", 3), ("C", 3)]),
    ],
)
def test_run_length_encode_multiple_chars(text, expected):
    assert run_length_encode(text) == expected
