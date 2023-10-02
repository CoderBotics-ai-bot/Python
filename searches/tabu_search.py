"""
This is pure Python implementation of Tabu search algorithm for a Travelling Salesman
Problem, that the distances between the cities are symmetric (the distance between city
'a' and city 'b' is the same between city 'b' and city 'a').
The TSP can be represented into a graph. The cities are represented by nodes and the
distance between them is represented by the weight of the ark between the nodes.

The .txt file with the graph has the form:

node1 node2 distance_between_node1_and_node2
node1 node3 distance_between_node1_and_node3
...

Be careful node1, node2 and the distance between them, must exist only once. This means
in the .txt file should not exist:
node1 node2 distance_between_node1_and_node2
node2 node1 distance_between_node2_and_node1

For pytests run following command:
pytest

For manual testing run:
python tabu_search.py -f your_file_name.txt -number_of_iterations_of_tabu_search \
    -s size_of_tabu_search
e.g. python tabu_search.py -f tabudata2.txt -i 4 -s 3
"""
import argparse
import copy


from typing import List
from typing import Tuple, List, Dict


from typing import Tuple, List, Dict


from typing import Union


from typing import List, Dict, Union


from typing import List, Dict, Tuple

def tabu_search(
    first_solution: List[str],
    distance_of_first_solution: int,
    dict_of_neighbours: Dict[str, List[List[str]]],
    iters: int,
    size: int,
) -> Tuple[List[str], int]:
    best_cost = distance_of_first_solution
    best_solution_ever = solution = first_solution
    tabu_list = []

    for count in range(1, iters + 1):
        next_solution, next_cost = find_best_neighbour(
            solution, dict_of_neighbours, tabu_list
        )

        if next_solution:
            # If a valid solution was found, update the current solution and tabu list
            tabu_list = update_tabu_list(tabu_list, solution, next_solution, size)
            solution = next_solution[:-1]

            # Check and update if the best solution so far
            if next_cost < best_cost:
                best_cost = next_cost
                best_solution_ever = solution

    return best_solution_ever, best_cost

def find_neighborhood(
    solution: List[str], dict_of_neighbours: Dict[str, List[List[str]]]
) -> List[List[Union[str, int]]]:
    """
    Generate neighborhoods for a solution in decreasing order of total distance.
    """

    neighborhood_of_solution = []

    for idx1, n in enumerate(solution[1:-1], start=1):
        for idx2, kn in enumerate(solution[1:-1], start=1):
            if n == kn:
                continue
            new_solution = _exchange_nodes(solution, idx1, idx2)
            distance = _calculate_distance(new_solution, dict_of_neighbours)
            new_solution.append(distance)

            if new_solution not in neighborhood_of_solution:
                neighborhood_of_solution.append(new_solution)

    neighborhood_of_solution.sort(key=lambda x: x[-1])

    return neighborhood_of_solution


def update_tabu_list(
    tabu_list: List[List[str]], solution: List[str], next_solution: List[str], size: int
) -> List[List[str]]:
    first_exchange_node, second_exchange_node = get_exchanged_nodes(
        solution, next_solution
    )
    tabu_list.append([first_exchange_node, second_exchange_node])

    if len(tabu_list) >= size:
        tabu_list.pop(0)

    return tabu_list


def get_exchanged_nodes(
    solution: List[str], next_solution: List[str]
) -> Tuple[str, str]:
    for i in range(len(solution)):
        if next_solution[i] != solution[i]:
            return next_solution[i], solution[i]


def find_best_neighbour(
    solution: List[str],
    dict_of_neighbours: Dict[str, List[List[str]]],
    tabu_list: List[List[str]],
) -> Tuple[List[str], int]:
    neighbourhood = find_neighborhood(solution, dict_of_neighbours)

    for neighbour in neighbourhood:
        first_exchange_node, second_exchange_node = get_exchanged_nodes(
            solution, neighbour[:-1]
        )

        if [first_exchange_node, second_exchange_node] not in tabu_list and [
            second_exchange_node,
            first_exchange_node,
        ] not in tabu_list:
            return neighbour[:-1], neighbour[-1]  # the next solution and its cost

    return None, None  # Return None if no valid neighbour is found

MAX_DISTANCE = 10000


def _exchange_nodes(solution: List[str], idx1: int, idx2: int) -> List[str]:
    """
    Return a new solution where nodes at idx1 and idx2 are swapped.
    """
    new_solution = solution.copy()
    new_solution[idx1], new_solution[idx2] = new_solution[idx2], new_solution[idx1]
    return new_solution


def _calculate_distance(
    solution: List[str], dict_of_neighbours: Dict[str, List[List[str]]]
) -> int:
    """
    Calculate the total distance of a solution.
    """
    distance = 0
    for current_node, next_node in zip(solution, solution[1:]):
        neighbors = dict_of_neighbours[current_node]
        for neighbor, neighbor_distance in neighbors:
            if neighbor == next_node:
                distance += int(neighbor_distance)
                break
    return distance

def generate_neighbours(path: str) -> dict:
    """
    :param path: Path to the .txt file that includes the graph.
    :return: A dictionary with each node as a key, and a list of [neighbor, cost] lists as values.
    """

    def add_neighbor(dictionary: dict, key: str, value: list):
        """Helper function to add a neighbor to the dictionary."""
        dictionary[key] = dictionary.get(key, []) + [value]

    neighbors_dict = {}

    with open(path) as file:
        for line in file:
            node, neighbor, cost = line.split()
            add_neighbor(neighbors_dict, node, [neighbor, cost])
            add_neighbor(neighbors_dict, neighbor, [node, cost])

    return neighbors_dict


def generate_first_solution(
    path: str, dict_of_neighbours: Dict[str, List[List[str]]]
) -> Tuple[List[str], int]:
    with open(path) as f:
        start_node = f.read(1)
    first_solution = []
    distance_of_first_solution = 0
    visiting = start_node

    while visiting not in first_solution:
        best_node, min_distance = find_node_with_min_dist(
            visiting, dict_of_neighbours, first_solution
        )
        if not best_node:
            break  # break if there is no neighbour to visit
        first_solution.append(visiting)
        distance_of_first_solution += min_distance
        visiting = best_node

    first_solution.append(start_node)
    distance_of_first_solution += calculate_total_distance(
        first_solution[-2], start_node, dict_of_neighbours
    )
    return first_solution, distance_of_first_solution



def find_node_with_min_dist(
    node: str, dict_of_neighbours: Dict[str, List[List[str]]], first_solution: List[str]
) -> Tuple[str, int]:
    """Find the node with the minimum distance from the given node and not in first_solution"""

    neighbours = [
        (int(k[1]), k[0])
        for k in dict_of_neighbours[node]
        if k[0] not in first_solution
    ]
    if not neighbours:  # if no neighbours are found
        return "", MAX_DISTANCE
    min_distance, best_node = min(neighbours)
    return best_node, min_distance


def calculate_total_distance(
    node: str, start_node: str, dict_of_neighbours: Dict[str, List[List[str]]]
) -> int:
    """Calculate the total distance to the start node from the given node"""
    position = next(
        i
        for i, neighbour in enumerate(dict_of_neighbours[node])
        if neighbour[0] == start_node
    )
    return int(dict_of_neighbours[node][position][1]) - MAX_DISTANCE


def main(args=None):
    dict_of_neighbours = generate_neighbours(args.File)

    first_solution, distance_of_first_solution = generate_first_solution(
        args.File, dict_of_neighbours
    )

    best_sol, best_cost = tabu_search(
        first_solution,
        distance_of_first_solution,
        dict_of_neighbours,
        args.Iterations,
        args.Size,
    )

    print(f"Best solution: {best_sol}, with total distance: {best_cost}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tabu Search")
    parser.add_argument(
        "-f",
        "--File",
        type=str,
        help="Path to the file containing the data",
        required=True,
    )
    parser.add_argument(
        "-i",
        "--Iterations",
        type=int,
        help="How many iterations the algorithm should perform",
        required=True,
    )
    parser.add_argument(
        "-s", "--Size", type=int, help="Size of the tabu list", required=True
    )

    # Pass the arguments to main method
    main(parser.parse_args())
