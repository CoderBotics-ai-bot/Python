
def bubble_sort(list_data: list) -> list:
    """
    Sort a list of elements in ascending order using bubble sort algorithm.

    Args:
    list_data : A mutable ordered sequence of elements (List).

    Returns:
    list: The sorted list.

    Example usage:

    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]

    >>> bubble_sort([])
    []

    >>> bubble_sort([-2, -45, -5])
    [-45, -5, -2]

    >>> bubble_sort(['z','a','y','b','x','c'])
    ['a', 'b', 'c', 'x', 'y', 'z']

    >>> bubble_sort([1.1, 3.3, 5.5, 7.7, 2.2, 4.4, 6.6])
    [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
    """
    has_swapped = True

    while has_swapped:
        has_swapped = False
        for i in range(len(list_data) - 1):
            if list_data[i] > list_data[i + 1]:
                list_data[i], list_data[i + 1] = list_data[i + 1], list_data[i]
                has_swapped = True

    return list_data


if __name__ == "__main__":
    import doctest

    doctest.testmod()
