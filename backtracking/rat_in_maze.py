from __future__ import annotations

def solve_maze(maze: list[list[int]]) -> bool:
    """Finds path from start to end in the maze."""
    size = len(maze)
    solutions = [[0] * size for _ in range(size)]
    if not run_maze(maze, 0, 0, solutions):
        print("No solution exists!")
        return False
    print_solutions(solutions)
    return True


def run_maze(maze: list[list[int]], i: int, j: int, solutions: list[list[int]]) -> bool:
    """
    This method is recursive starting from (i, j) and going in one of four directions:
    up, down, left, right.
    If a path is found to destination it returns True otherwise it returns False.
    Parameters:
        maze(2D matrix) : maze
        i, j : coordinates of matrix
        solutions(2D matrix) : solutions
    Returns:
        Boolean if path is found True, Otherwise False.
    """
    size = len(maze)
    # Final check point.
    if i == j == (size - 1):
        solutions[i][j] = 1
        return True

    lower_flag = (not i < 0) and (not j < 0)  # Check lower bounds
    upper_flag = (i < size) and (j < size)  # Check upper bounds

    if lower_flag and upper_flag:
        # check for already visited and block points.
        block_flag = (not solutions[i][j]) and (not maze[i][j])
        if block_flag:
            # check visited
            solutions[i][j] = 1

            # check for directions
            if (
                run_maze(maze, i + 1, j, solutions)
                or run_maze(maze, i, j + 1, solutions)
                or run_maze(maze, i - 1, j, solutions)
                or run_maze(maze, i, j - 1, solutions)
            ):
                return True

            solutions[i][j] = 0
            return False
    return False


def print_solutions(solutions: list[list[int]]) -> None:
    """Displays solutions in readable format."""
    print("\n".join(str(row) for row in solutions))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
