"""
        The sum-of-subsetsproblem states that a set of non-negative integers, and a
        value M, determine all possible subsets of the given set whose summation sum
        equal to given M.

        Summation of the chosen numbers must be equal to given number M and one number
        can be used only once.
"""
from __future__ import annotations


from typing import List, Optional


def generate_sum_of_subsets_soln(nums: list[int], max_sum: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []
    num_index = 0
    remaining_nums_sum = sum(nums)
    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum)
    return result

def create_state_space_tree(
    nums: list[int],
    max_sum: int,
    num_index: int,
    path: list[int],
    result: list[list[int]],
    remaining_nums_sum: int,
) -> None:
    current_sum = sum(path)
    if current_sum > max_sum or (remaining_nums_sum + current_sum) < max_sum:
        return

    if current_sum == max_sum:
        result.append(path)
        return

    for index in range(num_index, len(nums)):
        next_path = [*path, nums[index]]
        next_remaining_sum = remaining_nums_sum - nums[index]
        create_state_space_tree(
            nums, max_sum, index + 1, next_path, result, next_remaining_sum
        )


"""
remove the comment to take an input from the user

print("Enter the elements")
nums = list(map(int, input().split()))
print("Enter max_sum sum")
max_sum = int(input())

"""
nums = [3, 34, 4, 12, 5, 2]
max_sum = 9
result = generate_sum_of_subsets_soln(nums, max_sum)
print(*result)
