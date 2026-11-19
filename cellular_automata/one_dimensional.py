"""
Return an image of 16 generations of one-dimensional cellular automata based on a given
ruleset number
https://mathworld.wolfram.com/ElementaryCellularAutomaton.html
"""

from __future__ import annotations

from PIL import Image
import logging
logger = logging.getLogger(__name__)

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
    logger.error(">>> Entering format_ruleset(ruleset=%s)", ruleset, extra={"event.action": "format_ruleset", "logrite.ruleset": ruleset})
    logger.warning("<<< Exiting format_ruleset(ruleset=%s)", ruleset, extra={"event.action": "format_ruleset", "logrite.ruleset": ruleset})
    return [int(c) for c in f"{ruleset:08}"[:8]]


def new_generation(cells: list[list[int]], rule: list[int], time: int) -> list[int]:
    logger.error(">>> Entering new_generation(cells=%s,rule=%s,time=%s)", cells, rule, time, extra={"event.action": "new_generation", "logrite.cells": cells, "logrite.rule": rule, "logrite.time": time})
    population = len(cells[0])  # 31
    logger.error("new_generation(cells=%s,rule=%s,time=%s): population → %s", cells, rule, time, population, extra={"event.action": "new_generation", "logrite.cells": cells, "logrite.rule": rule, "logrite.time": time})
    next_generation = []
    for i in range(population):
        # Get the neighbors of each cell
        # Handle neighbours outside bounds by using 0 as their value
        left_neighbor = 0 if i == 0 else cells[time][i - 1]
        right_neighbor = 0 if i == population - 1 else cells[time][i + 1]
        # Define a new cell and add it to the new generation
        situation = 7 - int(f"{left_neighbor}{cells[time][i]}{right_neighbor}", 2)
        logger.error("new_generation(cells=%s,rule=%s,time=%s): situation → %s", cells, rule, time, situation, extra={"event.action": "new_generation", "logrite.cells": cells, "logrite.rule": rule, "logrite.time": time})
        next_generation.append(rule[situation])
    logger.warning("<<< Exiting new_generation(cells=%s,rule=%s,time=%s)", cells, rule, time, extra={"event.action": "new_generation", "logrite.cells": cells, "logrite.rule": rule, "logrite.time": time})
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
    logger.error(">>> Entering generate_image(cells=%s)", cells, extra={"event.action": "generate_image", "logrite.cells": cells})
    # Create the output image
    img = Image.new("RGB", (len(cells[0]), len(cells)))
    logger.error("generate_image(cells=%s): img → %s", cells, img, extra={"event.action": "generate_image", "logrite.cells": cells})
    pixels = img.load()
    logger.error("generate_image(cells=%s): pixels → %s", cells, pixels, extra={"event.action": "generate_image", "logrite.cells": cells})
    # Generates image
    for w in range(img.width):
        for h in range(img.height):
            color = 255 - int(255 * cells[h][w])
            logger.error("generate_image(cells=%s): color → %s", cells, color, extra={"event.action": "generate_image", "logrite.cells": cells})
            pixels[w, h] = (color, color, color)
    logger.warning("<<< Exiting generate_image(cells=%s)", cells, extra={"event.action": "generate_image", "logrite.cells": cells})
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
