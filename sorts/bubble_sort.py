from typing import Any
from typing import Any, List


from typing import Any, List


def bubble_sort(collection: List[Any]) -> List[Any]:
    """
    Pure implementation of bubble sort algorithm in Python.
    This function takes a list as input and returns the sorted list.
    The bubble sort algorithm works by comparing each item in the list with the item next to it,
    and swapping them if required.
    The algorithm repeats this process until it makes a pass through the list without
    swapping any items.

    Args:
        collection: A mutable ordered collection of heterogeneous comparable items.

    Returns:
        A sorted list in ascending order.
    """
    length = len(collection)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            swapped = True
            swap_elements(collection, j)
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


if __name__ == "__main__":
    import doctest
    import time

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubble_sort(unsorted), sep=",")
    print(f"Processing time: {(time.process_time() - start)%1e9 + 7}")



def swap_elements(collection: List[Any], index: int) -> None:
    """Swap two contiguous elements if they are out of order."""
    if collection[index] > collection[index + 1]:
        collection[index], collection[index + 1] = (
            collection[index + 1],
            collection[index],
        )
