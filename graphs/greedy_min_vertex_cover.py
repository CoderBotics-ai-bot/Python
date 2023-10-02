"""
* Author: Manuel Di Lullo (https://github.com/manueldilullo)
* Description: Approximization algorithm for minimum vertex cover problem.
               Greedy Approach. Uses graphs represented with an adjacency list
URL: https://mathworld.wolfram.com/MinimumVertexCover.html
URL: https://cs.stackexchange.com/questions/129017/greedy-algorithm-for-vertex-cover
"""

import heapq


from typing import Dict, List, Set

def greedy_min_vertex_cover(graph: Dict[int, List[int]]) -> Set[int]:
    """
    This is a greedily implemented approximate algorithm for minimum vertex cover problem.

    The function takes an undirected graph, represented as an adjacency list where the keys are nodes (represented as
    integers) and their values are a list of adjacent nodes. It returns a set of nodes comprising the minimum vertex
    cover for the graph.

    The method works by maintaining a priority queue of nodes in the graph, where the key is the node's degree. At each
    iteration, it pops the node with highest degree (i.e., has the most edges incident on it). This node is added to
    the selected vertices (i.e., vertex cover). All edges incident on this selected node are then removed from the graph.
    This process is repeated until either the queue is empty or there are no more edges left in the graph.

    Algorithm complexity is O(nlogn), where n is number of nodes in the graph, as for each node we push and pop it
    from the heap.

    Args:
        graph (Dict[int, List[int]]): The input graph as an adjacency list where keys are integers representing nodes
                                       and values are list of nodes indicating an edge.

    Returns:
        Set[int]: A set of integers representing the nodes in the minimum vertex cover.

    Example:
        >>> graph = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
        >>> greedy_min_vertex_cover(graph)
        {0, 1, 2, 4}
    """
    queue = build_queue(graph)
    chosen_vertices = select_vertices(queue)

    return chosen_vertices


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    graph = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    print(f"Minimum vertex cover:\n{greedy_min_vertex_cover(graph)}")


def build_queue(graph: Dict[int, List[int]]) -> list:
    queue = []
    for key, value in graph.items():
        heapq.heappush(queue, [-1 * len(value), (key, value)])
    return queue


def select_vertices(queue: list) -> Set[int]:
    chosen_vertices = set()
    while queue and queue[0][0] != 0:
        argmax = heapq.heappop(queue)[1][0]
        chosen_vertices.add(argmax)
        update_queue(queue, argmax)
    return chosen_vertices


def update_queue(queue: list, argmax: int) -> None:
    for elem in queue:
        if elem[0] == 0:
            continue
        if argmax in elem[1][1]:
            index = elem[1][1].index(argmax)
            del elem[1][1][index]
            elem[0] += 1
    heapq.heapify(queue)
