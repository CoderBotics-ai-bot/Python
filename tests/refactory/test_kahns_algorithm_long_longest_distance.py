from graphs.kahns_algorithm_long import *
import pytest


def longest_distance(graph: dict) -> int:
    """
    Returns the longest distance in a Directed Acyclic Graph using Kahns Algorithm.

    Parameters:
    graph (dict): The graph represented as adjacency dictionary.

    Returns:
    int: The longest distance in the graph.
    """
    indegree = [0] * len(graph)
    queue = []
    long_dist = [1] * len(graph)

    for values in graph.values():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        for x in graph[vertex]:
            indegree[x] -= 1

            if long_dist[vertex] + 1 > long_dist[x]:
                long_dist[x] = long_dist[vertex] + 1

            if indegree[x] == 0:
                queue.append(x)

    return max(long_dist)


def test_longest_distance():
    graph = {0: [1, 2], 1: [3], 2: [4], 3: [], 4: []}
    output = longest_distance(graph)
    assert output is not None


def test_longest_distance_single_node():
    graph = {0: []}
    output = longest_distance(graph)
    assert output == 1


def test_longest_distance_large_graph():
    graph = {i: [i + 1 for i in range(10)] for i in range(13)}
    output = longest_distance(graph)
    assert output is not None


def test_longest_distance_no_links():
    graph = {i: [] for i in range(10)}
    output = longest_distance(graph)
    assert output == 1
