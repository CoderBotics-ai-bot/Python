""" https://en.wikipedia.org/wiki/Cocktail_shaker_sort """

def cocktail_shaker_sort(unsorted: list) -> list:
    """
    Pure implementation of the cocktail shaker sort algorithm in Python.
    This function makes use of two helper functions, `forward_pass` and `backward_pass`
    which iterate through the list in forward and reverse order respectively,
    swapping pair of integers that are out of order.

    :param unsorted: List of integers to be sorted
    :return: Sorted list of integers

    >>> cocktail_shaker_sort([4, 5, 2, 1, 2])
    [1, 2, 2, 4, 5]
    >>> cocktail_shaker_sort([-4, 5, 0, 1, 2, 11])
    [-4, 0, 1, 2, 5, 11]
    >>> cocktail_shaker_sort([0.1, -2.4, 4.4, 2.2])
    [-2.4, 0.1, 2.2, 4.4]
    >>> cocktail_shaker_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> cocktail_shaker_sort([-4, -5, -24, -7, -11])
    [-24, -11, -7, -5, -4]
    """

    def forward_pass(data: list, start: int, end: int) -> bool:
        swapped = False
        for i in range(start, end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        return swapped

    def backward_pass(data: list, start: int, end: int) -> bool:
        swapped = False
        for i in range(end, start, -1):
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
                swapped = True
        return swapped

    n = len(unsorted)
    for i in range(n - 1, 0, -1):
        if not backward_pass(unsorted, 0, i):
            break
        if not forward_pass(unsorted, 0, i):
            break
    return unsorted


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(f"{cocktail_shaker_sort(unsorted) = }")
