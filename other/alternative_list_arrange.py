from typing import List, Any


from itertools import zip_longest



def alternative_list_arrange(
    first_input_list: List[Any], second_input_list: List[Any]
) -> List[Any]:
    return [
        item
        for sublist in zip_longest(first_input_list, second_input_list)
        for item in sublist
        if item is not None
    ]


if __name__ == "__main__":
    print(alternative_list_arrange(["A", "B", "C"], [1, 2, 3, 4, 5]), end=" ")
