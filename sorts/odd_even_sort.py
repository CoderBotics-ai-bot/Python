"""
Odd even sort implementation.

https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort
"""


from typing import List

def odd_even_sort(input_list: List[int]) -> List[int]:
    """
    Sort an input list using the odd-even sort algorithm.

    Args:
        input_list (List[int]): The list of integers that needs to be sorted.

    Returns:
        List[int]: The sorted list in ascending order.
    """

    def perform_swap(start_index: int) -> bool:
        """
        Perform swap operation on sequences of the input list starting from start_index

        Args:
            start_index (int): The starting index for the swap sequence.

        Returns:
            bool: Returns True if a swap operation was made, False otherwise.
        """
        is_sorted = True
        for i in range(start_index, len(input_list) - 1, 2):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                is_sorted = False
        return is_sorted

    is_sorted = False
    while not is_sorted:
        is_sorted_even = perform_swap(0)
        is_sorted_odd = perform_swap(1)
        is_sorted = is_sorted_even and is_sorted_odd
    return input_list


if __name__ == "__main__":
    print("Enter list to be sorted")
    input_list = [int(x) for x in input().split()]
    # inputing elements of the list in one line
    sorted_list = odd_even_sort(input_list)
    print("The sorted list is")
    print(sorted_list)
