

from typing import List, Tuple, Set, Optional
# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


class Matrix:
    def __init__(self, row: int, col: int, graph: list[list[bool]]) -> None:
        self.ROW = row
        self.COL = col
        self.graph = graph

    def is_safe(
        self,
        matrix: List[List[int]],
        starting_point: Tuple[int, int],
        already_checked: Optional[Set[Tuple[int, int]]] = None,
    ) -> bool:
        """
        Determine if a given starting_point in a matrix is surrounded by '1's or not.
        """

        def get_neighbour_positions(position):
            neighbours = [
                (position[0] + i, position[1] + j)
                for i in range(-1, 2)
                for j in range(-1, 2)
                if (i, j) != (0, 0)
            ]
            return [
                (i, j)
                for i, j in neighbours
                if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])
            ]

        if already_checked is None:
            already_checked = set()

        x, y = starting_point
        if matrix[x][y] == 0:
            return False

        if starting_point in already_checked:
            return True

        already_checked.add(starting_point)
        neighbours = get_neighbour_positions(starting_point)

        for neighbour in neighbours:
            if not self.is_safe(matrix, neighbour, already_checked):
                return False

        return True

    def diffs(self, i: int, j: int, visited: list[list[bool]]) -> None:
        # Checking all 8 elements surrounding nth element
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]  # Coordinate order
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True  # Make those cells visited
        for k in range(8):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k], visited):
                self.diffs(i + row_nbr[k], j + col_nbr[k], visited)

    def count_islands(self) -> int:  # And finally, count all islands.
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.diffs(i, j, visited)
                    count += 1
        return count
