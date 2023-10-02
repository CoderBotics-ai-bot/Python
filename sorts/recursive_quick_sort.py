from typing import List, Any


from typing import List, Any, Tuple

def quick_sort(data: List[Any]) -> List[Any]:
    """
    The quick_sort function performs the quick sort algorithm on a given list.

    Args:
        data (List[Any]): A list of sortable elements (integers, strings, floats etc.)

    Returns:
        List[Any]: Returns a copy of the original list with the elements sorted in ascending order.
    """
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        smaller, equal, larger = partition(data, pivot)
        return quick_sort(smaller) + equal + quick_sort(larger)


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def partition(data: List[Any], pivot: Any) -> Tuple[List[Any], List[Any], List[Any]]:
    """
    Function to partition given list into three parts - smaller, equal and larger
    than the pivot element.

    Args:
        data: list of elements to be partitioned.
        pivot: element around which to partition the list.

    Returns:
        Tuple of three lists having elements smaller, equal and larger than pivot.
    """
    smaller, equal, larger = [], [], []
    for element in data:
        if element < pivot:
            smaller.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            larger.append(element)
    return smaller, equal, larger
