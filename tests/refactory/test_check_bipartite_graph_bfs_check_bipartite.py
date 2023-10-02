from graphs.check_bipartite_graph_bfs import *

import pytest
from queue import Queue


from queue import Queue


def test_check_bipartite():
    # test case where graph is bipartite
    graph_bipartite = [[1, 3], [0, 2], [1, 3], [0, 2]]
    assert check_bipartite(graph_bipartite)

    # test case where graph is not bipartite
    graph_not_bipartite = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    assert not check_bipartite(graph_not_bipartite)

    # test case where graph is empty
    graph_empty = []
    assert check_bipartite(graph_empty)

    # test case where graph has only one node
    graph_single_node = [[]]
    assert check_bipartite(graph_single_node)

    # test case where graph has loop on a single node
    graph_single_loop = [[0]]
    assert not check_bipartite(graph_single_loop)
