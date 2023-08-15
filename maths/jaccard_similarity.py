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

def jaccard_similarity(
    set_a: set, set_b: set, alternative_union: Optional[bool] = False
) -> Union[float, None]:
    """
    Compute the Jaccard similarity coefficient between two sets.

    The Jaccard coefficient measures similarity between finite sample sets, and
    is defined as the size of the intersection divided by the size of the union
    of the sample sets.

    An alternative way to calculate this, which could be enabled by setting alternative_union=True,
    is to take the union as the sum of the number of items in the two sets. This results in a Jaccard
    similarity of a set with itself being 1/2 instead of 1.

    Parameters:
        set_a (set): A set of hashable items.
        set_b (set): A set of hashable items.
        alternative_union (Optional[bool]=False): If set to True, use the alternative way
            of calculating the union. Defaults to False.

    Returns:
        float: The Jaccard similarity coefficient between the two sets if successful.
        None: If the inputs are not of correct types.

    Raises:
        ValueError: If the inputs are not sets.

    Examples:
        >>> set_a = {'a', 'b', 'c', 'd', 'e'}
        >>> set_b = {'c', 'd', 'e', 'f', 'h', 'i'}
        >>> jaccard_similarity(set_a, set_b)
        0.375

        >>> jaccard_similarity(set_a, set_a)
        1.0

        >>> jaccard_similarity(set_a, set_a, True)
        0.5
    """
    if not isinstance(set_a, set) or not isinstance(set_b, set):
        raise ValueError("Inputs should be of set type")

    intersection_cardinality = len(set_a.intersection(set_b))
    if alternative_union:
        union_cardinality = len(set_a) + len(set_b)
    else:
        union_cardinality = len(set_a.union(set_b))
    return intersection_cardinality / union_cardinality


if __name__ == "__main__":
    set_a = {"a", "b", "c", "d", "e"}
    set_b = {"c", "d", "e", "f", "h", "i"}
    print(jaccard_similarity(set_a, set_b))
