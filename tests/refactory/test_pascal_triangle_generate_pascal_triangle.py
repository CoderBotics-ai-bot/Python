from matrix.pascal_triangle import *
import pytest


def test_generate_pascal_triangle():
    result = generate_pascal_triangle(2)
    assert result is not None


def test_generate_pascal_triangle_zero():
    result = generate_pascal_triangle(0)
    assert result == []


def test_generate_pascal_triangle_one():
    result = generate_pascal_triangle(1)
    assert result == [[1]]


def test_generate_pascal_triangle_negative():
    with pytest.raises(ValueError):
        generate_pascal_triangle(-5)


def test_generate_pascal_triangle_float():
    with pytest.raises(TypeError):
        generate_pascal_triangle(5.5)
