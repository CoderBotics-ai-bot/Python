from typing import List


from typing import List


def print_combination(arr, n, r):
    # A temporary array to store all combination one by one
    data = [0] * r
    # Print all combination using temporary array 'data[]'
    combination_util(arr, n, r, 0, data, 0)



def combination_util(
    arr: List[int], n: int, r: int, index: int, data: List[int], i: int
) -> None:
    """
    Generate all possible combinations of a given size from an input array.

    :param arr: The input array.
    :type arr: List[int]
    :param n: The size of the input array.
    :type n: int
    :param r: The desired combination size.
    :type r: int
    :param index: The current index in the temporary data array that stores the current combination.
    :type index: int
    :param data: The temporary array to store current combination.
    :type data: List[int]
    :param i: The current index in input array.
    :type i: int
    """
    if index == r:
        print(*data[:r])
        return

    if i >= n:
        return

    data[index] = arr[i]

    combination_util(arr, n, r, index + 1, data, i + 1)  # Include current element
    combination_util(arr, n, r, index, data, i + 1)  # Exclude current element


if __name__ == "__main__":
    # Driver code to check the function above
    arr = [10, 20, 30, 40, 50]
    print_combination(arr, len(arr), 3)
    # This code is contributed by Ambuj sahu
