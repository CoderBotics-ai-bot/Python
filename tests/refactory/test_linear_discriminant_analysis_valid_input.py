from machine_learning.linear_discriminant_analysis import *
import pytest


def test_valid_input_no_errors(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    result = valid_input(
        float,
        "Enter a number > 0:",
        "This number is not greater than 0",
        lambda x: x > 0,
    )
    assert result is not None


def test_valid_input_condition(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")
    result = valid_input(
        float,
        "Enter a number > 0:",
        "This number is not greater than 0",
        lambda x: x > 0,
    )
    assert float(result) > 0


def test_valid_input_with_no_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "")
    result = valid_input(
        float,
        "Enter a number > 0:",
        "This number is not greater than 0",
        lambda x: x > 0,
        default="10",
    )
    assert result == 10.0
