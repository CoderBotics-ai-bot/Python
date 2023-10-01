"""
Author: https://github.com/bhushan-borole
"""


from typing import Dict, List


from typing import Dict, List, Tuple
"""
The input graph for the algorithm is:

  A B C
A 0 1 1
B 0 0 1
C 1 0 0

"""

graph = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]


class Node:
    def __init__(self, name):
        self.name = name
        self.inbound = []
        self.outbound = []

    def add_inbound(self, node):
        self.inbound.append(node)

    def add_outbound(self, node):
        self.outbound.append(node)

    def __repr__(self):
        return f"<node={self.name} inbound={self.inbound} outbound={self.outbound}>"

def page_rank(nodes: List["Node"], limit: int = 3, d: float = 0.85) -> Dict[str, float]:
    """
    Calculate the PageRank of nodes in a network.

    This function implements the Google PageRank algorithm to determine the importance
    of nodes (web pages) in a network (the World Wide Web), based on their inbound and
    outbound connections.

    Parameters:
    nodes (List['Node']): A list of nodes in the network. Each node should have a 'name' attribute,
                          an 'inbound' attribute (a list of names of nodes from where it receives links),
                          and an 'outbound' attribute (a list of names of nodes to where it links).
    limit (int): The maximum number of iterations to perform. Default is 3.
    d (float): Damping factor, typically set to 0.85. Default is 0.85.

    Returns:
    ranks (Dict[str, float]): A dictionary mapping from node name to its calculated PageRank.
    """
    ranks, outbounds = initialize_ranks(nodes)

    for _ in range(limit):
        ranks = iterate_rank_calculation(d, nodes, ranks, outbounds)

    return ranks

def main() -> None:
    """
    Main function to calculate and display the PageRank of nodes in a graph.

    This function requests the user to input the names of the nodes, creates the nodes,
    assigns inbound and outbound connections based on predefined adjacency matrix (graph),
    and finally calculates and displays the PageRank for each node using the page_rank function.
    """
    nodes = get_nodes()

    assign_connections(nodes)

    display_nodes(nodes)

    page_rank(nodes)


def initialize_ranks(nodes: List["Node"]) -> Tuple[Dict[str, float], Dict[str, int]]:
    """Initializes and returns rank values and outbound values for nodes"""
    ranks = {node.name: 1 for node in nodes}
    outbounds = {node.name: len(node.outbound) for node in nodes}
    return ranks, outbounds


def get_nodes() -> List[Node]:
    """
    Function to get a list of nodes from user input.
    """
    names = list(input("Enter Names of the Nodes: ").split())
    return [Node(name) for name in names]


def assign_connections(nodes: List[Node]) -> None:
    """
    Function to assign inbound and outbound connections for nodes.
    """
    for ri, row in enumerate(graph):
        for ci, col in enumerate(row):
            if col == 1:
                nodes[ci].add_inbound(nodes[ri].name)
                nodes[ri].add_outbound(nodes[ci].name)


def display_nodes(nodes: List[Node]) -> None:
    """
    Function to Display the nodes.
    """
    print("======= Nodes =======")
    for node in nodes:
        print(node)


def iterate_rank_calculation(
    d: float, nodes: List["Node"], ranks: Dict[str, float], outbounds: Dict[str, int]
) -> Dict[str, float]:
    """Calculates rank values for a single iteration"""
    return {
        node.name: (1 - d) + d * sum(ranks[ib] / outbounds[ib] for ib in node.inbound)
        for node in nodes
    }


if __name__ == "__main__":
    main()
