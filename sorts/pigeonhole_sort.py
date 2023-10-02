from typing import List


def pigeonhole_sort(array: List[int]) -> None:
    """
    Performs in-place pigeonhole sorting on a list of integers.

    Arguments:
    array -- list of integers to be sorted

    Raises TypeError:
    If array contains non-integer values.
    """

    validate_integer_elements(array)

    min_val = min(array)
    max_val = max(array)

    size = max_val - min_val + 1  # size is difference of max and min values plus one

    holes = [0] * size  # list of pigeonholes of size equal to the variable size

    populate_pigeonholes(array, holes, min_val)

    reconstruct_sorted_array(array, holes, min_val)


def main():
    a = [8, 3, 2, 7, 4, 6, 8]
    pigeonhole_sort(a)
    print("Sorted order is:", " ".join(a))

def validate_integer_elements(array: List[int]) -> None:
    """
    Validates that every element in the array is an integer.

    Arguments:
    array -- list of elements to be checked

    Raises AssertionError:
    If array contains non-integer values.
    """
    for x in array:
        assert isinstance(x, int), "integers only please"


def populate_pigeonholes(array: List[int], holes: List[int], min_val: int) -> None:
    """
    Populates the pigeonholes based on the input array.

    Arguments:
    array -- list of integers
    holes -- list of pigeonholes
    min_val -- minimum value in the array
    """
    for x in array:
        holes[x - min_val] += 1


def reconstruct_sorted_array(array: List[int], holes: List[int], min_val: int) -> None:
    """
    Reconstructs the original array from the pigeonholes in a sorted order.

    Arguments:
    array -- list of integers to be sorted
    holes -- list of pigeonholes
    min_val -- minimum value in the array
    """
    i = 0
    for count in range(len(holes)):
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + min_val
            i += 1


if __name__ == "__main__":
    main()
