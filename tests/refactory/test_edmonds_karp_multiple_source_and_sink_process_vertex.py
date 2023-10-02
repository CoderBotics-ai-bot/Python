#
#from .classes import MaximumFlowAlgorithmExecutor
#
#import pytest
#from graphs.edmonds_karp_multiple_source_and_sink import *
#from typing import List
#
#
#@pytest.fixture
#def setup_test_instance() -> PushRelabelExecutor:
#    class FlowNetwork:
#        pass
#
#    class MaximumFlowAlgorithmExecutor:
#        def __init__(self, flow_network: FlowNetwork):
#            pass
#
#    class PushRelabelExecutor(MaximumFlowAlgorithmExecutor):
#        def __init__(self, flow_network: FlowNetwork):
#            super().__init__(flow_network)
#            self.verticies_count: int = 6
#            self.preflow: List[List[int]] = [
#                [0] * self.verticies_count for _ in range(self.verticies_count)
#            ]
#            self.heights: List[int] = [0] * self.verticies_count
#            self.excesses: List[int] = [0] * self.verticies_count
#            self.graph: List[List[int]] = [
#                [0, 3, 2, 1, 0, 0],
#                [0, 0, 1, 2, 0, 0],
#                [0, 1, 0, 1, 1, 0],
#                [0, 0, 2, 0, 2, 0],
#                [0, 0, 0, 1, 0, 2],
#                [0, 2, 0, 0, 0, 0],
#            ]
#
#        def push(self, from_vertex: int, to_vertex: int):
#            pass
#
#        def relabel(self, vertex: int):
#            pass
#
#        def process_vertex(self, vertex_index: int):
#            while self.excesses[vertex_index] > 0:
#                for neighbour_index in range(self.verticies_count):
#                    if (
#                        self.graph[vertex_index][neighbour_index]
#                        - self.preflow[vertex_index][neighbour_index]
#                        > 0
#                        and self.heights[vertex_index] > self.heights[neighbour_index]
#                    ):
#                        self.push(vertex_index, neighbour_index)
#                self.relabel(vertex_index)
#
#    return PushRelabelExecutor(FlowNetwork())
#
#
#def test_process_vertex_no_exception(setup_test_instance):
#    setup_test_instance.process_vertex(0)
#
#
#def test_process_vertex_no_excess(setup_test_instance):
#    setup_test_instance.excesses = [0] * setup_test_instance.verticies_count
#    assert setup_test_instance.process_vertex(0) is None
#