"""Conway's Game Of Life, Author Anurag Kumar(mailto:anuragkumarak95@gmail.com)

Requirements:
  - numpy
  - random
  - time
  - matplotlib

Python:
  - 3.5

Usage:
  - $python3 game_of_life <canvas_size:int>

Game-Of-Life Rules:

 1.
 Any live cell with fewer than two live neighbours
 dies, as if caused by under-population.
 2.
 Any live cell with two or three live neighbours lives
 on to the next generation.
 3.
 Any live cell with more than three live neighbours
 dies, as if by over-population.
 4.
 Any dead cell with exactly three live neighbours be-
 comes a live cell, as if by reproduction.
 """
import random
import sys

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap


from typing import List

usage_doc = "Usage of script: script_name <size_of_canvas:int>"

choice = [0] * 100 + [1] * 10
random.shuffle(choice)


def create_canvas(size: int) -> list[list[bool]]:
    canvas = [[False for i in range(size)] for j in range(size)]
    return canvas


def seed(canvas: list[list[bool]]) -> None:
    for i, row in enumerate(canvas):
        for j, _ in enumerate(row):
            canvas[i][j] = bool(random.getrandbits(1))


def run(canvas: list[list[bool]]) -> list[list[bool]]:
    """
    This function runs the rules of game through all points, and changes their
    status accordingly.(in the same canvas)
    @Args:
    --
    canvas : canvas of population to run the rules on.

    @returns:
    --
    canvas of population after one step
    """
    current_canvas = np.array(canvas)
    next_gen_canvas = np.array(create_canvas(current_canvas.shape[0]))
    for r, row in enumerate(current_canvas):
        for c, pt in enumerate(row):
            next_gen_canvas[r][c] = __judge_point(
                pt, current_canvas[r - 1 : r + 2, c - 1 : c + 2]
            )

    return next_gen_canvas.tolist()

def __judge_point(pt: bool, neighbours: list[list[bool]]) -> bool:
    """
    Determine the future status of a specified point based on its neighbours.

    This function implements the rules of the Game of Life to decide whether a certain point
    (cell) in the life grid will be alive or dead in the next generation.

    The rules are as follows:
    - Any live cell with fewer than two live neighbours dies.
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than three live neighbours dies.
    - Any dead cell with exactly three live neighbours becomes a live cell.

    Parameters:
    pt: The current status of the point. True if the point is alive, False otherwise.
    neighbours: A 2D list of boolean values representing the statuses of the neighbours of the point.

    Returns:
    bool: The status of the point in the next generation.
         True if the point will be alive, False otherwise.
    """

    alive_neighbours = sum(status for sublist in neighbours for status in sublist)
    alive_neighbours = alive_neighbours - 1 if pt else alive_neighbours

    # running the rules of game here.
    if pt and not 2 <= alive_neighbours <= 3:
        return False

    if not pt and alive_neighbours == 3:
        return True

    return pt


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception(usage_doc)

    canvas_size = int(sys.argv[1])
    # main working structure of this module.
    c = create_canvas(canvas_size)
    seed(c)
    fig, ax = plt.subplots()
    fig.show()
    cmap = ListedColormap(["w", "k"])
    try:
        while True:
            c = run(c)
            ax.matshow(c, cmap=cmap)
            fig.canvas.draw()
            ax.cla()
    except KeyboardInterrupt:
        # do nothing.
        pass
