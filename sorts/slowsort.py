"""
Slowsort is a sorting algorithm. It is of humorous nature and not useful.
It's based on the principle of multiply and surrender,
a tongue-in-cheek joke of divide and conquer.
It was published in 1986 by Andrei Broder and Jorge Stolfi
in their paper Pessimal Algorithms and Simplexity Analysis
(a parody of optimal algorithms and complexity analysis).

Source: https://en.wikipedia.org/wiki/Slowsort
"""
from __future__ import annotations

def slowsort(sequence: list, start: int | None = None, end: int | None = None) -> None:
    start, end = set_start_end(start, end, sequence)

    if start >= end:
        return

    mid = (start + end) // 2

    slowsort(sequence, start, mid)
    slowsort(sequence, mid + 1, end)
    swap_elements(sequence, end, mid)
    slowsort(sequence, start, end - 1)


if __name__ == "__main__":
    from doctest import testmod

    testmod()


def set_start_end(
    start: int | None, end: int | None, sequence: list
) -> tuple[int, int]:
    """Sets default values for start and end parameters if they are None.
    Otherwise, it returns the values passed in."""
    if start is None:
        start = 0
    if end is None:
        end = len(sequence) - 1

    return start, end


def swap_elements(sequence: list, index1: int, index2: int) -> None:
    """Swap the elements at the given indices in the sequence."""
    if sequence[index1] < sequence[index2]:
        sequence[index1], sequence[index2] = sequence[index2], sequence[index1]
