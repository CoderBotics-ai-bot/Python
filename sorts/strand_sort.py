import operator
from typing import List, Optional


from typing import List, Optional

def strand_sort(
    arr: List[int], reverse: bool = False, solution: Optional[List[int]] = None
) -> List[int]:
    def extract_sublist(arr: List[int], _operator):
        sublist = [arr.pop(0)]
        arr_copy = arr.copy()
        for item in arr_copy:
            if _operator(item, sublist[-1]):
                sublist.append(item)
                arr.remove(item)
        return sublist

    def merge_sublist(sublist: List[int], solution: List[int], _operator):
        for item in sublist:
            for i, xx in enumerate(solution):
                if not _operator(item, xx):
                    solution.insert(i, item)
                    break
            else:
                solution.append(item)

    _operator = operator.lt if reverse else operator.gt
    solution = solution or []
    if not arr:
        return solution

    sublist = extract_sublist(arr, _operator)
    merge_sublist(sublist, solution, _operator)

    return strand_sort(arr, reverse, solution)


if __name__ == "__main__":
    assert strand_sort([4, 3, 5, 1, 2]) == [1, 2, 3, 4, 5]
    assert strand_sort([4, 3, 5, 1, 2], reverse=True) == [5, 4, 3, 2, 1]
