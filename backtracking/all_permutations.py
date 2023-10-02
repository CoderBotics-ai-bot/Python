"""
        In this problem, we want to determine all possible permutations
        of the given sequence. We use backtracking to solve this problem.

        Time complexity: O(n! * n),
        where n denotes the length of the given sequence.
"""
from __future__ import annotations
from typing import List


def generate_all_permutations(sequence: list[int | str]) -> None:
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])

def create_state_space_tree(
    sequence: List[int | str],
    current_sequence: List[int | str] = [],
    index: int = 0,
    index_used: List[bool] = None,
) -> None:
    if index_used is None:
        index_used = [False] * len(sequence)

    if index == len(sequence):
        print(current_sequence)
        return

    for i, is_used in enumerate(index_used):
        if not is_used:
            index_used[i] = True
            current_sequence.append(sequence[i])

            create_state_space_tree(sequence, current_sequence, index + 1, index_used)

            current_sequence.pop()
            index_used[i] = False


"""
remove the comment to take an input from the user

print("Enter the elements")
sequence = list(map(int, input().split()))
"""

sequence: list[int | str] = [3, 1, 2, 4]
generate_all_permutations(sequence)

sequence_2: list[int | str] = ["A", "B", "C"]
generate_all_permutations(sequence_2)
