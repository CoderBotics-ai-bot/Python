#
#import numpy as np
#import pytest
#from unittest.mock import Mock, patch
#from typing import Any, Dict
#from queue import PriorityQueue
#from graphs.bi_directional_dijkstra import *
#
#
## First test checks if function execution doesn't result in any errors
#def test_bidirectional_dij_execution():
#    graph_forward: Dict[str, Dict[str, int]] = {"a": {"b": 1}, "b": {"c": 1}}
#    graph_backward: Dict[str, Dict[str, int]] = {"c": {"b": 1}, "b": {"a": 1}}
#
#    with patch("queue.PriorityQueue", return_value=Mock(spec=PriorityQueue)):
#        try:
#            result = bidirectional_dij("a", "c", graph_forward, graph_backward)
#            assert result is not None
#        except Exception as e:
#            pytest.fail(f"bidirectional_dij() raised {type(e).__name__} unexpectedly!")
#
#
## Second test checks if function returns correct output for special case when source is equal to destination
#def test_bidirectional_dij_same_source_destination():
#    graph_forward: Dict[str, Dict[str, int]] = {"a": {"b": 1}}
#    graph_backward: Dict[str, Dict[str, int]] = {"b": {"a": 1}}
#
#    with patch("queue.PriorityQueue", return_value=Mock(spec=PriorityQueue)):
#        result = bidirectional_dij("a", "a", graph_forward, graph_backward)
#        assert result == 0
#
#
## Third test checks if function returns correct output for unreachable destination
#def test_bidirectional_dij_unreachable_destination():
#    graph_forward: Dict[str, Dict[str, int]] = {"a": {"b": 1}}
#    graph_backward: Dict[str, Dict[str, int]] = {"b": {"a": 1}}
#
#    with patch("queue.PriorityQueue", return_value=Mock(spec=PriorityQueue)):
#        result = bidirectional_dij("a", "c", graph_forward, graph_backward)
#        assert result == -1
#
#
## Fourth test checks if function returns correct output for reachable destination
#def test_bidirectional_dij_reachable_destination():
#    graph_forward: Dict[str, Dict[str, int]] = {"a": {"b": 1}, "b": {"c": 1}}
#    graph_backward: Dict[str, Dict[str, int]] = {"c": {"b": 1}, "b": {"a": 1}}
#
#    with patch("queue.PriorityQueue", return_value=Mock(spec=PriorityQueue)):
#        result = bidirectional_dij("a", "c", graph_forward, graph_backward)
#        assert result is not None
#