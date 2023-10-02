"""
You are given a tree(a simple connected graph with no cycles). The tree has N
nodes numbered from 1 to N and is rooted at node 1.

Find the maximum number of edges you can remove from the tree to get a forest
such that each connected component of the forest contains an even number of
nodes.

Constraints
2 <= 2 <= 100

Note: The tree input will be such that it can always be decomposed into
components containing an even number of nodes.
"""
# pylint: disable=invalid-name
from collections import defaultdict

def dfs(start: int) -> int:
    """
    Performs a depth-first search (DFS) on a tree.

    This function is a recursive method that starts at a specified node,
    then explores as far as possible along each branch before backtracking.
    It marks nodes as visited to avoid revisiting the same node.
    It also keeps track of all nodes whose subtree contains an even number of nodes.

    Args:
        start (int): The starting node of the DFS.

    Returns:
        int: The total number of nodes in the subtree rooted at 'start'.

    Side Effects:
        Modifies the 'visited' and 'cuts' global lists. 'visited' is used to
        keep track of visited nodes. 'cuts' collects all nodes whose subtree contains
        an even number of nodes.

    Raises:
        Does not raise any errors or exceptions.
    """
    # pylint: disable=redefined-outer-name
    ret = 1
    visited[start] = True

    ret += handle_child_nodes(start)

    if ret % 2 == 0:
        cuts.append(start)

    return ret


def even_tree():
    """
    2 1
    3 1
    4 3
    5 2
    6 1
    7 2
    8 6
    9 8
    10 8
    On removing edges (1,3) and (1,6), we can get the desired result 2.
    """
    dfs(1)


def handle_child_nodes(node: int) -> int:
    """
    Handle child nodes for a given node in the DFS function.

    Args:
        node (int): Node whose children are to be handled.

    Returns:
        int: The count of total number of nodes in subtree rooted at each child of 'node'.

    """
    ret = 0
    for v in tree[node]:
        if v not in visited:
            ret += dfs(v)
    return ret


if __name__ == "__main__":
    n, m = 10, 9
    tree = defaultdict(list)
    visited: dict[int, bool] = {}
    cuts: list[int] = []
    count = 0
    edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    even_tree()
    print(len(cuts) - 1)
