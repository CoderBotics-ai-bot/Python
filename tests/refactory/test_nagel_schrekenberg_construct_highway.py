from cellular_automata.nagel_schrekenberg import *
import pytest


def test_construct_highway_no_error():
    """Test if the function doesn't throw any error."""
    try:
        construct_highway(10, 2, 6)
    except Exception as e:
        pytest.fail(f"construct_highway(10, 2, 6) raised an exception: {e}")


def test_construct_highway_return():
    """Test if the function returns a value."""
    assert construct_highway(10, 2, 6) is not None


def test_construct_highway_length():
    """Test if the function returns a result of correct length."""
    assert len(construct_highway(10, 2, 6)[0]) == 10


def test_construct_highway_random_speed():
    """Test if random speeds are indeed different if random_speed is set to True."""
    result = construct_highway(10, 2, 6, random_speed=True)
    speeds = {x for x in result[0] if x != -1}
    assert len(speeds) > 1


def test_construct_highway_negative_speed():
    """Test if function handles negative speed correctly."""
    result = construct_highway(10, 2, -1)
    result_speeds = [x for x in result[0] if x != -1]
    assert all(speed >= 0 for speed in result_speeds)
