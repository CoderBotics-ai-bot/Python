"""
pseudo-code

DIJKSTRA(graph G, start vertex s, destination vertex d):

//all nodes initially unexplored

1 -  let H = min heap data structure, initialized with 0 and s [here 0 indicates
     the distance from start vertex s]
2 -  while H is non-empty:
3 -    remove the first node and cost of H, call it U and cost
4 -    if U has been previously explored:
5 -      go to the while loop, line 2 //Once a node is explored there is no need
         to make it again
6 -    mark U as explored
7 -    if U is d:
8 -      return cost // total cost from start to destination vertex
9 -    for each edge(U, V): c=cost of edge(U,V) // for V in graph[U]
10 -     if V explored:
11 -       go to next V in line 9
12 -     total_cost = cost + c
13 -     add (total_cost,V) to H

You can think at cost as a distance where Dijkstra finds the shortest distance
between vertices s and v in a graph G. The use of a min heap as H guarantees
that if a vertex has already been explored there will be no other path with
shortest distance, that happens because heapq.heappop will always return the
next vertex with the shortest distance, considering that the heap stores not
only the distance between previous vertex and current vertex but the entire
distance between each vertex that makes up the path from start vertex to target
vertex.
"""
import heapq
from typing import Dict
from typing import List, Tuple, Dict
from typing import List, Tuple, Dict



def dijkstra(graph: Dict[str, List[Tuple[str, int]]], start: str, end: str) -> int:
    """
    In the given graph, it finds the shortest path from start to end and returns it's cost. If the end is not reachable from start it returns -1.
    """
    heap = [(0, start)]  # cost from start node, end node
    visited = set()

    while heap:
        (cost, current_node) = heapq.heappop(heap)
        if current_node in visited:
            continue

        visited.add(current_node)
        if current_node == end:
            return cost

        push_to_heap_unvisited_neighbors(graph, heap, visited, cost, current_node)

    return -1


G = {
    "A": [["B", 2], ["C", 5]],
    "B": [["A", 2], ["D", 3], ["E", 1], ["F", 1]],
    "C": [["A", 5], ["F", 3]],
    "D": [["B", 3]],
    "E": [["B", 4], ["F", 3]],
    "F": [["C", 3], ["E", 3]],
}


def push_to_heap_unvisited_neighbors(
    graph: Dict[str, List[Tuple[str, int]]],
    heap: List[Tuple[int, str]],
    visited: set,
    cost: int,
    current_node: str,
):
    """
    Helper function for dijkstra(). It pushes unvisited neighbors of current_node into the heap.
    """
    for neighbor, cost_to_travel in graph[current_node]:
        if neighbor not in visited:
            total_cost = cost + cost_to_travel
            heapq.heappush(heap, (total_cost, neighbor))

r"""
Layout of G2:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    ----------------- 3 --------------------
"""
G2 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["F", 3]],
    "F": [],
}

r"""
Layout of G3:

E -- 1 --> B -- 1 --> C -- 1 --> D -- 1 --> F
 \                                         /\
  \                                        ||
    -------- 2 ---------> G ------- 1 ------
"""
G3 = {
    "B": [["C", 1]],
    "C": [["D", 1]],
    "D": [["F", 1]],
    "E": [["B", 1], ["G", 2]],
    "F": [],
    "G": [["F", 1]],
}

short_distance = dijkstra(G, "E", "C")
print(short_distance)  # E -- 3 --> F -- 3 --> C == 6

short_distance = dijkstra(G2, "E", "F")
print(short_distance)  # E -- 3 --> F == 3

short_distance = dijkstra(G3, "E", "F")
print(short_distance)  # E -- 2 --> G -- 1 --> F == 3

if __name__ == "__main__":
    import doctest

    doctest.testmod()
