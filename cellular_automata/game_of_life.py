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
import logging
logger = logging.getLogger(__name__)

usage_doc = "Usage of script: script_name <size_of_canvas:int>"

choice = [0] * 100 + [1] * 10
random.shuffle(choice)


def create_canvas(size: int) -> list[list[bool]]:
    logger.debug(">>> Entering create_canvas(size=%s)", size)
    canvas = [[False for i in range(size)] for j in range(size)]
    logger.debug("create_canvas(size=%s): canvas → %s", size, canvas)
    logger.debug("<<< Exiting create_canvas(size=%s)", size)
    return canvas


def seed(canvas: list[list[bool]]) -> None:
    logger.debug(">>> Entering seed(canvas=%s)", canvas)
    for i, row in enumerate(canvas):
        for j, _ in enumerate(row):
            canvas[i][j] = bool(random.getrandbits(1))
            logger.debug("<<< Exiting seed(canvas=%s)", canvas)


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
    logger.debug(">>> Entering run(canvas=%s)", canvas)
    current_canvas = np.array(canvas)
    logger.debug("run(canvas=%s): current_canvas → %s", canvas, current_canvas)
    next_gen_canvas = np.array(create_canvas(current_canvas.shape[0]))
    logger.debug("run(canvas=%s): next_gen_canvas → %s", canvas, next_gen_canvas)
    for r, row in enumerate(current_canvas):
        for c, pt in enumerate(row):
            next_gen_canvas[r][c] = __judge_point(
                pt, current_canvas[r - 1 : r + 2, c - 1 : c + 2]
            )

    logger.debug("<<< Exiting run(canvas=%s)", canvas)
    return next_gen_canvas.tolist()


def __judge_point(pt: bool, neighbours: list[list[bool]]) -> bool:
    logger.debug(">>> Entering __judge_point(pt=%s,neighbours=%s)", pt, neighbours)
    dead = 0
    logger.debug("__judge_point(pt=%s,neighbours=%s): dead → %s", pt, neighbours, dead)
    alive = 0
    # finding dead or alive neighbours count.
    for i in neighbours:
        for status in i:
            if status:
                alive += 1
            else:
                dead += 1

    # handling duplicate entry for focus pt.
    if pt:
        alive -= 1
    else:
        dead -= 1

    # running the rules of game here.
    state = pt
    logger.debug("__judge_point(pt=%s,neighbours=%s): state → %s", pt, neighbours, state)
    if pt:
        if alive < 2:
            state = False
        elif alive in {2, 3}:
            state = True
        elif alive > 3:
            state = False
    elif alive == 3:
        state = True

    logger.debug("<<< Exiting __judge_point(pt=%s,neighbours=%s)", pt, neighbours)
    return state


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
