from typing import List
def quick_sort_3partition(sorting: list, left: int, right: int) -> None:
    """Sorts 'sorting' list using a three-way (Dutch National Flag) QuickSort method."""

    if right <= left:
        return

    a, z = rearrange_elements(sorting, left, right)

    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, z + 1, right)


def quick_sort_lomuto_partition(sorting: list, left: int, right: int) -> None:
    """
    A pure Python implementation of quick sort algorithm(in-place)
    with Lomuto partition scheme:
    https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme

    :param sorting: sort list
    :param left: left endpoint of sorting
    :param right: right endpoint of sorting
    :return: None

    Examples:
    >>> nums1 = [0, 5, 3, 1, 2]
    >>> quick_sort_lomuto_partition(nums1, 0, 4)
    >>> nums1
    [0, 1, 2, 3, 5]
    >>> nums2 = []
    >>> quick_sort_lomuto_partition(nums2, 0, 0)
    >>> nums2
    []
    >>> nums3 = [-2, 5, 0, -4]
    >>> quick_sort_lomuto_partition(nums3, 0, 3)
    >>> nums3
    [-4, -2, 0, 5]
    """
    if left < right:
        pivot_index = lomuto_partition(sorting, left, right)
        quick_sort_lomuto_partition(sorting, left, pivot_index - 1)
        quick_sort_lomuto_partition(sorting, pivot_index + 1, right)


def rearrange_elements(sorting: list, left: int, right: int) -> tuple:
    """
    Rearrange elements in 'sorting' list with standart QuickSort
    method using pivot.
    """

    a = i = left
    b = right
    pivot = sorting[left]

    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = sorting[i], sorting[a]
            a, i = increment_indices(a, i)
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = sorting[i], sorting[b]
            b -= 1
        else:
            i += 1

    return a, b


def increment_indices(a: int, i: int) -> tuple:
    """Increment 'a' and 'i' indices by one."""
    return a + 1, i + 1


def three_way_radix_quicksort(nums: List[int]) -> List[int]:
    """
    Perform three-way radix quicksort.

    This method divides the list into three parts (less than, equal to, and greater than the pivot),
    then recursively sorts the "less than" and "greater than" parts.

    Arguments:
    nums -- list of integers to sort

    Returns:
    Sorted list of integers.
    """
    if len(nums) <= 1:
        return nums

    less, equal, greater = partition(nums)

    return three_way_radix_quicksort(less) + equal + three_way_radix_quicksort(greater)


def lomuto_partition(sorting: list, left: int, right: int) -> int:
    """
    Example:
    >>> lomuto_partition([1,5,7,6], 0, 3)
    2
    """
    pivot = sorting[right]
    store_index = left
    for i in range(left, right):
        if sorting[i] < pivot:
            sorting[store_index], sorting[i] = sorting[i], sorting[store_index]
            store_index += 1
    sorting[right], sorting[store_index] = sorting[store_index], sorting[right]
    return store_index

def partition(nums: List[int]) -> List[List[int]]:
    """
    Partition the list into three parts.

    The first part contains elements less than the pivot.
    The second part contains elements equal to the pivot.
    The third part contains elements greater than the pivot.

    Arguments:
    nums -- list of integers to partition

    Returns:
    A list of three lists: less, equal, and greater parts.
    """
    pivot = nums[0]
    less, equal, greater = [], [], []

    for num in nums:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)

    return [less, equal, greater]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    quick_sort_3partition(unsorted, 0, len(unsorted) - 1)
    print(unsorted)
