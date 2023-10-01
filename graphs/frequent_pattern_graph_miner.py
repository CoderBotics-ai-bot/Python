"""
FP-GraphMiner - A Fast Frequent Pattern Mining Algorithm for Network Graphs

A novel Frequent Pattern Graph Mining algorithm, FP-GraphMiner, that compactly
represents a set of network graphs as a Frequent Pattern Graph (or FP-Graph).
This graph can be used to efficiently mine frequent subgraphs including maximal
frequent subgraphs and maximum common subgraphs.

URL: https://www.researchgate.net/publication/235255851
"""
from typing import List


from typing import List
from typing import Dict, List, Union


from typing import Dict, List, Tuple, Union
# fmt: off
edge_array = [
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12', 'cd-e2', 'ce-e4',
     'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3', 'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'cd-e2', 'de-e1', 'df-e8',
     'ef-e3', 'eg-e2', 'fg-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'de-e1', 'df-e8', 'dg-e5', 'ef-e3', 'eg-e2',
     'eh-e12', 'fg-e6', 'fh-e10', 'gh-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'bh-e12', 'cd-e2', 'df-e8', 'dh-e10'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'cd-e2', 'ce-e4', 'de-e1', 'df-e8',
     'dg-e5', 'ef-e3', 'eg-e2', 'fg-e6']
]
# fmt: on


def get_distinct_edge(edge_array):
    """
    Return Distinct edges from edge array of multiple graphs
    >>> sorted(get_distinct_edge(edge_array))
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    distinct_edge = set()
    for row in edge_array:
        for item in row:
            distinct_edge.add(item[0])
    return list(distinct_edge)


def get_frequency_table(edge_array):
    """
    Returns Frequency Table
    """
    distinct_edge = get_distinct_edge(edge_array)
    frequency_table = {}

    for item in distinct_edge:
        bit = get_bitcode(edge_array, item)
        # print('bit',bit)
        # bt=''.join(bit)
        s = bit.count("1")
        frequency_table[item] = [s, bit]
    # Store [Distinct edge, WT(Bitcode), Bitcode] in descending order
    sorted_frequency_table = [
        [k, v[0], v[1]]
        for k, v in sorted(frequency_table.items(), key=lambda v: v[1][0], reverse=True)
    ]
    return sorted_frequency_table



def get_bitcode(edge_array: List[List[str]], distinct_edge: str) -> str:
    """
    Returns the bitcode of the distinct_edge in the edge array.

    The bitcode represents the presence of an edge in each row of the edge array.
    It is a string of 1's and 0's, where '1' represents the presence of distinct_edge
    in the row and '0' represents the absence.

    Args:
        edge_array (List[List[str]]): The array of edge lists.
        distinct_edge (str): The distinct edge for which to compute the bitcode.

    Returns:
        str: The bitcode represented as a string.
    """
    bitcode = ["0"] * len(edge_array)  # Initialize bitcode with '0's
    for i, row in enumerate(edge_array):
        for item in row:
            if distinct_edge in item:
                bitcode[i] = "1"
                break
    return "".join(bitcode)


def get_nodes(frequency_table):
    """
    Returns nodes
    format nodes={bitcode:edges that represent the bitcode}
    >>> get_nodes([['ab', 5, '11111'], ['ac', 5, '11111'], ['df', 5, '11111'],
    ...            ['bd', 5, '11111'], ['bc', 5, '11111']])
    {'11111': ['ab', 'ac', 'df', 'bd', 'bc']}
    """
    nodes = {}
    for _, item in enumerate(frequency_table):
        nodes.setdefault(item[2], []).append(item[0])
    return nodes


def get_cluster(nodes):
    """
    Returns cluster
    format cluster:{WT(bitcode):nodes with same WT}
    """
    cluster = {}
    for key, value in nodes.items():
        cluster.setdefault(key.count("1"), {})[key] = value
    return cluster


def get_support(cluster):
    """
    Returns support
    >>> get_support({5: {'11111': ['ab', 'ac', 'df', 'bd', 'bc']},
    ...              4: {'11101': ['ef', 'eg', 'de', 'fg'], '11011': ['cd']},
    ...              3: {'11001': ['ad'], '10101': ['dg']},
    ...              2: {'10010': ['dh', 'bh'], '11000': ['be'], '10100': ['gh'],
    ...                  '10001': ['ce']},
    ...              1: {'00100': ['fh', 'eh'], '10000': ['hi']}})
    [100.0, 80.0, 60.0, 40.0, 20.0]
    """
    return [i * 100 / len(cluster) for i in cluster]

def print_all() -> None:
    """
    Prints the content of all global structures: nodes, support, cluster, graph, and frequent subgraph edge list.

    This is a utility function intended for debugging or monitoring the progress of the algorithm. It does not
    return any value. The function fetches and prints the state of global variables directly. It should be noted
    that this function relies on the following global variables:

    - nodes: a dictionary containing all graph nodes.
    - support: a dictionary containing supporting information for the graph.
    - cluster: a dictionary containing information about the clusters in the graph.
    - graph: a dictionary representing the graph itself.
    - freq_subgraph_edge_list: a list containing frequent subgraph edges.
    """
    _print_nodes()
    _print_support()
    _print_cluster()
    _print_graph()
    _print_freq_subgraph_edge_list()



def create_edge(
    nodes: Dict[str, List[str]],
    graph: Dict[Union[str, Tuple[str]], List[List[str]]],
    cluster: Dict[int, List[str]],
    c1: int,
) -> None:
    """
    Create edges between the nodes if certain conditions are met.

    Given a dictionary of nodes, an initially empty graph, a dictionary of clusters,
    and a cluster number, this function creates edges between nodes in the graph if
    there is a bitwise similarity between them. The condition for similarity is when
    bitwise 'And' operation between any two nodes in different clusters results in a
    value equal to the value of the first node.

    Args:
    nodes (dict): Dictionary with key as a binary string and value as a list of strings.
    graph (dict): Empty dictionary construct edges from nodes.
    cluster (dict): Dictionary with keys as cluster numbers and values as identifiers of nodes.
    c1 (int): Current cluster number.

    Side Effect:
    This function does not return anything but it modifies the graph dictionary in-place
    by adding new edges to it.

    Note:
    'c1 + 1' and 'max(cluster.keys())' ensure that edges are only created between nodes
    in subsequent clusters and not within the same cluster.
    """

    for i in cluster[c1]:
        count = 0
        c2 = c1 + 1
        max_cluster_key = max(cluster.keys())
        while c2 < max_cluster_key:
            node_edges = get_node_edges(nodes, cluster, i, c2, count)
            graph.update(node_edges)
            if node_edges:
                break
            c2 += 1


def _print_nodes() -> None:
    print("\nNodes\n")
    for key, value in nodes.items():
        print(key, value)


def get_node_edges(
    nodes: Dict[str, List[str]],
    cluster: Dict[int, List[str]],
    current_node: str,
    c2: int,
    edge_count: int,
) -> Dict[Union[str, Tuple[str]], List[List[str]]]:
    """
    Get edges of the current node with nodes of the next cluster based on bitwise similarity.

    Args:
    nodes (dict): Dictionary with key as binary string and value as list of strings.
    cluster (dict): Dictionary with keys as cluster numbers and values as lists of binary string identifiers.
    current_node (str): Identifier of current node as a binary string.
    c2 (int): Identifier of the next cluster.
    edge_count: Number of edges created so far.

    Returns:
    (dict): New edges of the current node with nodes of the next cluster.
    """

    node_edges = {}
    for next_node in cluster[c2]:
        if is_bitwise_similar(current_node, next_node):
            if tuple(nodes[current_node]) in node_edges:
                node_edges[tuple(nodes[current_node])].append(nodes[next_node])
            else:
                node_edges[tuple(nodes[current_node])] = [nodes[next_node]]
            edge_count += 1
    return node_edges if edge_count else {}


def is_bitwise_similar(node1: str, node2: str) -> bool:
    """
    Check if two nodes are bitwise similar.

    Two nodes are bitwise similar if the result of bitwise 'And' operation between
    their binary string identifiers is equal to the identifier of the first node.

    Args:
    node1 (str): Identifier of the first node as binary string.
    node2 (str): Identifier of the second node as binary string.

    Returns:
    (bool): Bitwise similarity between the nodes.
    """

    return int(node1, 2) & int(node2, 2) == int(node1, 2)


def _print_support() -> None:
    print("\nSupport\n")
    print(support)


def _print_cluster() -> None:
    print("\n Cluster \n")
    for key, value in sorted(cluster.items(), reverse=True):
        print(key, value)


def _print_graph() -> None:
    print("\n Graph\n")
    for key, value in graph.items():
        print(key, value)


def _print_freq_subgraph_edge_list() -> None:
    print("\n Edge List of Frequent subgraphs \n")
    for edge_list in freq_subgraph_edge_list:
        print(edge_list)


def construct_graph(cluster, nodes):
    x = cluster[max(cluster.keys())]
    cluster[max(cluster.keys()) + 1] = "Header"
    graph = {}
    for i in x:
        if (["Header"],) in graph:
            graph[(["Header"],)].append(x[i])
        else:
            graph[(["Header"],)] = [x[i]]
    for i in x:
        graph[(x[i],)] = [["Header"]]
    i = 1
    while i < max(cluster) - 1:
        create_edge(nodes, graph, cluster, i)
        i = i + 1
    return graph


def my_dfs(graph, start, end, path=None):
    """
    find different DFS walk from given node to Header node
    """
    path = (path or []) + [start]
    if start == end:
        paths.append(path)
    for node in graph[start]:
        if tuple(node) not in path:
            my_dfs(graph, tuple(node), end, path)


def find_freq_subgraph_given_support(s, cluster, graph):
    """
    find edges of multiple frequent subgraphs
    """
    k = int(s / 100 * (len(cluster) - 1))
    for i in cluster[k]:
        my_dfs(graph, tuple(cluster[k][i]), (["Header"],))


def freq_subgraphs_edge_list(paths):
    """
    returns Edge list for frequent subgraphs
    """
    freq_sub_el = []
    for edges in paths:
        el = []
        for j in range(len(edges) - 1):
            temp = list(edges[j])
            for e in temp:
                edge = (e[0], e[1])
                el.append(edge)
        freq_sub_el.append(el)
    return freq_sub_el


def preprocess(edge_array):
    """
    Preprocess the edge array
    >>> preprocess([['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12',
    ...              'cd-e2', 'ce-e4', 'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3',
    ...              'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3']])

    """
    for i in range(len(edge_array)):
        for j in range(len(edge_array[i])):
            t = edge_array[i][j].split("-")
            edge_array[i][j] = t


if __name__ == "__main__":
    preprocess(edge_array)
    frequency_table = get_frequency_table(edge_array)
    nodes = get_nodes(frequency_table)
    cluster = get_cluster(nodes)
    support = get_support(cluster)
    graph = construct_graph(cluster, nodes)
    find_freq_subgraph_given_support(60, cluster, graph)
    paths: list = []
    freq_subgraph_edge_list = freq_subgraphs_edge_list(paths)
    print_all()
