#
#import pytest
#from graphs.edmonds_karp_multiple_source_and_sink import *
#from typing import List
#
#
## Dummy class to avoid import errors
#class MaximumFlowAlgorithmExecutor:
#    pass
#
#
#class PushRelabelExecutor(MaximumFlowAlgorithmExecutor):
#    def relabel(self, vertex_index: int) -> None:
#        min_height = None
#        for to_index in range(self.verticies_count):
#            if (
#                self.graph[vertex_index][to_index]
#                - self.preflow[vertex_index][to_index]
#                > 0
#            ) and (min_height is None or self.heights[to_index] < min_height):
#                min_height = self.heights[to_index]
#
#        if min_height is not None:
#            self.heights[vertex_index] = min_height + 1
#
#    def __init__(self, flow_network: List[List[int]]):
#        super().__init__(flow_network)
#
#        self.verticies_count = len(flow_network)
#        self.preflow = [[0] * self.verticies_count for i in range(self.verticies_count)]
#        self.graph = flow_network
#        self.heights = [0] * self.verticies_count
#        self.excesses = [0] * self.verticies_count
#
#
#def test_relabel_does_not_throw_errors():
#    flow_network = [
#        [0, 16, 13, 0, 0, 0],
#        [0, 0, 10, 12, 0, 0],
#        [0, 4, 0, 0, 14, 0],
#        [0, 0, 9, 0, 0, 20],
#        [0, 0, 0, 7, 0, 4],
#        [0, 0, 0, 0, 0, 0],
#    ]
#    executor = PushRelabelExecutor(flow_network)
#    vertex_index = 1
#
#    try:
#        executor.relabel(vertex_index)
#        result = executor.heights[vertex_index]
#    except Exception as e:
#        pytest.fail("Unexpected Exception: {}".format(e))
#
#    assert result is not None
#
#
#def test_relabel_does_not_modify_height_when_no_preflow_exists():
#    flow_network = [
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#    ]
#    vertex_index = 1
#    executor = PushRelabelExecutor(flow_network)
#    initial_height = executor.heights[vertex_index]
#    executor.relabel(vertex_index)
#    assert executor.heights[vertex_index] == initial_height
#
#
#def test_relabel_changes_height_when_preflow_exists():
#    flow_network = [
#        [0, 4, 0, 0, 6, 0],
#        [0, 0, 7, 0, 2, 0],
#        [0, 0, 0, 4, 0, 0],
#        [0, 0, 0, 0, 0, 2],
#        [0, 0, 0, 5, 0, 3],
#        [0, 0, 0, 0, 0, 0],
#    ]
#    vertex_index = 2
#    executor = PushRelabelExecutor(flow_network)
#    initial_height = executor.heights[vertex_index]
#    executor.relabel(vertex_index)
#    assert executor.heights[vertex_index] > initial_height
#
#
#def test_relabel_increases_height_by_one():
#    flow_network = [
#        [0, 3, 0, 0, 5, 0],
#        [0, 0, 6, 5, 1, 0],
#        [0, 0, 0, 2, 0, 0],
#        [0, 0, 0, 0, 0, 1],
#        [0, 0, 0, 4, 0, 2],
#        [0, 0, 0, 0, 0, 0],
#    ]
#    vertex_index = 3
#    executor = PushRelabelExecutor(flow_network)
#    executor.heights[vertex_index] = 1
#    executor.relabel(vertex_index)
#    assert executor.heights[vertex_index] == 2
#