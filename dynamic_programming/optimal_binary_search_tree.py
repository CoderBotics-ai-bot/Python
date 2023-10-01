#!/usr/bin/env python3

# This Python program implements an optimal binary search tree (abbreviated BST)
# building dynamic programming algorithm that delivers O(n^2) performance.
#
# The goal of the optimal BST problem is to build a low-cost BST for a
# given set of nodes, each with its own key and frequency. The frequency
# of the node is defined as how many time the node is being searched.
# The search cost of binary search tree is given by this formula:
#
# cost(1, n) = sum{i = 1 to n}((depth(node_i) + 1) * node_i_freq)
#
# where n is number of nodes in the BST. The characteristic of low-cost
# BSTs is having a faster overall search time than other implementations.
# The reason for their fast search time is that the nodes with high
# frequencies will be placed near the root of the tree while the nodes
# with low frequencies will be placed near the leaves of the tree thus
# reducing search time in the most frequent instances.
import sys
from random import randint


from typing import List
from typing import List, Tuple
import sys


from typing import List, Tuple
import sys
from collections import namedtuple

Node = namedtuple("Node", ["key", "freq"])


class Node:
    """Binary Search Tree Node"""

    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __str__(self):
        """
        >>> str(Node(1, 2))
        'Node(key=1, freq=2)'
        """
        return f"Node(key={self.key}, freq={self.freq})"


def print_binary_search_tree(
    root: List[List[int]], key: List[int], i: int, j: int, parent: int, is_left: bool
) -> None:
    """Refactored function to print the structure of a Binary Search Tree (BST) from a root table."""
    if i > j or i < 0 or j > len(root) - 1:
        return

    node_key = key[root[i][j]]

    is_root = parent == -1
    relationship = "left" if is_left else "right"

    print_node_relationship(node_key, parent, relationship if not is_root else "")

    new_parent = node_key
    print_binary_search_tree(root, key, i, root[i][j] - 1, new_parent, True)
    print_binary_search_tree(root, key, root[i][j] + 1, j, new_parent, False)



def print_node_relationship(key_node: int, parent: int, relationship: str) -> None:
    """Helper function to print the key-node relationship."""
    node = "root" if parent == -1 else f"{relationship} child of key {parent}"
    print(f"{key_node} is the {node} of the binary search tree.")


def main():
    # A sample binary search tree
    nodes = [Node(i, randint(1, 50)) for i in range(10, 0, -1)]
    find_optimal_binary_search_tree(nodes)



def find_optimal_binary_search_tree(nodes: List[Node]) -> None:
    nodes.sort(key=lambda node: node.key)
    n = len(nodes)

    keys, freqs = get_keys_and_freqs(nodes, n)
    dp, total, root = initialize_matrices(freqs, n)

    dp, root = process_intervals(dp, total, root, freqs, n)
    print_optimized_binary_search_tree(dp, nodes, root, keys, n)


if __name__ == "__main__":
    main()


def get_keys_and_freqs(nodes: List[Node], n: int) -> Tuple[List[int], List[int]]:
    keys = [nodes[i].key for i in range(n)]
    freqs = [nodes[i].freq for i in range(n)]
    return keys, freqs


def initialize_matrices(
    freqs: List[int], n: int
) -> Tuple[List[List[int]], List[List[int]], List[List[int]]]:
    dp = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
    total = [[freqs[i] if i == j else 0 for j in range(n)] for i in range(n)]
    root = [[i if i == j else 0 for j in range(n)] for i in range(n)]
    return dp, total, root


def process_intervals(
    dp: List[List[int]],
    total: List[List[int]],
    root: List[List[int]],
    freqs: List[int],
    n: int,
) -> Tuple[List[List[int]], List[List[int]]]:
    for interval_length in range(2, n + 1):
        for i in range(n - interval_length + 1):
            j = i + interval_length - 1

            dp[i][j] = sys.maxsize  # set the value to "infinity"
            total[i][j] = total[i][j - 1] + freqs[j]

            # Apply Knuth's optimization
            # Loop without optimization: for r in range(i, j + 1):
            for r in range(root[i][j - 1], root[i + 1][j] + 1):  # r is a temporary root
                left = dp[i][r - 1] if r != i else 0  # optimal cost for left subtree
                right = dp[r + 1][j] if r != j else 0  # optimal cost for right subtree
                cost = left + total[i][j] + right

                if dp[i][j] > cost:
                    dp[i][j] = cost
                    root[i][j] = r
    return dp, root


def print_optimized_binary_search_tree(
    dp: List[List[int]],
    nodes: List[Node],
    root: List[List[int]],
    keys: List[int],
    n: int,
) -> None:
    print("Binary search tree nodes:")
    for node in nodes:
        print(node)

    print(f"\nThe cost of optimal BST for given tree nodes is {dp[0][n - 1]}.")
    print_binary_search_tree(root, keys, 0, n - 1, -1, False)
