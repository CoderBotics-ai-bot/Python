from dynamic_programming.edit_distance import *
import pytest


def test_min_dist_top_down_dp():
    ed = EditDistance()
    ed.word1 = "kitten"
    ed.word2 = "sitting"
    ed.dp = [[-1 for _ in range(len(ed.word2) + 1)] for _ in range(len(ed.word1) + 1)]
    assert (
        ed._EditDistance__min_dist_top_down_dp(len(ed.word1) - 1, len(ed.word2) - 1)
        == 3
    )

    ed.word1 = "rosettacode"
    ed.word2 = "raisethysword"
    ed.dp = [[-1 for _ in range(len(ed.word2) + 1)] for _ in range(len(ed.word1) + 1)]
    assert (
        ed._EditDistance__min_dist_top_down_dp(len(ed.word1) - 1, len(ed.word2) - 1)
        == 8
    )

    ed.word1 = "python"
    ed.word2 = "python"
    ed.dp = [[-1 for _ in range(len(ed.word2) + 1)] for _ in range(len(ed.word1) + 1)]
    assert (
        ed._EditDistance__min_dist_top_down_dp(len(ed.word1) - 1, len(ed.word2) - 1)
        == 0
    )

    ed.word1 = ""
    ed.word2 = "python"
    ed.dp = [[-1 for _ in range(len(ed.word2) + 1)] for _ in range(len(ed.word1) + 1)]
    assert (
        ed._EditDistance__min_dist_top_down_dp(len(ed.word1) - 1, len(ed.word2) - 1)
        == 6
    )

    ed.word1 = "python"
    ed.word2 = ""
    ed.dp = [[-1 for _ in range(len(ed.word2) + 1)] for _ in range(len(ed.word1) + 1)]
    assert (
        ed._EditDistance__min_dist_top_down_dp(len(ed.word1) - 1, len(ed.word2) - 1)
        == 6
    )
