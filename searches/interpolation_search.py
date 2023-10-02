"""
This is pure Python implementation of interpolation search algorithm
"""


from typing import List, Union


from typing import List, Union, Tuple


def interpolation_search(sorted_collection: List[int], item: int) -> Union[int, None]:
    """
    Implementation of the interpolation search algorithm in Python.
    """
    left = 0
    right = len(sorted_collection) - 1

    while left <= right:
        if sorted_collection[left] == sorted_collection[right]:
            if sorted_collection[left] == item:
                return left
            else:
                return None

        point = calculate_midpoint(sorted_collection, item, left, right)

        if point < 0 or point >= len(sorted_collection):
            return None

        if is_item_found(sorted_collection, point, item):
            return point

        left, right = update_boundaries(sorted_collection, item, left, right, point)

    return None


def interpolation_search_by_recursion(sorted_collection, item, left, right):
    """Pure implementation of interpolation search algorithm in Python by recursion
    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    First recursion should be started with left=0 and right=(len(sorted_collection)-1)
    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    """

    # avoid divided by 0 during interpolation
    if sorted_collection[left] == sorted_collection[right]:
        if sorted_collection[left] == item:
            return left
        else:
            return None

    point = left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )

    # out of range check
    if point < 0 or point >= len(sorted_collection):
        return None

    if sorted_collection[point] == item:
        return point
    elif point < left:
        return interpolation_search_by_recursion(sorted_collection, item, point, left)
    elif point > right:
        return interpolation_search_by_recursion(sorted_collection, item, right, left)
    else:
        if sorted_collection[point] > item:
            return interpolation_search_by_recursion(
                sorted_collection, item, left, point - 1
            )
        else:
            return interpolation_search_by_recursion(
                sorted_collection, item, point + 1, right
            )

def calculate_midpoint(
    sorted_collection: List[int], item: int, left: int, right: int
) -> int:
    """
    Calculate the median of the list.
    """
    return left + ((item - sorted_collection[left]) * (right - left)) // (
        sorted_collection[right] - sorted_collection[left]
    )


def is_item_found(sorted_collection: List[int], point: int, item: int) -> bool:
    """
    Check the item found at the midpoint.
    """
    return sorted_collection[point] == item


def update_boundaries(
    sorted_collection: List[int], item: int, left: int, right: int, point: int
) -> Tuple[int, int]:
    """
    Update the boundaries of the list based on midpoint.
    """
    if item < sorted_collection[point]:
        right = point - 1
    else:
        left = point + 1
    return left, right


def __assert_sorted(collection):
    """Check if collection is ascending sorted, if not - raises :py:class:`ValueError`
    :param collection: collection
    :return: True if collection is ascending sorted
    :raise: :py:class:`ValueError` if collection is not ascending sorted
    Examples:
    >>> __assert_sorted([0, 1, 2, 4])
    True
    >>> __assert_sorted([10, -1, 5])
    Traceback (most recent call last):
        ...
    ValueError: Collection must be ascending sorted
    """
    if collection != sorted(collection):
        raise ValueError("Collection must be ascending sorted")
    return True


if __name__ == "__main__":
    import sys

    """
        user_input = input('Enter numbers separated by comma:\n').strip()
    collection = [int(item) for item in user_input.split(',')]
    try:
        __assert_sorted(collection)
    except ValueError:
        sys.exit('Sequence must be ascending sorted to apply interpolation search')

    target_input = input('Enter a single number to be found in the list:\n')
    target = int(target_input)
        """

    debug = 0
    if debug == 1:
        collection = [10, 30, 40, 45, 50, 66, 77, 93]
        try:
            __assert_sorted(collection)
        except ValueError:
            sys.exit("Sequence must be ascending sorted to apply interpolation search")
        target = 67

    result = interpolation_search(collection, target)
    if result is not None:
        print(f"{target} found at positions: {result}")
    else:
        print("Not found")
