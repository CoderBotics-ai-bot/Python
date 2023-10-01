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


def generate_images(cells: List[List[int]], frames: int) -> List[Image.Image]:
    """
    Generates a list of images of subsequent Game of Life states.

    Args:
        cells (List[List[int]]): The initial state of the Game of Life grid.
        A 2D list containing 1s (alive cells) and 0s (dead cells).
        frames (int): The number of frames to generate. Each frame is a subsequent
        state in the Game of Life game.

    Returns:
        List[Image.Image]: A list of PIL Image objects representing each frame.

    The function generates each frame by first creating an empty image, then populates
    the image with black (representing alive cells) and white (representing dead cells) pixels
    based on the state of the cells. For each frame, the cells argument is updated to the
    next generation using the new_generation function.
    """
    images = [cells_to_image(cells)]

    for _ in range(frames - 1):
        cells = new_generation(cells)
        images.append(cells_to_image(cells))

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

def cells_to_image(cells: List[List[int]]) -> Image.Image:
    """
    Create an image from the Game of Life cells

    Args:
        cells (List[List[int]]): The current state of the Game of Life grid.

    Returns:
        Image.Image: A PIL Image object representing the current state.
    """

    # initialize image
    img = Image.new("RGB", (len(cells[0]), len(cells)))
    pixels = img.load()

    # colour the image based on the cell state
    for x in range(len(cells)):
        for y in range(len(cells[0])):
            colour = 255 - cells[y][x] * 255
            pixels[x, y] = (colour, colour, colour)

    return img


if __name__ == "__main__":
    images = generate_images(GLIDER, 16)
    images[0].save("out.gif", save_all=True, append_images=images[1:])
