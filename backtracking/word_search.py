"""
Author  : Alexander Pantyukhin
Date    : November 24, 2022

Task:
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

Matrix:
---------
|A|B|C|E|
|S|F|C|S|
|A|D|E|E|
---------

Word:
"ABCCED"

Result:
True

Implementation notes: Use backtracking approach.
At each point, check all neighbors to try to find the next letter of the word.

leetcode: https://leetcode.com/problems/word-search/

"""


from typing import List, Set


def get_point_key(len_board: int, len_board_column: int, row: int, column: int) -> int:
    """
    Returns the hash key of matrix indexes.

    >>> get_point_key(10, 20, 1, 0)
    200
    """

    return len_board * len_board_column * row + column


def word_exists(board: list[list[str]], word: str) -> bool:
    """
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    True
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    False
    >>> word_exists([["A"]], "A")
    True
    >>> word_exists([["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","A"],
    ...              ["A","A","A","A","A","B"],
    ...              ["A","A","A","A","B","A"]],
    ...             "AAAAAAAAAAAAABB")
    False
    >>> word_exists([["A"]], 123)
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> word_exists([["A"]], "")
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> word_exists([[]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    >>> word_exists([], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    >>> word_exists([["A"], [21]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    """

    # Validate board
    board_error_message = (
        "The board should be a non empty matrix of single chars strings."
    )

    len_board = len(board)
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError(board_error_message)

    for row in board:
        if not isinstance(row, list) or len(row) == 0:
            raise ValueError(board_error_message)

        for item in row:
            if not isinstance(item, str) or len(item) != 1:
                raise ValueError(board_error_message)

    # Validate word
    if not isinstance(word, str) or len(word) == 0:
        raise ValueError(
            "The word parameter should be a string of length greater than 0."
        )

    len_board_column = len(board[0])
    for i in range(len_board):
        for j in range(len_board_column):
            if exits_word(
                board, word, i, j, 0, {get_point_key(len_board, len_board_column, i, j)}
            ):
                return True

    return False

def exits_word(
    board: List[List[str]],
    word: str,
    row: int,
    column: int,
    word_index: int,
    visited_points_set: set[int],
) -> bool:
    """
    Return True if it's possible to search the word suffix
    starting from the word_index.

    :param board: 2D grid of characters
    :param word: The word to be checked
    :param row: The row index from where to start the search
    :param column: The column index from where to start the search
    :param word_index: The current index of the word to be checked
    :param visited_points_set: a set of visited points
    :return: True if the word can be found, False otherwise
    """

    # Check if current cell matches word character
    if board[row][column] != word[word_index]:
        return False

    # If the current character is the last one in the word
    if word_index == len(word) - 1:
        return True

    key = get_point_key(len(board), len(board[0]), row, column)
    if key in visited_points_set:
        return False

    visited_points_set.add(key)
    for direction in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        next_row, next_col = row + direction[0], column + direction[1]
        if not (0 <= next_row < len(board) and 0 <= next_col < len(board[0])):
            continue

        if exits_word(
            board, word, next_row, next_col, word_index + 1, visited_points_set
        ):
            return True

    visited_points_set.remove(key)
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
