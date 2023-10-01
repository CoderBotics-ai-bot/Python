"""
Return an image of 16 generations of one-dimensional cellular automata based on a given
ruleset number
https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
"""

from __future__ import annotations

from PIL import Image
from typing import List

# Define the first generation of cells
# fmt: off
CELLS = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# fmt: on


def format_ruleset(ruleset: int) -> list[int]:
    """
    >>> format_ruleset(11100)
    [0, 0, 0, 1, 1, 1, 0, 0]
    >>> format_ruleset(0)
    [0, 0, 0, 0, 0, 0, 0, 0]
    >>> format_ruleset(11111111)
    [1, 1, 1, 1, 1, 1, 1, 1]
    """
    return [int(c) for c in f"{ruleset:08}"[:8]]



def new_generation(cells: List[List[int]], rule: List[int], time: int) -> List[int]:
    """
    Generates the next generation of cells in a cellular automaton based on the given rules.

    Args:
    cells (List[List[int]]): Current states of cells.
    rule (List[int]): The automaton evolution rules.
    time (int): Current time step.

    Returns:
    List[int]: The state of each cell within the next generation.
    """
    population = len(cells[0])
    current_generation = cells[time]

    next_generation = []
    for i in range(population):
        # obtain 'left', 'current' and 'right' cell values
        left = current_generation[i - 1] if i != 0 else 0
        current = current_generation[i]
        right = current_generation[i + 1] if i != population - 1 else 0

        # determine the new cell state by the rule set, converting binary to decimal
        situation = 7 - int(f"{left}{current}{right}", 2)
        next_generation.append(rule[situation])

    return next_generation


def generate_image(cells: list[list[int]]) -> Image.Image:
    """
    Convert the cells into a greyscale PIL.Image.Image and return it to the caller.
    >>> from random import random
    >>> cells = [[random() for w in range(31)] for h in range(16)]
    >>> img = generate_image(cells)
    >>> isinstance(img, Image.Image)
    True
    >>> img.width, img.height
    (31, 16)
    """
    # Create the output image
    img = Image.new("RGB", (len(cells[0]), len(cells)))
    pixels = img.load()
    # Generates image
    for w in range(img.width):
        for h in range(img.height):
            color = 255 - int(255 * cells[h][w])
            pixels[w, h] = (color, color, color)
    return img


if __name__ == "__main__":
    rule_num = bin(int(input("Rule:\n").strip()))[2:]
    rule = format_ruleset(int(rule_num))
    for time in range(16):
        CELLS.append(new_generation(CELLS, rule, time))
    img = generate_image(CELLS)
    # Uncomment to save the image
    # img.save(f"rule_{rule_num}.png")
    img.show()
