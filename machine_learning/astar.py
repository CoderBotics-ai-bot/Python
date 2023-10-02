"""
The A* algorithm combines features of uniform-cost search and pure heuristic search to
efficiently compute optimal solutions.

The A* algorithm is a best-first search algorithm in which the cost associated with a
node is f(n) = g(n) + h(n), where g(n) is the cost of the path from the initial state to
node n and h(n) is the heuristic estimate or the cost or a path from node n to a goal.

The A* algorithm introduces a heuristic into a regular graph-searching algorithm,
essentially planning ahead at each step so a more optimal decision is made. For this
reason, A* is known as an algorithm with brains.

https://en.wikipedia.org/wiki/A*_search_algorithm
"""
import numpy as np


from typing import List


class Cell:
    """
    Class cell represents a cell in the world which have the properties:
    position: represented by tuple of x and y coordinates initially set to (0,0).
    parent: Contains the parent cell object visited before we arrived at this cell.
    g, h, f: Parameters used when calling our heuristic function.
    """

    def __init__(self):
        self.position = (0, 0)
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    """
    Overrides equals method because otherwise cell assign will give
    wrong results.
    """

    def __eq__(self, cell):
        return self.position == cell.position

    def showcell(self):
        print(self.position)


class Gridworld:
    """
    Gridworld class represents the  external world here a grid M*M
    matrix.
    world_size: create a numpy array with the given world_size default is 5.
    """

    def __init__(self, world_size=(5, 5)):
        self.w = np.zeros(world_size)
        self.world_x_limit = world_size[0]
        self.world_y_limit = world_size[1]

    def show(self):
        print(self.w)

    def get_neigbours(self, cell):
        """
        Return the neighbours of cell
        """
        neughbour_cord = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        current_x = cell.position[0]
        current_y = cell.position[1]
        neighbours = []
        for n in neughbour_cord:
            x = current_x + n[0]
            y = current_y + n[1]
            if 0 <= x < self.world_x_limit and 0 <= y < self.world_y_limit:
                c = Cell()
                c.position = (x, y)
                c.parent = cell
                neighbours.append(c)
        return neighbours


if __name__ == "__main__":
    world = Gridworld()
    # Start position and goal
    start = Cell()
    start.position = (0, 0)
    goal = Cell()
    goal.position = (4, 4)
    print(f"path from {start.position} to {goal.position}")
    s = astar(world, start, goal)
    #   Just for visual reasons.
    for i in s:
        world.w[i] = 1
    print(world.w)

def astar(world: "Gridworld", start: "Cell", goal: "Cell") -> List[tuple]:
    """Implementation of the A* Pathfinding Algorithm."""

    open_list = [start]
    closed_list = []

    while open_list:
        current = min(
            open_list, key=lambda o: o.f
        )  # Get the node in open list with the lowest f score
        open_list.remove(current)
        closed_list.append(current)

        if current == goal:
            return construct_path(current)

        process_neighbours(world, open_list, closed_list, current, goal)


def calculate_fgh(current: "Cell", neighbour: "Cell", goal: "Cell"):
    """Calculate f, g, and h values for a cell."""

    neighbour.g = current.g + 1
    x1, y1 = neighbour.position
    x2, y2 = goal.position
    neighbour.h = (y2 - y1) ** 2 + (x2 - x1) ** 2
    neighbour.f = neighbour.h + neighbour.g


def process_neighbours(
    world: "Gridworld",
    open_list: List["Cell"],
    closed_list: List["Cell"],
    current: "Cell",
    goal: "Cell",
):
    """Scan and process all neighbours of the current cell."""

    for neighbour in world.get_neigbours(current):
        if neighbour in closed_list or (
            neighbour in open_list and neighbour.f < current.f
        ):
            continue

        calculate_fgh(current, neighbour, goal)
        open_list.append(neighbour)


def construct_path(current: "Cell") -> List[tuple]:
    """Traverse the path from the goal to the start and return the path."""

    path = []
    while current.parent is not None:
        path.append(current.position)
        current = current.parent
    path.append(current.position)
    return path[::-1]
