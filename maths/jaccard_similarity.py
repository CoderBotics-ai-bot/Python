"""
The Jaccard similarity coefficient is a commonly used indicator of the
similarity between two sets. Let U be a set and A and B be subsets of U,
then the Jaccard index/similarity is defined to be the ratio of the number
of elements of their intersection and the number of elements of their union.

Inspired from Wikipedia and
the book Mining of Massive Datasets [MMDS 2nd Edition, Chapter 3]

https://en.wikipedia.org/wiki/Jaccard_index
https://mmds.org

Jaccard similarity is widely used with MinHashing.
"""


from typing import List, Tuple, Union


def jaccard_similarity(
    set_a: Union[set, List, Tuple],
    set_b: Union[set, List, Tuple],
    alternative_union: bool = False,
) -> float:
    """
    Compute the Jaccard similarity between two sets, lists, or tuples.
    Jaccard similarity is the ratio of the size of the intersection to the size of the union
    of the two sets.
    Raises a ValueError if the input is not of the types set, list, or tuple.
    """

    set_a, set_b = validate_input(set_a, set_b)

    intersect = compute_intersection(set_a, set_b)
    union = compute_union(set_a, set_b, alternative_union)

    return intersect / union


if __name__ == "__main__":
    set_a = {"a", "b", "c", "d", "e"}
    set_b = {"c", "d", "e", "f", "h", "i"}
    print(jaccard_similarity(set_a, set_b))

def validate_input(
    set_a: Union[set, List, Tuple], set_b: Union[set, List, Tuple]
) -> Tuple[set, set]:
    """
    Validate the types of the inputs and convert lists and tuples to sets for processing.
    Raises a ValueError if the input is not of the types set, list, or tuple.
    """
    if not all(isinstance(x, (set, list, tuple)) for x in (set_a, set_b)):
        raise ValueError("Both inputs must be of type set, list or tuple.")

    return set(set_a), set(set_b)


def compute_intersection(set_a: set, set_b: set) -> int:
    """Compute intersection of two sets and return its size"""
    return len(set_a & set_b)


def compute_union(set_a: set, set_b: set, alternative: bool = False) -> int:
    """Compute union of two sets in two different ways and return its size"""
    if alternative:
        return len(set_a) + len(set_b)
    return len(set_a | set_b)
