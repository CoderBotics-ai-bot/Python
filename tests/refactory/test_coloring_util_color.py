import pytest
from backtracking.coloring import *


def test_util_color_no_errors():
    # define the required input for the function
    # for this test case we'll provide a simple graph with just three nodes and two available colors
    graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    max_colors = 2
    colored_vertices = [0, 0, 0]
    index = 0

    # make sure the function doesn't raise an error
    assert util_color(graph, max_colors, colored_vertices, index) is not None


def test_util_color_edge_case():
    # test case where the graph is just a single vertex
    graph = [[0]]
    max_colors = 1
    colored_vertices = [0]
    index = 0

    # since it's just a single vertex, it should not be a problem to find a valid coloring
    assert util_color(graph, max_colors, colored_vertices, index) == True


def test_util_color_complex_case():
    # test case where the graph is a cycle of 4 nodes and coloring is not possible with 2 colors
    graph = [[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
    max_colors = 2
    colored_vertices = [0, 0, 0, 0]
    index = 0

    # in this case it is not possible to find a valid coloring with 2 colors for a cycle of 4 nodes
    assert util_color(graph, max_colors, colored_vertices, index) == False
