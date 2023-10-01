from other.scoring_algorithm import *
import pytest


def test_generate_final_scores_no_errors():
    score_lists = [[1.0, 0.0, 0.33], [0.75, 1.0, 0.25], [0.0, 0.0, 1.0]]
    result = generate_final_scores(score_lists)
    assert result is not None


def test_generate_final_scores_output_type():
    score_lists = [[0.5, 1.0, 0.33], [0.5, 0.0, 0.75], [1.0, 0.0, 0.0]]
    result = generate_final_scores(score_lists)
    assert isinstance(result, list)
    assert all(isinstance(score, float) for score in result)


def test_generate_final_scores_single_score_list():
    score_lists = [[1.0, 0.75, 0.25]]
    result = generate_final_scores(score_lists)
    assert result == score_lists[0]
