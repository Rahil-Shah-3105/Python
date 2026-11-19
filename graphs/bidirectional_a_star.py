"""
https://en.wikipedia.org/wiki/Bidirectional_search
"""

from __future__ import annotations

import time
from math import sqrt
import logging
logger = logging.getLogger(__name__)

# 1 for manhattan, 0 for euclidean
HEURISTIC = 0

grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],  # 0 are free path whereas 1's are obstacles
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
]

delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # up, left, down, right

TPosition = tuple[int, int]


class Node:
    """
    >>> k = Node(0, 0, 4, 3, 0, None)
    >>> k.calculate_heuristic()
    5.0
    >>> n = Node(1, 4, 3, 4, 2, None)
    >>> n.calculate_heuristic()
    2.0
    >>> l = [k, n]
    >>> n == l[0]
    False
    >>> l.sort()
    >>> n == l[0]
    True
    """

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        goal_x: int,
        goal_y: int,
        g_cost: int,
        parent: Node | None,
    ) -> None:
        logger.error(">>> Entering __init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s)", pos_x, pos_y, goal_x, goal_y, g_cost, parent, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.pos_x = pos_x
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.pos_x → %s", self, pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.pos_x, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.pos_y = pos_y
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.pos_y → %s", self, pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.pos_y, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.pos = (pos_y, pos_x)
        logger.error("__init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.pos → %s", pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.pos, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.goal_x = goal_x
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.goal_x → %s", self, pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.goal_x, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.goal_y = goal_y
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.goal_y → %s", self, pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.goal_y, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.g_cost = g_cost
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.g_cost → %s", self, pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.g_cost, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.parent = parent
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.parent → %s", self, pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.parent, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.h_cost = self.calculate_heuristic()
        logger.error("__init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.h_cost → %s", pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.h_cost, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        self.f_cost = self.g_cost + self.h_cost
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.f_cost → %s", self, pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.f_cost, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        logger.warning("<<< Exiting __init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s)", pos_x, pos_y, goal_x, goal_y, g_cost, parent, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})

    def calculate_heuristic(self) -> float:
        """
        Heuristic for the A*
        """
        logger.error(">>> Entering calculate_heuristic()", extra={"event.action": "calculate_heuristic"})
        dy = self.pos_x - self.goal_x
        dx = self.pos_y - self.goal_y
        if HEURISTIC == 1:
            return abs(dx) + abs(dy)
        else:
            logger.warning("<<< Exiting calculate_heuristic()", extra={"event.action": "calculate_heuristic"})
            return sqrt(dy**2 + dx**2)

    def __lt__(self, other: Node) -> bool:
        logger.error(">>> Entering __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        logger.warning("<<< Exiting __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        return self.f_cost < other.f_cost


class AStar:
    """
    >>> astar = AStar((0, 0), (len(grid) - 1, len(grid[0]) - 1))
    >>> (astar.start.pos_y + delta[3][0], astar.start.pos_x + delta[3][1])
    (0, 1)
    >>> [x.pos for x in astar.get_successors(astar.start)]
    [(1, 0), (0, 1)]
    >>> (astar.start.pos_y + delta[2][0], astar.start.pos_x + delta[2][1])
    (1, 0)
    >>> astar.retrace_path(astar.start)
    [(0, 0)]
    >>> astar.search()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3),
     (4, 3), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6)]
    """

    def __init__(self, start: TPosition, goal: TPosition):
        logger.error(">>> Entering __init__(start=%s,goal=%s)", start, goal, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 99999, None)
        logger.error("__init__(start=%s,goal=%s): self.target → %s", start, goal, self.target, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})

        self.open_nodes = [self.start]
        logger.debug("__init__(self=%s,start=%s,goal=%s): self.open_nodes → %s", self, start, goal, self.open_nodes, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.closed_nodes: list[Node] = []

        logger.warning("<<< Exiting __init__(start=%s,goal=%s)", start, goal, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.reached = False
        logger.debug("__init__(self=%s,start=%s,goal=%s): self.reached → %s", self, start, goal, self.reached, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})

    def search(self) -> list[TPosition]:
        logger.error(">>> Entering search()", extra={"event.action": "search"})
        while self.open_nodes:
            # Open Nodes are sorted using __lt__
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)
            logger.error("search(): current_node → %s", current_node, extra={"event.action": "search"})

            if current_node.pos == self.target.pos:
                return self.retrace_path(current_node)

            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)

            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue

                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)
                else:
                    # retrieve the best current path
                    better_node = self.open_nodes.pop(self.open_nodes.index(child_node))

                    if child_node.g_cost < better_node.g_cost:
                        self.open_nodes.append(child_node)
                    else:
                        self.open_nodes.append(better_node)

        logger.warning("<<< Exiting search()", extra={"event.action": "search"})
        return [self.start.pos]

    def get_successors(self, parent: Node) -> list[Node]:
        """
        Returns a list of successors (both in the grid and free spaces)
        """
        logger.error(">>> Entering get_successors(parent=%s)", parent, extra={"event.action": "get_successors"})
        successors = []
        for action in delta:
            pos_x = parent.pos_x + action[1]
            pos_y = parent.pos_y + action[0]
            if not (0 <= pos_x <= len(grid[0]) - 1 and 0 <= pos_y <= len(grid) - 1):
                continue

            if grid[pos_y][pos_x] != 0:
                continue

            successors.append(
                Node(
                    pos_x,
                    pos_y,
                    self.target.pos_y,
                    self.target.pos_x,
                    parent.g_cost + 1,
                    parent,
                )
            )
        logger.warning("<<< Exiting get_successors(parent=%s)", parent, extra={"event.action": "get_successors"})
        return successors

    def retrace_path(self, node: Node | None) -> list[TPosition]:
        """
        Retrace the path from parents to parents until start node
        """
        logger.error(">>> Entering retrace_path(node=%s)", node, extra={"event.action": "retrace_path", "logrite.node": node})
        current_node = node
        path = []
        while current_node is not None:
            path.append((current_node.pos_y, current_node.pos_x))
            current_node = current_node.parent
        path.reverse()
        logger.warning("<<< Exiting retrace_path(node=%s)", node, extra={"event.action": "retrace_path", "logrite.node": node})
        return path


class BidirectionalAStar:
    """
    >>> bd_astar = BidirectionalAStar((0, 0), (len(grid) - 1, len(grid[0]) - 1))
    >>> bd_astar.fwd_astar.start.pos == bd_astar.bwd_astar.target.pos
    True
    >>> bd_astar.retrace_bidirectional_path(bd_astar.fwd_astar.start,
    ...                                     bd_astar.bwd_astar.start)
    [(0, 0)]
    >>> bd_astar.search()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4),
     (2, 5), (3, 5), (4, 5), (5, 5), (5, 6), (6, 6)]
    """

    def __init__(self, start: TPosition, goal: TPosition) -> None:
        self.fwd_astar = AStar(start, goal)
        logger.error("__init__(start=%s,goal=%s): self.fwd_astar → %s", start, goal, self.fwd_astar, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.bwd_astar = AStar(goal, start)
        logger.error("__init__(start=%s,goal=%s): self.bwd_astar → %s", start, goal, self.bwd_astar, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.reached = False

    def search(self) -> list[TPosition]:
        while self.fwd_astar.open_nodes or self.bwd_astar.open_nodes:
            self.fwd_astar.open_nodes.sort()
            self.bwd_astar.open_nodes.sort()
            current_fwd_node = self.fwd_astar.open_nodes.pop(0)
            logger.error("search(): current_fwd_node → %s", current_fwd_node, extra={"event.action": "search"})
            current_bwd_node = self.bwd_astar.open_nodes.pop(0)
            logger.error("search(): current_bwd_node → %s", current_bwd_node, extra={"event.action": "search"})

            if current_bwd_node.pos == current_fwd_node.pos:
                return self.retrace_bidirectional_path(
                    current_fwd_node, current_bwd_node
                )

            self.fwd_astar.closed_nodes.append(current_fwd_node)
            self.bwd_astar.closed_nodes.append(current_bwd_node)

            self.fwd_astar.target = current_bwd_node
            self.bwd_astar.target = current_fwd_node

            successors = {
                self.fwd_astar: self.fwd_astar.get_successors(current_fwd_node),
                self.bwd_astar: self.bwd_astar.get_successors(current_bwd_node),
            }

            for astar in [self.fwd_astar, self.bwd_astar]:
                for child_node in successors[astar]:
                    if child_node in astar.closed_nodes:
                        continue

                    if child_node not in astar.open_nodes:
                        astar.open_nodes.append(child_node)
                    else:
                        # retrieve the best current path
                        better_node = astar.open_nodes.pop(
                            astar.open_nodes.index(child_node)
                        )

                        if child_node.g_cost < better_node.g_cost:
                            astar.open_nodes.append(child_node)
                        else:
                            astar.open_nodes.append(better_node)

        return [self.fwd_astar.start.pos]

    def retrace_bidirectional_path(
        self, fwd_node: Node, bwd_node: Node
    ) -> list[TPosition]:
        logger.error(">>> Entering retrace_bidirectional_path(fwd_node=%s,bwd_node=%s)", fwd_node, bwd_node, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        fwd_path = self.fwd_astar.retrace_path(fwd_node)
        logger.error("retrace_bidirectional_path(fwd_node=%s,bwd_node=%s): fwd_path → %s", fwd_node, bwd_node, fwd_path, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        bwd_path = self.bwd_astar.retrace_path(bwd_node)
        logger.error("retrace_bidirectional_path(fwd_node=%s,bwd_node=%s): bwd_path → %s", fwd_node, bwd_node, bwd_path, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        bwd_path.pop()
        bwd_path.reverse()
        path = fwd_path + bwd_path
        logger.warning("<<< Exiting retrace_bidirectional_path(fwd_node=%s,bwd_node=%s)", fwd_node, bwd_node, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        return path


if __name__ == "__main__":
    # all coordinates are given in format [y,x]
    init = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    for elem in grid:
        print(elem)

    start_time = time.time()
    a_star = AStar(init, goal)
    path = a_star.search()
    end_time = time.time() - start_time
    print(f"AStar execution time = {end_time:f} seconds")

    bd_start_time = time.time()
    bidir_astar = BidirectionalAStar(init, goal)
    bd_end_time = time.time() - bd_start_time
    print(f"BidirectionalAStar execution time = {bd_end_time:f} seconds")
