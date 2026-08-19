"""
The A* algorithm combines features of uniform-cost search and pure heuristic search to
efficiently compute optimal solutions.

The A* algorithm is a best-first search algorithm in which the cost associated with a
node is f(n) = g(n) + h(n), where g(n) is the cost of the path from the initial state to
node n and h(n) is the heuristic estimate or the cost or a path from node n to a goal.

The A* algorithm introduces a heuristic into a regular graph-searching algorithm,
essentially planning ahead at each step so a more optimal decision is made. For this
reason, A* is known as an algorithm with brains.

https://en.wikipedia.org/wiki/A*_search_algorithm
"""

import numpy as np
import logging
logger = logging.getLogger(__name__)


class Cell:
    """
    Class cell represents a cell in the world which have the properties:
    position: represented by tuple of x and y coordinates initially set to (0,0).
    parent: Contains the parent cell object visited before we arrived at this cell.
    g, h, f: Parameters used when calling our heuristic function.
    """

    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.position = (0, 0)
        logger.debug("__init__(): self.position → %s", self.position)
        self.parent = None
        logger.debug("__init__(self=%s): self.parent → %s", self, self.parent)
        self.g = 0
        logger.debug("__init__(self=%s): self.g → %s", self, self.g)
        self.h = 0
        logger.debug("__init__(self=%s): self.h → %s", self, self.h)
        self.f = 0
        logger.debug("__init__(self=%s): self.f → %s", self, self.f)
        logger.debug("<<< Exiting __init__()")
        logger.debug(">>> Entering __init__(world_size=%s)", world_size)
        logger.debug("__init__(world_size=%s): self.w → %s", world_size, self.w)
        logger.debug("__init__(self=%s,world_size=%s): self.world_x_limit → %s", self, world_size, self.world_x_limit)
        logger.debug("<<< Exiting __init__(world_size=%s)", world_size)

    """
    Overrides equals method because otherwise cell assign will give
    wrong results.
    """

    def __eq__(self, cell):
        logger.debug(">>> Entering __eq__(cell=%s)", cell)
        logger.debug("<<< Exiting __eq__(cell=%s)", cell)
        return self.position == cell.position

    def showcell(self):
        logger.debug(">>> Entering showcell()")
        print(self.position)
        logger.debug("<<< Exiting showcell()")


class Gridworld:
    """
    Gridworld class represents the  external world here a grid M*M
    matrix.
    world_size: create a numpy array with the given world_size default is 5.
    """

    def __init__(self, world_size=(5, 5)):
        self.w = np.zeros(world_size)
        self.world_x_limit = world_size[0]
        self.world_y_limit = world_size[1]
        logger.debug("__init__(self=%s,world_size=%s): self.world_y_limit → %s", self, world_size, self.world_y_limit)

    def show(self):
        logger.debug(">>> Entering show()")
        print(self.w)
        logger.debug("<<< Exiting show()")

    def get_neighbours(self, cell):
        """
        Return the neighbours of cell
        """
        logger.debug(">>> Entering get_neighbours(cell=%s)", cell)
        neughbour_cord = [
        logger.debug("get_neighbours(self=%s,cell=%s): neughbour_cord → %s", self, cell, neughbour_cord)
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        current_x = cell.position[0]
        logger.debug("get_neighbours(self=%s,cell=%s): current_x → %s", self, cell, current_x)
        current_y = cell.position[1]
        logger.debug("get_neighbours(self=%s,cell=%s): current_y → %s", self, cell, current_y)
        neighbours = []
        logger.debug("get_neighbours(self=%s,cell=%s): neighbours → %s", self, cell, neighbours)
        for n in neughbour_cord:
            x = current_x + n[0]
            y = current_y + n[1]
            if 0 <= x < self.world_x_limit and 0 <= y < self.world_y_limit:
                c = Cell()
                logger.debug("get_neighbours(cell=%s): c → %s", cell, c)
                c.position = (x, y)
                c.parent = cell
                logger.debug("get_neighbours(self=%s,cell=%s): c.parent → %s", self, cell, c.parent)
                neighbours.append(c)
        logger.debug("<<< Exiting get_neighbours(cell=%s)", cell)
        return neighbours


def astar(world, start, goal):
    """
    Implementation of a start algorithm.
    world : Object of the world object.
    start : Object of the cell as  start position.
    stop  : Object of the cell as goal position.

    >>> p = Gridworld()
    >>> start = Cell()
    >>> start.position = (0,0)
    >>> goal = Cell()
    >>> goal.position = (4,4)
    >>> astar(p, start, goal)
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    """
    logger.debug(">>> Entering astar(world=%s,start=%s,goal=%s)", world, start, goal)
    _open = []
    logger.debug("astar(world=%s,start=%s,goal=%s): _open → %s", world, start, goal, _open)
    _closed = []
    logger.debug("astar(world=%s,start=%s,goal=%s): _closed → %s", world, start, goal, _closed)
    _open.append(start)

    while _open:
        min_f = np.argmin([n.f for n in _open])
        logger.debug("astar(world=%s,start=%s,goal=%s): min_f → %s", world, start, goal, min_f)
        current = _open[min_f]
        _closed.append(_open.pop(min_f))
        if current == goal:
            break
        for n in world.get_neighbours(current):
            for c in _closed:
                if c == n:
                    continue
            n.g = current.g + 1
            logger.debug("astar(world=%s,start=%s,goal=%s): n.g → %s", world, start, goal, n.g)
            x1, y1 = n.position
            x2, y2 = goal.position
            n.h = (y2 - y1) ** 2 + (x2 - x1) ** 2
            n.f = n.h + n.g
            logger.debug("astar(world=%s,start=%s,goal=%s): n.f → %s", world, start, goal, n.f)

            for c in _open:
                if c == n and c.f < n.f:
                    continue
            _open.append(n)
    path = []
    logger.debug("astar(world=%s,start=%s,goal=%s): path → %s", world, start, goal, path)
    while current.parent is not None:
        path.append(current.position)
        current = current.parent
    path.append(current.position)
    logger.debug("<<< Exiting astar(world=%s,start=%s,goal=%s)", world, start, goal)
    return path[::-1]


if __name__ == "__main__":
    world = Gridworld()
    # Start position and goal
    start = Cell()
    start.position = (0, 0)
    goal = Cell()
    goal.position = (4, 4)
    print(f"path from {start.position} to {goal.position}")
    s = astar(world, start, goal)
    #   Just for visual reasons.
    for i in s:
        world.w[i] = 1
    print(world.w)
