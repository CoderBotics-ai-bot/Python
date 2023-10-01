"""
Simulate the evolution of a highway with only one road that is a loop.
The highway is divided in cells, each cell can have at most one car in it.
The highway is a loop so when a car comes to one end, it will come out on the other.
Each car is represented by its speed (from 0 to 5).

Some information about speed:
    -1 means that the cell on the highway is empty
    0 to 5 are the speed of the cars with 0 being the lowest and 5 the highest

highway: list[int]  Where every position and speed of every car will be stored
probability         The probability that a driver will slow down
initial_speed       The speed of the cars a the start
frequency           How many cells there are between two cars at the start
max_speed           The maximum speed a car can go to
number_of_cells     How many cell are there in the highway
number_of_update    How many times will the position be updated

More information here: https://en.wikipedia.org/wiki/Nagel%E2%80%93Schreckenberg_model

Examples for doctest:
>>> simulate(construct_highway(6, 3, 0), 2, 0, 2)
[[0, -1, -1, 0, -1, -1], [-1, 1, -1, -1, 1, -1], [-1, -1, 1, -1, -1, 1]]
>>> simulate(construct_highway(5, 2, -2), 3, 0, 2)
[[0, -1, 0, -1, 0], [0, -1, 0, -1, -1], [0, -1, -1, 1, -1], [-1, 1, -1, 0, -1]]
"""
from random import randint, random


from random import randint


from random import random
from typing import List

def construct_highway(
    number_of_cells: int,
    frequency: int,
    initial_speed: int,
    random_frequency: bool = False,
    random_speed: bool = False,
    max_speed: int = 5,
) -> list:
    """
    This function builds a highway populated with cars at defined distances.

    Args:
        number_of_cells (int): The number of cells in the highway (length of the highway).
        frequency (int): The frequency of cars on the highway. A car will be placed every nth cell, where n is the frequency.
        initial_speed (int): The initial speed of all cars.
        random_frequency (bool, optional): If True, cars will be placed at random distances apart. Defaults to False.
        random_speed (bool, optional): If True, each car will start with a random speed. Defaults to False.
        max_speed (int, optional): The maximum allowable random speed. Defaults to 5.

    Returns:
        list: A 2D list representing the state of the highway.
    """

    # ensure that speed is non-negative
    initial_speed = max(initial_speed, 0)

    # construct the highway
    highway = [
        -1
        if (index % frequency != 0)
        or (random_frequency and randint(1, max_speed * 2) != 1)
        else randint(0, max_speed)
        if random_speed
        else initial_speed
        for index in range(number_of_cells)
    ]

    return [highway]


def get_distance(highway_now: list, car_index: int) -> int:
    """
    Get the distance between a car (at index car_index) and the next car
    >>> get_distance([6, -1, 6, -1, 6], 2)
    1
    >>> get_distance([2, -1, -1, -1, 3, 1, 0, 1, 3, 2], 0)
    3
    >>> get_distance([-1, -1, -1, -1, 2, -1, -1, -1, 3], -1)
    4
    """

    distance = 0
    cells = highway_now[car_index + 1 :]
    for cell in range(len(cells)):  # May need a better name for this
        if cells[cell] != -1:  # If the cell is not empty then
            return distance  # we have the distance we wanted
        distance += 1
    # Here if the car is near the end of the highway
    return distance + get_distance(highway_now, -1)


def simulate(
    highway: List[List[int]], number_of_update: int, probability: float, max_speed: int
) -> List[List[int]]:
    """
    Simulates the evolution of the highway status according to traffic rules.
    """
    for _ in range(number_of_update):
        next_speeds = update(highway[-1], probability, max_speed)
        highway.append(update_highway(highway[-1], next_speeds))
    return highway


def update(highway_now: list, probability: float, max_speed: int) -> list:
    """
    Updates...

    Args:
        highway_now...
        probability...
        max_speed...

    Returns:
        list...

    Examples:
        >>> update...
    """
    next_highway = [-1] * len(highway_now)
    for car_index, current_speed in enumerate(highway_now):
        if current_speed == -1:
            continue
        dn = get_distance(highway_now, car_index)
        next_highway[car_index] = update_car_speed(
            current_speed, max_speed, dn, probability
        )
    return next_highway

def update_highway(current_speeds: List[int], next_speeds: List[int]) -> List[int]:
    """Update the locations of each car based on the next calculated speed."""
    real_next_speeds = [-1] * len(current_speeds)
    for car_index, speed in enumerate(next_speeds):
        if speed != -1:
            real_next_speeds[(car_index + speed) % len(current_speeds)] = speed
    return real_next_speeds

def update_car_speed(
    current_speed: int, max_speed: int, distance_to_next: int, slow_down_prob: float
) -> int:
    """
    Update car speed according to rules. The speed depends on its current speed,
    the maximum speed limit, the distance to the next car and the probability
    of a spontaneous slowdown.

    Args:
        current_speed (int): Current speed of the car.
        max_speed (int): Maximum speed limit.
        distance_to_next (int): Distance to the next car.
        slow_down_prob (float): The probability that a spontaneous slowdown occurs.

    Returns:
        int: The new speed of the car.
    """
    new_speed = min(current_speed + 1, max_speed)
    new_speed = min(new_speed, distance_to_next - 1)
    if random() < slow_down_prob:
        new_speed = max(new_speed - 1, 0)
    return new_speed


if __name__ == "__main__":
    import doctest

    doctest.testmod()
