from cellular_automata.game_of_life import *
import pytest


def test_judge_point_no_errors(game_of_life_instance):
    """
    Test to check if __judge_point function runs without throwing any errors
    """
    neighbours = [[True, False, True], [False, True, False], [True, False, True]]
    assert game_of_life_instance._GameOfLife__judge_point(True, neighbours) is not None


def test_judge_point_alive_less_than_2(game_of_life_instance):
    """
    Test to check if __judge_point function returns correct result when alive cells around pt is less than 2
    """
    neighbours = [[False, False, False], [False, True, False], [False, False, False]]
    assert not game_of_life_instance._GameOfLife__judge_point(True, neighbours)


def test_judge_point_alive_equal_to_2_or_3(game_of_life_instance):
    """
    Test to check if __judge_point function returns correct result when alive cells around pt is 2 or 3
    """
    neighbours = [[True, False, True], [False, True, False], [True, False, False]]
    assert game_of_life_instance._GameOfLife__judge_point(True, neighbours)


def test_judge_point_alive_greater_than_3(game_of_life_instance):
    """
    Test to check if __judge_point function returns correct result when alive cells around pt is more than 3
    """
    neighbours = [[True, True, True], [True, True, True], [True, True, True]]
    assert not game_of_life_instance._GameOfLife__judge_point(True, neighbours)


def test_judge_point_dead_becomes_alive(game_of_life_instance):
    """
    Test to check if __judge_point function returns correct result when dead cell becomes alive (i.e. it has exactly 3 alive neighbours)
    """
    neighbours = [[False, True, False], [True, False, True], [False, False, False]]
    assert game_of_life_instance._GameOfLife__judge_point(False, neighbours)


def test_judge_point_dead_stays_dead(game_of_life_instance):
    """
    Test to check if __judge_point function returns correct result when dead cell stays dead (i.e. it has not exactly 3 alive neighbours)
    """
    neighbours = [[False, False, False], [False, False, False], [False, False, False]]
    assert not game_of_life_instance._GameOfLife__judge_point(False, neighbours)


@pytest.fixture
def game_of_life_instance():
    class GameOfLife:
        def __judge_point(self, pt: bool, neighbours: list[list[bool]]) -> bool:
            dead = 0
            alive = 0
            for i in neighbours:
                for status in i:
                    if status:
                        alive += 1
                    else:
                        dead += 1

            if pt:
                alive -= 1
            else:
                dead -= 1

            state = pt
            if pt:
                if alive < 2:
                    state = False
                elif alive in {2, 3}:
                    state = True
                elif alive > 3:
                    state = False
            else:
                if alive == 3:
                    state = True

            return state

    return GameOfLife()
