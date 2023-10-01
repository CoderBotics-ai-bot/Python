"""
An implementation of Karger's Algorithm for partitioning a graph.
"""

from __future__ import annotations

import random


from typing import Dict, List, Set, Tuple

# Adjacency list representation of this graph:
# https://en.wikipedia.org/wiki/File:Single_run_of_Karger%E2%80%99s_Mincut_algorithm.svg
TEST_GRAPH = {
    "1": ["2", "3", "4", "5"],
    "2": ["1", "3", "4", "5"],
    "3": ["1", "2", "4", "5", "10"],
    "4": ["1", "2", "3", "5", "6"],
    "5": ["1", "2", "3", "4", "7"],
    "6": ["7", "8", "9", "10", "4"],
    "7": ["6", "8", "9", "10", "5"],
    "8": ["6", "7", "9", "10"],
    "9": ["6", "7", "8", "10"],
    "10": ["6", "7", "8", "9", "3"],
}

def partition_graph(graph: Dict[str, List[str]]) -> Set[Tuple[str, str]]:
    """
    Contract the graph until only two nodes exist and return the cutset.
    """
    graph_copy = get_copy_with_all_nodes(graph)
    contract_all_edges(graph_copy)

    groups = get_nodes_in_each_group(graph_copy)

    return get_cutset(graph, groups)


if __name__ == "__main__":
    print(partition_graph(TEST_GRAPH))


def get_copy_with_all_nodes(graph: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Get a copy of the graph with mapping of all nodes to themselves.
    Each node in the graph is represented as a list of strings.
    """
    return {node: graph[node][:] for node in graph}


def get_random_nodes(graph: Dict[str, List[str]]) -> Tuple[str, str]:
    """
    In a given graph, select a random edge and return the nodes.
    """
    node_u = random.choice(list(graph.keys()))
    node_v = random.choice(graph[node_u])

    return node_u, node_v


def contract_edge(graph: Dict[str, List[str]], node_u: str, node_v: str) -> None:
    """
    Contract the selected edge to a new node and update its neighbors.
    """
    contracted_node = node_u + node_v
    contracted_node_neighbors = set(graph[node_u] + graph[node_v])

    graph[contracted_node] = list(
        contracted_node_neighbors.difference({node_u, node_v})
    )

    for neighbor in graph[contracted_node]:
        graph[neighbor].append(contracted_node)


def remove_nodes(graph: Dict[str, List[str]], node_u: str, node_v: str) -> None:
    """
    Remove the selected nodes from the given graph.
    """
    del graph[node_u]
    del graph[node_v]

    for node in graph.keys():
        graph[node] = [
            neighbor for neighbor in graph[node] if neighbor not in {node_u, node_v}
        ]


def contract_all_edges(graph: Dict[str, List[str]]) -> None:
    """
    Keep contracting the edges until only two nodes exist in the given graph.
    """
    while len(graph) > 2:
        node_u, node_v = get_random_nodes(graph)
        contract_edge(graph, node_u, node_v)
        remove_nodes(graph, node_u, node_v)


def get_nodes_in_each_group(graph: Dict[str, List[str]]) -> List[List[str]]:
    """
    Make a list of all nodes present in each of the remaining nodes in the graph.
    """
    return [list(node) for node in graph.keys()]


def get_cutset(
    graph: Dict[str, List[str]], groups: List[List[str]]
) -> Set[Tuple[str, str]]:
    """
    Get a set of tuple pairs representing the edges in the partition cutset.
    """
    return {
        (node, neighbor)
        for node in groups[0]
        for neighbor in graph[node]
        if neighbor in groups[1]
    }
