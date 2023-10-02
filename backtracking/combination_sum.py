"""
In the Combination Sum problem, we are given a list consisting of distinct integers.
We need to find all the combinations whose sum equals to target given.
We can use an element more than one.

Time complexity(Average Case): O(n!)

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""


from typing import List


def backtrack(
    candidates: List[int],
    path: List[int],
    answer: List[List[int]],
    target: int,
    previous_index: int,
) -> None:
    """
    A recursive function that is responsible for searching for possible combinations.
    As a backtracking algorithm, if the current combination sum goes past the target value, the function will backtrack.

    Args:
    candidates (List[int]): A list of integers from which we can use to form different combinations.
    path (List[int]): The current combination's path being tracked.
    answer (List[List[int]]): A list where all possible combinations will be stored.
    target (int): The target integer value that we need to obtain by summing the integers in the `path` list.
    previous_index (int): The index of the previous integer that was used in forming the current combination.

    Returns:
    None. Note that the function returns None since the result is updated in the `answer` list which is a mutable type in Python.
    """
    if target == 0:
        answer.append(path.copy())
        return

    for index in range(previous_index, len(candidates)):
        check_candidate(candidates, path, answer, target, index)


def combination_sum(candidates: list, target: int) -> list:
    """
    >>> combination_sum([2, 3, 5], 8)
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    >>> combination_sum([2, 3, 6, 7], 7)
    [[2, 2, 3], [7]]
    >>> combination_sum([-8, 2.3, 0], 1)
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded in comparison
    """
    path = []  # type: list[int]
    answer = []  # type: list[int]
    backtrack(candidates, path, answer, target, 0)
    return answer

def check_candidate(
    candidates: List[int],
    path: List[int],
    answer: List[List[int]],
    target: int,
    index: int,
) -> None:
    """
    Check if a candidate from candidates list can be used to form a combination that sums to target.
    If so, continue the path with this candidate and backtrack for following candidates.

    Args:
    candidates (List[int]): A list of integers from which we can use to form different combinations.
    path (List[int]): The current combination's path being tracked.
    answer (List[List[int]]): A list where all possible combinations will be stored.
    target (int): The target integer value that we need to obtain by summing the integers in the `path` list.
    index (int): The index of the current integer that is being checked.

    Returns:
    None. Note that the function returns None as the result is updated in the `answer` list which is a mutable type in Python.
    """
    if target < candidates[index]:
        return
    path.append(candidates[index])
    backtrack(candidates, path, answer, target - candidates[index], index)
    path.pop()


def main() -> None:
    print(combination_sum([-8, 2.3, 0], 1))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
