import pytest
from sorts.external_sort import *


def test_parse_memory_no_error():
    """Test parse_memory function whether it runs without an error"""
    result = parse_memory("1g")
    assert result is not None


def test_parse_memory_k():
    """Test parse_memory function with kilobytes parameter"""
    result = parse_memory("10k")
    assert result == 10 * 1024


def test_parse_memory_m():
    """Test parse_memory function with megabytes parameter"""
    result = parse_memory("10m")
    assert result == 10 * 1024 * 1024


def test_parse_memory_g():
    """Test parse_memory function with gigabytes parameter"""
    result = parse_memory("10g")
    assert result == 10 * 1024 * 1024 * 1024


def test_parse_memory_no_suffix():
    """Test parse_memory function with no suffix parameter"""
    result = parse_memory("10")
    assert result == 10


def test_parse_memory_lower_upper():
    """Test parse_memory function with lowercase and uppercase parameter"""
    result_lowercase = parse_memory("10k")
    result_uppercase = parse_memory("10K")
    assert result_lowercase == result_uppercase


def test_parse_memory_espacing():
    """Test parse_memory function with edge cases"""
    with pytest.raises(ValueError):
        parse_memory("10h")
