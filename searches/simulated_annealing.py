# https://en.wikipedia.org/wiki/Simulated_annealing
import math
import random
from typing import Any

from .hill_climbing import SearchProblem
import math


from typing import Any, List
import random, math


def simulated_annealing(
    search_prob: SearchProblem,
    find_max: bool = True,
    max_x: float = math.inf,
    min_x: float = -math.inf,
    max_y: float = math.inf,
    min_y: float = -math.inf,
    visualization: bool = False,
    start_temperate: float = 100,
    rate_of_decrease: float = 0.01,
    threshold_temp: float = 1,
) -> Any:
    current_state = search_prob
    current_temp = start_temperate
    best_state = None
    scores = []

    while current_temp >= threshold_temp:
        current_score = current_state.score()
        best_state = (
            current_state
            if best_state is None or current_score > best_state.score()
            else best_state
        )
        scores.append(current_score)

        neighbors = current_state.get_neighbors()
        next_state = None

        while not next_state and neighbors:
            picked_neighbor = get_random_neighbor(neighbors)

            if not is_valid_neighbor(picked_neighbor, max_x, min_x, max_y, min_y):
                continue

            change = (picked_neighbor.score() - current_score) * (
                -1 if not find_max else 1
            )

            if change > 0 or neighbor_probability_change(change, current_temp):
                next_state = picked_neighbor

        current_temp = update_temperature(current_temp, rate_of_decrease)

        if next_state is None:
            break
        else:
            current_state = next_state

    if visualization:
        from matplotlib import pyplot as plt

        plt.plot(range(len(scores)), scores)
        plt.xlabel("Iterations")
        plt.ylabel("Function values")
        plt.show()

    return best_state


if __name__ == "__main__":

    def test_f1(x, y):
        return (x**2) + (y**2)

    # starting the problem with initial coordinates (12, 47)
    prob = SearchProblem(x=12, y=47, step_size=1, function_to_optimize=test_f1)
    local_min = simulated_annealing(
        prob, find_max=False, max_x=100, min_x=5, max_y=50, min_y=-5, visualization=True
    )
    print(
        "The minimum score for f(x, y) = x^2 + y^2 with the domain 100 > x > 5 "
        f"and 50 > y > - 5 found via hill climbing: {local_min.score()}"
    )

    # starting the problem with initial coordinates (12, 47)
    prob = SearchProblem(x=12, y=47, step_size=1, function_to_optimize=test_f1)
    local_min = simulated_annealing(
        prob, find_max=True, max_x=100, min_x=5, max_y=50, min_y=-5, visualization=True
    )
    print(
        "The maximum score for f(x, y) = x^2 + y^2 with the domain 100 > x > 5 "
        f"and 50 > y > - 5 found via hill climbing: {local_min.score()}"
    )

    def test_f2(x, y):
        return (3 * x**2) - (6 * y)

    prob = SearchProblem(x=3, y=4, step_size=1, function_to_optimize=test_f1)
    local_min = simulated_annealing(prob, find_max=False, visualization=True)
    print(
        "The minimum score for f(x, y) = 3*x^2 - 6*y found via hill climbing: "
        f"{local_min.score()}"
    )

    prob = SearchProblem(x=3, y=4, step_size=1, function_to_optimize=test_f1)
    local_min = simulated_annealing(prob, find_max=True, visualization=True)
    print(
        "The maximum score for f(x, y) = 3*x^2 - 6*y found via hill climbing: "
        f"{local_min.score()}"
    )

def get_random_neighbor(neighbors: List[SearchProblem]) -> SearchProblem:
    """Pick a random neighbor from the list."""
    index = random.randint(0, len(neighbors) - 1)
    return neighbors.pop(index)


def is_valid_neighbor(
    neighbor: SearchProblem, max_x: float, min_x: float, max_y: float, min_y: float
) -> bool:
    """Check if potential neighbor is within defined bounds."""
    return not (
        neighbor.x > max_x
        or neighbor.x < min_x
        or neighbor.y > max_y
        or neighbor.y < min_y
    )


def update_temperature(current_temp: float, rate_of_decrease: float) -> float:
    """Decrease the temperature based on rate_of_decrease"""
    return current_temp - (current_temp * rate_of_decrease)


def neighbor_probability_change(change: float, current_temp: float) -> bool:
    """Probability function deciding if a neighbor causing negative change should be accepted."""
    probability = math.exp(change / current_temp)
    return random.random() < probability
