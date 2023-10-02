#from graphs.multi_heuristic_astar import *
#import pytest
#
#
#@pytest.fixture
#def n():
#    return 5
#
#
#def test_valid_no_exception(n):
#    assert valid((1, 1)) is not None
#
#
#def test_valid_in_valid_range(n):
#    assert valid((0, 0))
#    assert valid((n - 1, n - 1))
#
#
#def test_valid_with_values_out_of_range(n):
#    assert not valid((-1, 0))
#    assert not valid((0, -1))
#    assert not valid((n, 0))
#    assert not valid((0, n))
#