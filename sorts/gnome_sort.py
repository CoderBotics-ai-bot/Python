"""
Gnome Sort Algorithm (A.K.A. Stupid Sort)

This algorithm iterates over a list comparing an element with the previous one.
If order is not respected, it swaps element backward until order is respected with
previous element.  It resumes the initial iteration from element new position.

For doctests run following command:
python3 -m doctest -v gnome_sort.py

For manual testing run:
python3 gnome_sort.py
"""


from typing import List, Any

def gnome_sort(lst: List[Any]) -> List[Any]:
    """
    Pure implementation of the gnome sort algorithm in Python.

    Argument:
        lst: some mutable ordered collection with heterogeneous comparable items.

    Returns:
         same collection ordered by ascending.

    Examples:
        >>> gnome_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]

        >>> gnome_sort([])
        []

        >>> gnome_sort([-2, -5, -45])
        [-45, -5, -2]

        >>> "".join(gnome_sort(list(set("Gnomes are stupid!"))))
        ' !Gadeimnoprstu'
    """

    def swap(items: List[Any], index: int) -> None:
        items[index - 1], items[index] = items[index], items[index - 1]

    len_lst = len(lst)
    if len_lst <= 1:
        return lst

    i = 1

    while i < len_lst:
        if lst[i - 1] > lst[i]:
            swap(lst, i)
            if i > 1:
                i -= 1
        else:
            i += 1

    return lst


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(gnome_sort(unsorted))
