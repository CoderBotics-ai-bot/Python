"""
Conway's Game of Life implemented in Python.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""
from __future__ import annotations

from PIL import Image


from typing import List

# Define glider example
GLIDER = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Define blinker example
BLINKER = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


def new_generation(cells: List[List[int]]) -> List[List[int]]:
    rows, cols = len(cells), len(cells[0])
    next_generation = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            neighbour_count = _get_neighbour_count(cells, i, j)
            is_alive = cells[i][j] == 1

            if (is_alive and 2 <= neighbour_count <= 3) or (
                not is_alive and neighbour_count == 3
            ):
                next_generation[i][j] = 1

    return next_generation


def generate_images(cells: list[list[int]], frames: int) -> list[Image.Image]:
    """
    Generates a list of images of subsequent Game of Life states.
    """
    images = []
    for _ in range(frames):
        # Create output image
        img = Image.new("RGB", (len(cells[0]), len(cells)))
        pixels = img.load()

        # Save cells to image
        for x in range(len(cells)):
            for y in range(len(cells[0])):
                colour = 255 - cells[y][x] * 255
                pixels[x, y] = (colour, colour, colour)

        # Save image
        images.append(img)
        cells = new_generation(cells)
    return images

def _get_neighbour_count(cells: List[List[int]], i: int, j: int) -> int:
    """A helper function to compute the number of alive neighbors of a cell."""
    neighbour_count = 0
    rows, cols = len(cells), len(cells[0])

    for a in range(max(0, i - 1), min(rows, i + 2)):
        for b in range(max(0, j - 1), min(cols, j + 2)):
            neighbour_count += cells[a][b]

    neighbour_count -= cells[i][j]  # Do not count the cell itself
    return neighbour_count


if __name__ == "__main__":
    images = generate_images(GLIDER, 16)
    images[0].save("out.gif", save_all=True, append_images=images[1:])
