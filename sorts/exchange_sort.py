

from typing import List, TypeVar

Comparable = TypeVar("Comparable")

def exchange_sort(numbers: List[Comparable]) -> List[Comparable]:
    """
    Sort a list of comparable elements using exchange sort algorithm.
    """

    def swap(i: int, j: int) -> None:
        """
        Swap elements at index i and j.
        """
        numbers[i], numbers[j] = numbers[j], numbers[i]

    numbers_length = len(numbers)
    for i in range(numbers_length):
        for j in range(i + 1, numbers_length):
            if numbers[j] < numbers[i]:
                swap(i, j)
    return numbers


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(exchange_sort(unsorted))
