"""
https://en.wikipedia.org/wiki/Bidirectional_search
"""

from __future__ import annotations

import time
import logging
logger = logging.getLogger(__name__)

Path = list[tuple[int, int]]

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


class Node:
    def __init__(
        self, pos_x: int, pos_y: int, goal_x: int, goal_y: int, parent: Node | None
    ):
        logger.error(">>> Entering __init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s)", pos_x, pos_y, goal_x, goal_y, parent, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})
        self.pos_x = pos_x
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s): self.pos_x → %s", self, pos_x, pos_y, goal_x, goal_y, parent, self.pos_x, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})
        self.pos_y = pos_y
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s): self.pos_y → %s", self, pos_x, pos_y, goal_x, goal_y, parent, self.pos_y, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})
        self.pos = (pos_y, pos_x)
        logger.error("__init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s): self.pos → %s", pos_x, pos_y, goal_x, goal_y, parent, self.pos, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})
        self.goal_x = goal_x
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s): self.goal_x → %s", self, pos_x, pos_y, goal_x, goal_y, parent, self.goal_x, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})
        self.goal_y = goal_y
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s): self.goal_y → %s", self, pos_x, pos_y, goal_x, goal_y, parent, self.goal_y, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})
        self.parent = parent
        logger.debug("__init__(self=%s,pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s): self.parent → %s", self, pos_x, pos_y, goal_x, goal_y, parent, self.parent, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})

        logger.warning("<<< Exiting __init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,parent=%s)", pos_x, pos_y, goal_x, goal_y, parent, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y})

class BreadthFirstSearch:
    """
    # Comment out slow pytests...
    # 9.15s call     graphs/bidirectional_breadth_first_search.py:: \
    #                graphs.bidirectional_breadth_first_search.BreadthFirstSearch
    # >>> bfs = BreadthFirstSearch((0, 0), (len(grid) - 1, len(grid[0]) - 1))
    # >>> (bfs.start.pos_y + delta[3][0], bfs.start.pos_x + delta[3][1])
    (0, 1)
    # >>> [x.pos for x in bfs.get_successors(bfs.start)]
    [(1, 0), (0, 1)]
    # >>> (bfs.start.pos_y + delta[2][0], bfs.start.pos_x + delta[2][1])
    (1, 0)
    # >>> bfs.retrace_path(bfs.start)
    [(0, 0)]
    # >>> bfs.search()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1),
     (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 5), (6, 6)]
    """

    def __init__(self, start: tuple[int, int], goal: tuple[int, int]):
        logger.error(">>> Entering __init__(start=%s,goal=%s)", start, goal, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.start = Node(start[1], start[0], goal[1], goal[0], None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], None)
        logger.error("__init__(start=%s,goal=%s): self.target → %s", start, goal, self.target, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})

        logger.warning("<<< Exiting __init__(start=%s,goal=%s)", start, goal, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.node_queue = [self.start]
        logger.debug("__init__(self=%s,start=%s,goal=%s): self.node_queue → %s", self, start, goal, self.node_queue, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.reached = False
        logger.debug("__init__(self=%s,start=%s,goal=%s): self.reached → %s", self, start, goal, self.reached, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})

    def search(self) -> Path | None:
        logger.error(">>> Entering search()", extra={"event.action": "search"})
        while self.node_queue:
            current_node = self.node_queue.pop(0)
            logger.error("search(): current_node → %s", current_node, extra={"event.action": "search"})

            if current_node.pos == self.target.pos:
                self.reached = True
                logger.debug("search(self=%s): self.reached → %s", self, self.reached, extra={"event.action": "search"})
                return self.retrace_path(current_node)

            successors = self.get_successors(current_node)

            for node in successors:
                self.node_queue.append(node)

        if not self.reached:
            return [self.start.pos]
        logger.warning("<<< Exiting search()", extra={"event.action": "search"})
        return None

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
                Node(pos_x, pos_y, self.target.pos_y, self.target.pos_x, parent)
            )
        logger.warning("<<< Exiting get_successors(parent=%s)", parent, extra={"event.action": "get_successors"})
        return successors

    def retrace_path(self, node: Node | None) -> Path:
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


class BidirectionalBreadthFirstSearch:
    """
    >>> bd_bfs = BidirectionalBreadthFirstSearch((0, 0), (len(grid) - 1,
    ...                                                   len(grid[0]) - 1))
    >>> bd_bfs.fwd_bfs.start.pos == bd_bfs.bwd_bfs.target.pos
    True
    >>> bd_bfs.retrace_bidirectional_path(bd_bfs.fwd_bfs.start,
    ...                                     bd_bfs.bwd_bfs.start)
    [(0, 0)]
    >>> bd_bfs.search()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3),
     (2, 4), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (6, 6)]
    """

    def __init__(self, start, goal):
        self.fwd_bfs = BreadthFirstSearch(start, goal)
        logger.error("__init__(start=%s,goal=%s): self.fwd_bfs → %s", start, goal, self.fwd_bfs, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.bwd_bfs = BreadthFirstSearch(goal, start)
        logger.error("__init__(start=%s,goal=%s): self.bwd_bfs → %s", start, goal, self.bwd_bfs, extra={"event.action": "__init__", "logrite.start": start, "logrite.goal": goal})
        self.reached = False

    def search(self) -> Path | None:
        while self.fwd_bfs.node_queue or self.bwd_bfs.node_queue:
            current_fwd_node = self.fwd_bfs.node_queue.pop(0)
            logger.error("search(): current_fwd_node → %s", current_fwd_node, extra={"event.action": "search"})
            current_bwd_node = self.bwd_bfs.node_queue.pop(0)
            logger.error("search(): current_bwd_node → %s", current_bwd_node, extra={"event.action": "search"})

            if current_bwd_node.pos == current_fwd_node.pos:
                self.reached = True
                return self.retrace_bidirectional_path(
                    current_fwd_node, current_bwd_node
                )

            self.fwd_bfs.target = current_bwd_node
            self.bwd_bfs.target = current_fwd_node

            successors = {
                self.fwd_bfs: self.fwd_bfs.get_successors(current_fwd_node),
                self.bwd_bfs: self.bwd_bfs.get_successors(current_bwd_node),
            }

            for bfs in [self.fwd_bfs, self.bwd_bfs]:
                for node in successors[bfs]:
                    bfs.node_queue.append(node)

        if not self.reached:
            return [self.fwd_bfs.start.pos]
        return None

    def retrace_bidirectional_path(self, fwd_node: Node, bwd_node: Node) -> Path:
        logger.error(">>> Entering retrace_bidirectional_path(fwd_node=%s,bwd_node=%s)", fwd_node, bwd_node, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        fwd_path = self.fwd_bfs.retrace_path(fwd_node)
        logger.error("retrace_bidirectional_path(fwd_node=%s,bwd_node=%s): fwd_path → %s", fwd_node, bwd_node, fwd_path, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        bwd_path = self.bwd_bfs.retrace_path(bwd_node)
        logger.error("retrace_bidirectional_path(fwd_node=%s,bwd_node=%s): bwd_path → %s", fwd_node, bwd_node, bwd_path, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        bwd_path.pop()
        bwd_path.reverse()
        path = fwd_path + bwd_path
        logger.warning("<<< Exiting retrace_bidirectional_path(fwd_node=%s,bwd_node=%s)", fwd_node, bwd_node, extra={"event.action": "retrace_bidirectional_path", "logrite.fwd_node": fwd_node, "logrite.bwd_node": bwd_node})
        return path


if __name__ == "__main__":
    # all coordinates are given in format [y,x]
    import doctest

    doctest.testmod()
    init = (0, 0)
    goal = (len(grid) - 1, len(grid[0]) - 1)
    for elem in grid:
        print(elem)

    start_bfs_time = time.time()
    bfs = BreadthFirstSearch(init, goal)
    path = bfs.search()
    bfs_time = time.time() - start_bfs_time

    print("Unidirectional BFS computation time : ", bfs_time)

    start_bd_bfs_time = time.time()
    bd_bfs = BidirectionalBreadthFirstSearch(init, goal)
    bd_path = bd_bfs.search()
    bd_bfs_time = time.time() - start_bd_bfs_time

    print("Bidirectional BFS computation time : ", bd_bfs_time)
