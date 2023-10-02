from __future__ import annotations


from typing import List, Tuple

DIRECTIONS = [
    [-1, 0],  # left
    [0, -1],  # down
    [1, 0],  # right
    [0, 1],  # up
]


def search(
    grid: List[List[int]],
    init: List[int],
    goal: List[int],
    cost: int,
    heuristic: List[List[int]],
) -> Tuple[List[List[int]], List[List[int]]]:
    closed, action = initialize_matrices(init, grid)
    g = 0
    f = g + heuristic[init[0]][init[1]]
    cell = [[f, g] + init]

    while True:
        if not cell:
            raise ValueError("Algorithm is unable to find solution")
        cell.sort()
        f, g, x, y = cell.pop()

        if [x, y] == goal:
            return backtrace(goal, init, action), action
        expand_cell(x, y, g, grid, heuristic, closed, cell, cost)


if __name__ == "__main__":
    grid = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],  # 0 are free path whereas 1's are obstacles
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
    ]

    init = [0, 0]
    # all coordinates are given in format [y,x]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1

    # the cost map which pushes the path closer to the goal
    heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            heuristic[i][j] = abs(i - goal[0]) + abs(j - goal[1])
            if grid[i][j] == 1:
                # added extra penalty in the heuristic map
                heuristic[i][j] = 99

    path, action = search(grid, init, goal, cost, heuristic)

    print("ACTION MAP")
    for i in range(len(action)):
        print(action[i])

    for i in range(len(path)):
        print(path[i])

def initialize_matrices(
    init: List[int], grid: List[List[int]]
) -> Tuple[List[List[int]], List[List[int]]]:
    """Initializes reference and action grids."""
    closed = [[0 for _ in grid[0]] for _ in grid]
    closed[init[0]][init[1]] = 1

    action = [[0 for _ in grid[0]] for _ in grid]

    return closed, action


def expand_cell(
    x: int,
    y: int,
    g: int,
    grid: List[List[int]],
    heuristic: List[List[int]],
    closed: List[List[int]],
    cell: List[List[int]],
    cost: int,
) -> None:
    """Expands the current cell to its valid neighbors."""
    for i in range(len(DIRECTIONS)):
        x2 = x + DIRECTIONS[i][0]
        y2 = y + DIRECTIONS[i][1]
        if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
            if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                g2 = g + cost
                f2 = g2 + heuristic[x2][y2]
                cell.append([f2, g2, x2, y2])
                closed[x2][y2] = 1


def backtrace(
    goal: List[int], init: List[int], action: List[List[int]]
) -> List[List[int]]:
    """Retrieves the path from the initial position to the goal."""
    x, y = goal
    path = [[x, y]]
    while [x, y] != init:
        i = action[x][y]
        x, y = x - DIRECTIONS[i][0], y - DIRECTIONS[i][1]
        path.append([x, y])

    return path[::-1]
