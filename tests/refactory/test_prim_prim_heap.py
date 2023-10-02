#from graphs.prim import *
#
#import pytest
#from unittest.mock import MagicMock
#from typing import List
#
#
#def test_prim_heap_no_exception(graph: list, rootVertex: Vertex):
#    graph = [MagicMock() for _ in range(5)]
#    rootVertex = graph[0]
#
#    try:
#        prim_heap(graph, rootVertex)
#    except Exception:
#        pytest.fail("prim_heap raised an exception")
#
#
#def test_prim_heap_result_not_none(graph: list, rootVertex: Vertex):
#    graph = [MagicMock() for _ in range(5)]
#    rootVertex = graph[0]
#
#    result = prim_heap(graph, rootVertex)
#
#    assert result is not None, "Expected result not None"
#
#
#def test_prim_heap_empty_graph(graph: list, rootVertex: Vertex):
#    rootVertex = MagicMock()
#
#    result = prim_heap([], rootVertex)
#
#    assert result is not None, "Expected result to be not None"
#
#
#def test_prim_heap_singleton_graph(graph: list, rootVertex: Vertex):
#    rootVertex = MagicMock()
#    graph = [rootVertex]
#
#    result = prim_heap(graph, rootVertex)
#
#    assert result is not None, "Expected result not None"
#