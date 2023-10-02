"""
A pure implementation of Dutch national flag (DNF) sort algorithm in Python.
Dutch National Flag algorithm is an algorithm originally designed by Edsger Dijkstra.
It is the most optimal sort for 3 unique values (eg. 0, 1, 2) in a sequence.  DNF can
sort a sequence of n size with [0 <= a[i] <= 2] at guaranteed O(n) complexity in a
single pass.

The flag of the Netherlands consists of three colors: white, red, and blue.
The task is to randomly arrange balls of white, red, and blue in such a way that balls
of the same color are placed together.  DNF sorts a sequence of 0, 1, and 2's in linear
time that does not consume any extra space.  This algorithm can be implemented only on
a sequence that contains three unique elements.

1) Time complexity is O(n).
2) Space complexity is O(1).

More info on: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

For doctests run following command:
python3 -m doctest -v dutch_national_flag_sort.py

For manual testing run:
python dnf_sort.py
"""
from typing import List, Tuple


# Python program to sort a sequence containing only 0, 1 and 2 in a single pass.
red = 0  # The first color of the flag.
white = 1  # The second color of the flag.
blue = 2  # The third color of the flag.
colors = (red, white, blue)


def dutch_national_flag_sort(sequence: List[int]) -> List[int]:
    """
    Implementation of Dutch National Flag sort algorithm: Sorts sequence containing ONLY 0, 1, 2 in a single pass.

    Args:
        sequence (List[int]): Input sequence of integers containing ONLY 0, 1, and 2.

    Returns:
        List[int]: Sorted sequence in ascending order.

    Raises:
        ValueError: If elements are not 0, 1, or 2.
    """
    if not sequence:
        return []
    if len(sequence) == 1:
        return list(sequence)

    low, mid, high = 0, 0, len(sequence) - 1
    while mid <= high:
        validate_sequence(sequence[mid], colors)
        if sequence[mid] == colors[0]:
            swap(sequence, low, mid)
            low, mid = increment_low_and_mid(low, mid)
        elif sequence[mid] == colors[1]:
            mid += 1
        elif sequence[mid] == colors[2]:
            swap(sequence, mid, high)
            high = decrement_high(high)
    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    unsorted = [int(item.strip()) for item in user_input.split(",")]
    print(f"{dutch_national_flag_sort(unsorted)}")

def swap(sequence: List[int], i: int, j: int) -> None:
    sequence[i], sequence[j] = sequence[j], sequence[i]


def increment_low_and_mid(low: int, mid: int) -> Tuple[int, int]:
    return low + 1, mid + 1


def decrement_high(high: int) -> int:
    return high - 1


def validate_sequence(sequence_value: int, valid_values: Tuple[int, int, int]) -> None:
    if sequence_value not in valid_values:
        raise ValueError(
            f"The elements inside the sequence must contains only {valid_values} values"
        )
