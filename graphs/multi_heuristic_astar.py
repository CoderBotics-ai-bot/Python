import heapq
import sys

import numpy as np


from typing import Dict, Tuple


from sys import exit as sys_exit
from numpy import chararray as np_chararray


from typing import Dict, List


from typing import List, Tuple

TPos = Tuple[int, int]

TPos = tuple[int, int]


class PriorityQueue:
    def __init__(self):
        self.elements = []
        self.set = set()

    def minkey(self):
        if not self.empty():
            return self.elements[0][0]
        else:
            return float("inf")

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        if item not in self.set:
            heapq.heappush(self.elements, (priority, item))
            self.set.add(item)
        else:
            # update
            # print("update", item)
            temp = []
            (pri, x) = heapq.heappop(self.elements)
            while x != item:
                temp.append((pri, x))
                (pri, x) = heapq.heappop(self.elements)
            temp.append((priority, item))
            for pro, xxx in temp:
                heapq.heappush(self.elements, (pro, xxx))

    def remove_element(self, item):
        if item in self.set:
            self.set.remove(item)
            temp = []
            (pro, x) = heapq.heappop(self.elements)
            while x != item:
                temp.append((pro, x))
                (pro, x) = heapq.heappop(self.elements)
            for prito, yyy in temp:
                heapq.heappush(self.elements, (prito, yyy))

    def top_show(self):
        return self.elements[0][1]

    def get(self):
        (priority, item) = heapq.heappop(self.elements)
        self.set.remove(item)
        return (priority, item)


def consistent_heuristic(p: TPos, goal: TPos):
    # euclidean distance
    a = np.array(p)
    b = np.array(goal)
    return np.linalg.norm(a - b)


def heuristic_2(p: TPos, goal: TPos):
    # integer division by time variable
    return consistent_heuristic(p, goal) // t


def heuristic_1(p: TPos, goal: TPos):
    # manhattan distance
    return abs(p[0] - goal[0]) + abs(p[1] - goal[1])


def key(start: TPos, i: int, goal: TPos, g_function: dict[TPos, float]):
    ans = g_function[start] + W1 * heuristics[i](start, goal)
    return ans


def make_common_ground() -> List[Tuple[int, int]]:
    """Create a common ground with obstacles.

    This function defines a ground where each cell represents a possible position of an agent.
    The board has dimensions 20x20 and obstacles are defined in specific cells.
    The positions of the obstacles are hardcoded according to the game logic.

    Returns:
        A list of tuples where each tuple is a pair of integers representing the
        coordinate (x, y) of a cell with an obstacle.
    """
    obstacle1 = make_obstacle(1, 5, 1, 6)
    obstacle2 = make_obstacle(15, 20, 17, 18)
    obstacle3 = make_obstacle(10, 19, 1, 15)
    obstacle4 = make_obstacle(1, 4, 12, 19)
    obstacle5 = make_obstacle(3, 13, 16, 19)

    return obstacle1 + obstacle2 + obstacle3 + obstacle4 + obstacle5

def valid(p: TPos) -> bool:
    """
    Check if the given position (p) is within the allowed limits.

    The allowed limits for the position's x and y coordinates are [0, n-1],
    where 'n' is a hyper-parameter defined in the outer scope.

    Args:
        p (TPos): The position to be checked, represented by a tuple of two integers (x, y).

    Returns:
        bool: Returns True if the position is valid, otherwise returns False.
    """
    x, y = p
    return all(0 <= coordinate < n for coordinate in (x, y))

def make_obstacle(
    start_x: int, end_x: int, start_y: int, end_y: int
) -> List[Tuple[int, int]]:
    """Create a list of coordinates of obstacles.

    This function generates a list where each item represents the coordinate (x, y)
    of an obstacle for a given range between start and end points on x and y axes.

    Args:
        start_x (int): start point on x axis
        end_x (int): end point on x axis
        start_y (int): start point on y axis
        end_y (int): end point on y axis

    Returns:
        A list of tuples where each tuple is a pair of integers representing the
        obstacle coordinate (x, y).
    """
    return [(x, y) for x in range(start_x, end_x) for y in range(start_y, end_y)]


def expand_state(
    s: TPos,
    j: int,
    visited: set,
    g_function: Dict[TPos, float],
    close_list_anchor: set,
    close_list_inad: set,
    open_list: List["PriorityQueue"],
) -> None:
    """Expand the state."""
    (x, y) = s
    neighbours_list = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]

    for itera in range(n_heuristic):
        open_list[itera].remove_element(s)

    for neighbour in neighbours_list:
        evaluate_neighbour(
            neighbour,
            s,
            open_list,
            visited,
            g_function,
            back_pointer,
            close_list_anchor,
            close_list_inad,
        )


def do_something(back_pointer: dict[TPos, TPos], goal: TPos, start: TPos) -> None:
    grid = create_initial_grid()
    visualize_grid(grid, back_pointer, goal, start)

    print("^")
    print("Start position")
    print()
    print("# is an obstacle")
    print("- is the path taken by algorithm")

    print_path_back_trace(back_pointer, goal, start)
    sys.exit()

def evaluate_neighbour(
    neighbour: TPos,
    current_state: TPos,
    open_list: List["PriorityQueue"],
    visited: set,
    g_function: Dict[TPos, float],
    back_pointer: Dict[TPos, TPos],
    close_list_anchor: set,
    close_list_inad: set,
) -> None:
    """Evaluate the neighbour node."""
    if valid(neighbour) and neighbour not in blocks:
        if neighbour not in visited:
            visited.add(neighbour)
            back_pointer[neighbour] = -1
            g_function[neighbour] = float("inf")

        if g_function[neighbour] > g_function[current_state] + 1:
            g_function[neighbour] = g_function[current_state] + 1
            back_pointer[neighbour] = current_state

            if neighbour not in close_list_anchor:
                open_list[0].put(neighbour, key(neighbour, 0, goal, g_function))
                if neighbour not in close_list_inad:
                    for var in range(1, n_heuristic):
                        if key(neighbour, var, goal, g_function) <= W2 * key(
                            neighbour, 0, goal, g_function
                        ):
                            open_list[var].put(
                                neighbour, key(neighbour, var, goal, g_function)
                            )

def visualize_grid(
    grid: np.array, back_pointer: Dict[TPos, TPos], goal: TPos, start: TPos
) -> None:
    """Visualizes the grid and prints it to the console."""

    grid[0][(n - 1)] = "-"
    x = back_pointer[goal]

    while x != start:
        (x_c, y_c) = x
        grid[(n - 1) - y_c][x_c] = "-"
        x = back_pointer[x]
    grid[(n - 1)][0] = "-"

    for i in range(n):
        print_end_position(grid, i)
        print()


def print_end_position(grid, i):
    """Prints the character representation of the position on the grid."""
    for j in range(n):
        if (i, j) == (0, n - 1):
            print(grid[i][j], end=" ")
            print("<-- End position", end=" ")
        else:
            print(grid[i][j], end=" ")


def print_path_back_trace(
    back_pointer: Dict[TPos, TPos], goal: TPos, start: TPos
) -> None:
    """Prints the path back trace and prints it the console."""
    print("PATH TAKEN BY THE ALGORITHM IS:-")
    x = back_pointer[goal]

    while x != start:
        print(x, end=" ")
        x = back_pointer[x]

    print(x)


def create_initial_grid() -> np.array:
    """Create the initial grid and mark the obstacles with '#'. Returns the grid."""
    grid = np.chararray((n, n))

    for i in range(n):
        for j in range(n):
            grid[(n - 1) - i][j] = "#" if (j, (n - 1) - i) in blocks else "*"
    return grid


heuristics = {0: consistent_heuristic, 1: heuristic_1, 2: heuristic_2}

blocks_blk = [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 1),
    (10, 1),
    (11, 1),
    (12, 1),
    (13, 1),
    (14, 1),
    (15, 1),
    (16, 1),
    (17, 1),
    (18, 1),
    (19, 1),
]
blocks_all = make_common_ground()


blocks = blocks_blk
# hyper parameters
W1 = 1
W2 = 1
n = 20
n_heuristic = 3  # one consistent and two other inconsistent

# start and end destination
start = (0, 0)
goal = (n - 1, n - 1)

t = 1


def multi_a_star(start: TPos, goal: TPos, n_heuristic: int):
    g_function = {start: 0, goal: float("inf")}
    back_pointer = {start: -1, goal: -1}
    open_list = []
    visited = set()

    for i in range(n_heuristic):
        open_list.append(PriorityQueue())
        open_list[i].put(start, key(start, i, goal, g_function))

    close_list_anchor: list[int] = []
    close_list_inad: list[int] = []
    while open_list[0].minkey() < float("inf"):
        for i in range(1, n_heuristic):
            # print(open_list[0].minkey(), open_list[i].minkey())
            if open_list[i].minkey() <= W2 * open_list[0].minkey():
                global t
                t += 1
                if g_function[goal] <= open_list[i].minkey():
                    if g_function[goal] < float("inf"):
                        do_something(back_pointer, goal, start)
                else:
                    _, get_s = open_list[i].top_show()
                    visited.add(get_s)
                    expand_state(
                        get_s,
                        i,
                        visited,
                        g_function,
                        close_list_anchor,
                        close_list_inad,
                        open_list,
                        back_pointer,
                    )
                    close_list_inad.append(get_s)
            else:
                if g_function[goal] <= open_list[0].minkey():
                    if g_function[goal] < float("inf"):
                        do_something(back_pointer, goal, start)
                else:
                    get_s = open_list[0].top_show()
                    visited.add(get_s)
                    expand_state(
                        get_s,
                        0,
                        visited,
                        g_function,
                        close_list_anchor,
                        close_list_inad,
                        open_list,
                        back_pointer,
                    )
                    close_list_anchor.append(get_s)
    print("No path found to goal")
    print()
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if (j, i) in blocks:
                print("#", end=" ")
            elif (j, i) in back_pointer:
                if (j, i) == (n - 1, n - 1):
                    print("*", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("*", end=" ")
            if (j, i) == (n - 1, n - 1):
                print("<-- End position", end=" ")
        print()
    print("^")
    print("Start position")
    print()
    print("# is an obstacle")
    print("- is the path taken by algorithm")


if __name__ == "__main__":
    multi_a_star(start, goal, n_heuristic)
