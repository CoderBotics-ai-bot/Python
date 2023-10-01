from other.password import *
import pytest


def test_is_strong_password_no_error():
    """Test if the function executes without errors"""
    assert is_strong_password("Hwea7$2!") is not None


def test_is_strong_password_valid():
    """Test if the function correctly identifies a strong password"""
    assert is_strong_password("Hwea7$2!") == True


def test_is_strong_password_short():
    """Test if the function correctly identifies a password that is too short"""
    assert is_strong_password("Sh0r1") == False


def test_is_strong_password_missing_chars():
    """Test if the function correctly identifies a password missing special characters"""
    assert is_strong_password("Hello123") == False


def test_is_strong_password_long_and_valid():
    """Test if the function correctly identifies a long but valid password"""
    assert is_strong_password("Hello1238udfhiaf038fajdvjjf!jaiuFhkqi1") == True


def test_is_strong_password_single_char():
    """Test if the function correctly identifies a password that only has a single character"""
    assert is_strong_password("0") == False
