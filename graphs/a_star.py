from __future__ import annotations
from typing import List


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
) -> tuple:
    closed, action, x, y = initialize_search(grid, init)
    g = 0
    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            raise ValueError("Path not found!")
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(DIRECTIONS)):
                    x2, y2 = get_next_position(x, y, DIRECTIONS[i])
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i

    path = reconstruct_path(action, init, goal)
    return path, action


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



def initialize_search(grid: List[List[int]], init: List[int]) -> tuple:
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1
    x = init[0]
    y = init[1]
    return closed, action, x, y


def get_next_position(x: int, y: int, direction: List[int]) -> tuple:
    x2 = x + direction[0]
    y2 = y + direction[1]
    return x2, y2


def reconstruct_path(
    action: List[List[int]], init: List[int], goal: List[int]
) -> List[List[int]]:
    x = goal[0]
    y = goal[1]
    path = [[-1 for col in range(len(action[0]))] for row in range(len(action))]
    path[x][y] = "*"
    while x != init[0] or y != init[1]:
        x2 = x - DIRECTIONS[action[x][y]][0]
        y2 = y - DIRECTIONS[action[x][y]][1]
        path[x2][y2] = DIRECTIONS.index([x - x2, y - y2])
        x = x2
        y = y2
    return path
