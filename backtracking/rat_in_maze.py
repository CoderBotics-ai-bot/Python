from __future__ import annotations


from typing import List

def solve_maze(maze: list[list[int]]) -> bool:
    """Finds path from start to end in the maze."""
    size = len(maze)
    solutions = [[0] * size for _ in range(size)]
    if not run_maze(maze, 0, 0, solutions):
        print("No solution exists!")
        return False
    print_solutions(solutions)
    return True


def run_maze(maze: List[List[int]], i: int, j: int, solutions: List[List[int]]) -> bool:
    size = len(maze)

    # Final check point.
    if i == j == (size - 1):
        solutions[i][j] = 1
        return True

    if bounds_check(i, j, size) and block_check(i, j, maze, solutions):
        solutions[i][j] = 1

        # Define directions: Down, Right, Up, Left
        directions = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]

        # check for directions
        for direction_i, direction_j in directions:
            if run_maze(maze, direction_i, direction_j, solutions):
                return True

        solutions[i][j] = 0

    return False


def print_solutions(solutions: list[list[int]]) -> None:
    """Displays solutions in readable format."""
    print("\n".join(str(row) for row in solutions))

def bounds_check(i: int, j: int, size: int) -> bool:
    """
    Function to check if the coordinates (i, j) are within the bounds of the maze.

    Parameters:
    i (int): The row index.
    j (int): The column index.
    size (int): Size of the maze.

    Returns:
    bool: True if the coordinates are within the bounds, otherwise False.
    """
    return (0 <= i < size) and (0 <= j < size)


def block_check(
    i: int, j: int, maze: List[List[int]], solutions: List[List[int]]
) -> bool:
    """
    Function to check if a cell in the maze is a block or already visited.

    Parameters:
    i (int): The row index.
    j (int): The column index.
    maze (List[List[int]]): Maze in the form of a 2D list.
    solutions (List[List[int]]): Solutions in the form of a 2D list.

    Returns:
    bool: True if the cell is not a block and not visited, otherwise False.
    """
    return (0 == maze[i][j]) and (0 == solutions[i][j])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
