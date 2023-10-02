#
#
#from typing import List, Tuple
#
#import pytest
#from typing import List, Tuple
#from graphs.graphs_floyd_warshall import *
#
#
#def test_print_dist_does_not_throw(
#    dist_v_fixture: Tuple[List[List[float]], int]
#) -> None:
#    dist, v = dist_v_fixture
#    try:
#        _print_dist(dist, v)
#    except Exception as e:
#        pytest.fail(f"_print_dist() raised {type(e).__name__} unexpectedly!")
#
#
#@pytest.fixture
#def dist_v_fixture() -> Tuple[List[List[float]], int]:
#    return (
#        [
#            [0, 5, float("inf"), 10],
#            [float("inf"), 0, 3, float("inf")],
#            [float("inf"), float("inf"), 0, 1],
#            [float("inf"), float("inf"), float("inf"), 0],
#        ],
#        4,
#    )
#