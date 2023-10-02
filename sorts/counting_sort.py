"""
This is pure Python implementation of counting sort algorithm
For doctests run following command:
python -m doctest -v counting_sort.py
or
python3 -m doctest -v counting_sort.py
For manual testing run:
python counting_sort.py
"""


from typing import List

def counting_sort(collection: List[int]) -> List[int]:
    """
    This function sorts a mutable collection of integers in ascending order using the counting sort algorithm.
    """
    if not collection:
        return []

    # get collection stats and initialize the counting array
    coll_min, coll_max, counting_arr = initialize(collection)

    # perform counting of elements in the collection
    counting_arr = perform_counting(collection, counting_arr, coll_min)

    # perform cumulative sum in the counting array
    counting_arr = cumulative_sum(counting_arr)

    # create the ordered collection
    ordered_collection = create_ordered_collection(collection, counting_arr, coll_min)

    return ordered_collection


def counting_sort_string(string):
    """
    >>> counting_sort_string("thisisthestring")
    'eghhiiinrsssttt'
    """
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])


def initialize(collection: List[int]) -> List[int]:
    """
    This function initializes and returns the collection stats and the counting array.
    """
    coll_min = min(collection)
    coll_max = max(collection)
    counting_arr = [0] * (coll_max + 1 - coll_min)

    return coll_min, coll_max, counting_arr


def perform_counting(
    collection: List[int], counting_arr: List[int], coll_min: int
) -> List[int]:
    """
    This function counts how much a number appears in the collection.
    """
    for number in collection:
        counting_arr[number - coll_min] += 1

    return counting_arr


def cumulative_sum(counting_arr: List[int]) -> List[int]:
    """
    This function performs the cumulative sum in the counting array.
    """
    for i in range(1, len(counting_arr)):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    return counting_arr


def create_ordered_collection(
    collection: List[int], counting_arr: List[int], coll_min: int
) -> List[int]:
    """
    This function creates and returns the ordered collection.
    """
    coll_len = len(collection)
    ordered = [0] * coll_len

    for i in reversed(range(coll_len)):
        ordered[counting_arr[collection[i] - coll_min] - 1] = collection[i]
        counting_arr[collection[i] - coll_min] -= 1

    return ordered


if __name__ == "__main__":
    # Test string sort
    assert counting_sort_string("thisisthestring") == "eghhiiinrsssttt"

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(counting_sort(unsorted))
