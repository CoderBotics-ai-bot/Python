"""
https://en.wikipedia.org/wiki/Shellsort#Pseudocode
"""


from typing import List

def shell_sort(collection: List[int]) -> List[int]:
    """
    Pure implementation of the Shell sort algorithm in Python.
    Args:
        collection: Some mutable ordered collection with heterogeneous comparable items inside
    Returns:
        A new sorted list from the elements of the input collection
    """

    def sort_on_gap(collection: List[int], gap: int) -> List[int]:
        """
        Sorts the collection based on a given gap
        Args:
            collection: The collection to sort
            gap: The gap to sort with
        Returns:
            The sorted collection based on the given gap
        """
        for i in range(gap, len(collection)):
            selected = collection[i]
            j = i
            while j >= gap and collection[j - gap] > selected:
                collection[j] = collection[j - gap]
                j -= gap
            if j != i:
                collection[j] = selected

        return collection

    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        collection = sort_on_gap(collection, gap)

    return collection


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(shell_sort(unsorted))
