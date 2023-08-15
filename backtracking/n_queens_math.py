r"""
Problem:

The n queens problem is: placing N queens on a N * N chess board such that no queen
can attack any other queens placed on that chess board.  This means that one queen
cannot have any other queen on its horizontal, vertical and diagonal lines.

Solution:

To solve this problem we will use simple math. First we know the queen can move in all
the possible ways, we can simplify it in this: vertical, horizontal, diagonal left and
 diagonal right.

We can visualize it like this:

left diagonal = \
right diagonal = /

On a chessboard vertical movement could be the rows and horizontal movement could be
the columns.

In programming we can use an array, and in this array each index could be the rows and
each value in the array could be the column. For example:

    . Q . .     We have this chessboard with one queen in each column and each queen
    . . . Q     can't attack to each other.
    Q . . .     The array for this example would look like this: [1, 3, 0, 2]
    . . Q .

So if we use an array and we verify that each value in the array is different to each
other we know that at least the queens can't attack each other in horizontal and
vertical.

At this point we have it halfway completed and we will treat the chessboard as a
Cartesian plane.  Hereinafter we are going to remember basic math, so in the school we
learned this formula:

    Slope of a line:

           y2 - y1
     m = ----------
          x2 - x1

This formula allow us to get the slope. For the angles 45º (right diagonal) and 135º
(left diagonal) this formula gives us m = 1, and m = -1 respectively.

See::
https://www.enotes.com/homework-help/write-equation-line-that-hits-origin-45-degree-1474860

Then we have this other formula:

Slope intercept:

y = mx + b

b is where the line crosses the Y axis (to get more information see:
https://www.mathsisfun.com/y_intercept.html), if we change the formula to solve for b
we would have:

y - mx = b

And since we already have the m values for the angles 45º and 135º, this formula would
look like this:

45º: y - (1)x = b
45º: y - x = b

135º: y - (-1)x = b
135º: y + x = b

y = row
x = column

Applying these two formulas we can check if a queen in some position is being attacked
for another one or vice versa.

"""
from __future__ import annotations


def depth_first_search(
    possible_board: list[int],
    diagonal_right_collisions: list[int],
    diagonal_left_collisions: list[int],
    boards: list[list[str]],
    n: int,
) -> None:
    """
    Recursively solves the N-Queens problem using depth-first search (DFS).

    Args:
        possible_board (list): List of integers representing the possible positions of the queens on the board.
        diagonal_right_collisions (list): List of integers representing the positions that cause a collision on the right diagonal.
        diagonal_left_collisions (list): List of integers representing the positions that cause a collision on the left diagonal.
        boards (list): List of boards to keep track of found solutions.
        n (int): The size of the board (n x n) and the number of queens to be placed on the board.

    Returns:
        None

    Examples:
        >>> boards = []
        >>> depth_first_search([], [], [], boards, 4)
        >>> for board in boards:
        ...     print(board)
        ['. Q . . ', '. . . Q ', 'Q . . . ', '. . Q . ']
        ['. . Q . ', 'Q . . . ', '. . . Q ', '. Q . . ']
    """
    row = len(possible_board)
    if row == n:
        add_solution(possible_board, boards, n)
        return

    for pos in range(n):
        if is_pos_valid(
            pos,
            possible_board,
            diagonal_right_collisions,
            diagonal_left_collisions,
            row,
        ):
            depth_first_search(
                [*possible_board, pos],
                [*diagonal_right_collisions, row - pos],
                [*diagonal_left_collisions, row + pos],
                boards,
                n,
            )


def n_queens_solution(n: int) -> None:
    boards: list[list[str]] = []
    depth_first_search([], [], [], boards, n)

    # Print all the boards
    for board in boards:
        for column in board:
            print(column)
        print("")

    print(len(boards), "solutions were found.")



def is_pos_valid(
    pos: int,
    possible_board: list[int],
    diag_right_collisions: list[int],
    diag_left_collisions: list[int],
    row: int,
) -> bool:
    """Check if the position is valid"""
    return (
        pos not in possible_board
        and row - pos not in diag_right_collisions
        and row + pos not in diag_left_collisions
    )


def add_solution(possible_board: list[int], boards: list[list[str]], n: int) -> None:
    """Adds the current board to the list of solutions"""
    boards.append([". " * i + "Q " + ". " * (n - 1 - i) for i in possible_board])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n_queens_solution(4)
