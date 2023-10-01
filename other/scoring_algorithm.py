"""
developed by: markmelnic
original repo: https://github.com/markmelnic/Scoring-Algorithm

Analyse data using a range based percentual proximity algorithm
and calculate the linear maximum likelihood estimation.
The basic principle is that all values supplied will be broken
down to a range from 0 to 1 and each column's score will be added
up to get the total score.

==========
Example for data of vehicles
price|mileage|registration_year
20k  |60k    |2012
22k  |50k    |2011
23k  |90k    |2015
16k  |210k   |2010

We want the vehicle with the lowest price,
lowest mileage but newest registration year.
Thus the weights for each column are as follows:
[0, 0, 1]
"""


from typing import List

def get_data(source_data: List[List[float]]) -> List[List[float]]:
    """
    Transpose the input two-dimensional list.

    This function takes a two-dimensional list and returns another list
    where each inner list corresponds to a column in the original list.
    It also ensures that all elements in the resulting list are floats.

    Args:
        source_data: A two-dimensional list of mixed numerical data.
                     Each inner list corresponds to a row of data.

    Returns:
        A two-dimensional list where each inner list corresponds to a column
        in the original list. All the elements are converted to floats.

    Example:
        >>> get_data([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]])
        [[20.0, 23.0, 22.0], [60.0, 90.0, 50.0], [2012.0, 2015.0, 2011.0]]
    """
    return [list(map(float, item)) for item in zip(*source_data)]



def calculate_each_score(
    data_lists: List[List[float]], weights: List[int]
) -> List[List[float]]:
    """
    >>> calculate_each_score([[20, 23, 22], [60, 90, 50], [2012, 2015, 2011]],
    ...                      [0, 0, 1])
    [[1.0, 0.0, 0.33333333333333337], [0.75, 0.0, 1.0], [0.25, 1.0, 0.0]]
    """
    return [calculate_score(data, weight) for data, weight in zip(data_lists, weights)]



def generate_final_scores(score_lists: List[List[float]]) -> List[float]:
    """
    Compute the sum of corresponding elements from multiple lists.

    This function generates the final scores by adding up the
    corresponding elements of sub-lists of floats in the `score_lists`.

    The output list's nth element is the sum of the nth elements from
    each input sub-list.

    Parameters
    ----------
    score_lists : list of list of float
        A list of lists of floats for which the corresponding elements
        are to be summed. All sub-lists must be of equal length.

    Returns
    -------
    list of float
        A new list where the nth element is the sum of nth elements from
        each sub-list in the input list.

    Raises
    ------
    IndexError
        If lists in `score_lists` have different lengths.

    Examples
    --------
    >>> generate_final_scores([[1.0, 0.0, 0.33333333333333337],
    ...                        [0.75, 0.0, 1.0],
    ...                        [0.25, 1.0, 0.0]])
    [2.0, 1.0, 1.3333333333333335]

    """
    # use zip() to iterate over the sublists in parallel
    # use map() along with sum() to find the sum of the corresponding elements from each sublist
    final_scores = list(map(sum, zip(*score_lists)))

    return final_scores


def calculate_score(dlist: List[float], weight: int) -> List[float]:
    validate_weight(weight)
    mind = min(dlist)
    maxd = max(dlist)
    scores = calculate_scores_based_on_weight(dlist, mind, maxd, weight)
    return scores


def calculate_scores_based_on_weight(
    dlist: List[float], min_d: float, max_d: float, weight: int
) -> List[float]:
    return [(item_weight_based_score(item, min_d, max_d, weight)) for item in dlist]


def item_weight_based_score(
    item: float, min_d: float, max_d: float, weight: int
) -> float:
    try:
        score = (item - min_d) / (max_d - min_d)
    except ZeroDivisionError:
        score = 0
    return 1 - score if weight == 0 else score


def validate_weight(weight: int) -> None:
    if weight not in [0, 1]:
        raise ValueError(f"Invalid weight of {weight}: Weight can only be 0 or 1.")


def procentual_proximity(
    source_data: list[list[float]], weights: list[int]
) -> list[list[float]]:
    """
    weights - int list
    possible values - 0 / 1
    0 if lower values have higher weight in the data set
    1 if higher values have higher weight in the data set

    >>> procentual_proximity([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 0, 1])
    [[20, 60, 2012, 2.0], [23, 90, 2015, 1.0], [22, 50, 2011, 1.3333333333333335]]
    """

    data_lists = get_data(source_data)
    score_lists = calculate_each_score(data_lists, weights)
    final_scores = generate_final_scores(score_lists)

    # append scores to source data
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    return source_data
