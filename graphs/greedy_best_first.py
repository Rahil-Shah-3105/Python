"""
https://en.wikipedia.org/wiki/Best-first_search#Greedy_BFS
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)

Path = list[tuple[int, int]]

# 0's are free path whereas 1's are obstacles
TEST_GRIDS = [
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
    ],
    [
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
    ],
    [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
    ],
]

delta = ([-1, 0], [0, -1], [1, 0], [0, 1])  # up, left, down, right


class Node:
    """
    >>> k = Node(0, 0, 4, 5, 0, None)
    >>> k.calculate_heuristic()
    9
    >>> n = Node(1, 4, 3, 4, 2, None)
    >>> n.calculate_heuristic()
    2
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
        g_cost: float,
        parent: Node | None,
    ):
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
        self.f_cost = self.calculate_heuristic()
        logger.error("__init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s): self.f_cost → %s", pos_x, pos_y, goal_x, goal_y, g_cost, parent, self.f_cost, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})
        logger.warning("<<< Exiting __init__(pos_x=%s,pos_y=%s,goal_x=%s,goal_y=%s,g_cost=%s,parent=%s)", pos_x, pos_y, goal_x, goal_y, g_cost, parent, extra={"event.action": "__init__", "logrite.pos_x": pos_x, "logrite.pos_y": pos_y, "logrite.goal_x": goal_x, "logrite.goal_y": goal_y, "logrite.g_cost": g_cost})

    def calculate_heuristic(self) -> float:
        """
        The heuristic here is the Manhattan Distance
        Could elaborate to offer more than one choice
        """
        logger.error(">>> Entering calculate_heuristic()", extra={"event.action": "calculate_heuristic"})
        dx = abs(self.pos_x - self.goal_x)
        logger.error("calculate_heuristic(): dx → %s", dx, extra={"event.action": "calculate_heuristic"})
        dy = abs(self.pos_y - self.goal_y)
        logger.error("calculate_heuristic(): dy → %s", dy, extra={"event.action": "calculate_heuristic"})
        logger.warning("<<< Exiting calculate_heuristic()", extra={"event.action": "calculate_heuristic"})
        return dx + dy

    def __lt__(self, other) -> bool:
        logger.error(">>> Entering __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        logger.warning("<<< Exiting __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        return self.f_cost < other.f_cost

    def __eq__(self, other) -> bool:
        logger.error(">>> Entering __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        logger.warning("<<< Exiting __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        return self.pos == other.pos


class GreedyBestFirst:
    """
    >>> grid = TEST_GRIDS[2]
    >>> gbf = GreedyBestFirst(grid, (0, 0), (len(grid) - 1, len(grid[0]) - 1))
    >>> [x.pos for x in gbf.get_successors(gbf.start)]
    [(1, 0), (0, 1)]
    >>> (gbf.start.pos_y + delta[3][0], gbf.start.pos_x + delta[3][1])
    (0, 1)
    >>> (gbf.start.pos_y + delta[2][0], gbf.start.pos_x + delta[2][1])
    (1, 0)
    >>> gbf.retrace_path(gbf.start)
    [(0, 0)]
    >>> gbf.search()  # doctest: +NORMALIZE_WHITESPACE
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3),
     (4, 4)]
    """

    def __init__(
        self, grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]
    ):
        logger.error(">>> Entering __init__(grid=%s,start=%s,goal=%s)", grid, start, goal, extra={"event.action": "__init__", "logrite.grid": grid, "logrite.start": start, "logrite.goal": goal})
        self.grid = grid
        logger.debug("__init__(self=%s,grid=%s,start=%s,goal=%s): self.grid → %s", self, grid, start, goal, self.grid, extra={"event.action": "__init__", "logrite.grid": grid, "logrite.start": start, "logrite.goal": goal})
        self.start = Node(start[1], start[0], goal[1], goal[0], 0, None)
        self.target = Node(goal[1], goal[0], goal[1], goal[0], 99999, None)
        logger.error("__init__(grid=%s,start=%s,goal=%s): self.target → %s", grid, start, goal, self.target, extra={"event.action": "__init__", "logrite.grid": grid, "logrite.start": start, "logrite.goal": goal})

        self.open_nodes = [self.start]
        logger.debug("__init__(self=%s,grid=%s,start=%s,goal=%s): self.open_nodes → %s", self, grid, start, goal, self.open_nodes, extra={"event.action": "__init__", "logrite.grid": grid, "logrite.start": start, "logrite.goal": goal})
        self.closed_nodes: list[Node] = []

        logger.warning("<<< Exiting __init__(grid=%s,start=%s,goal=%s)", grid, start, goal, extra={"event.action": "__init__", "logrite.grid": grid, "logrite.start": start, "logrite.goal": goal})
        self.reached = False
        logger.debug("__init__(self=%s,grid=%s,start=%s,goal=%s): self.reached → %s", self, grid, start, goal, self.reached, extra={"event.action": "__init__", "logrite.grid": grid, "logrite.start": start, "logrite.goal": goal})

    def search(self) -> Path | None:
        """
        Search for the path,
        if a path is not found, only the starting position is returned
        """
        logger.error(">>> Entering search()", extra={"event.action": "search"})
        while self.open_nodes:
            # Open Nodes are sorted using __lt__
            self.open_nodes.sort()
            current_node = self.open_nodes.pop(0)
            logger.error("search(): current_node → %s", current_node, extra={"event.action": "search"})

            if current_node.pos == self.target.pos:
                self.reached = True
                logger.debug("search(self=%s): self.reached → %s", self, self.reached, extra={"event.action": "search"})
                return self.retrace_path(current_node)

            self.closed_nodes.append(current_node)
            successors = self.get_successors(current_node)

            for child_node in successors:
                if child_node in self.closed_nodes:
                    continue

                if child_node not in self.open_nodes:
                    self.open_nodes.append(child_node)

        if not self.reached:
            return [self.start.pos]
        logger.warning("<<< Exiting search()", extra={"event.action": "search"})
        return None

    def get_successors(self, parent: Node) -> list[Node]:
        """
        Returns a list of successors (both in the grid and free spaces)
        """
        logger.error(">>> Entering get_successors(parent=%s)", parent, extra={"event.action": "get_successors"})
        logger.warning("<<< Exiting get_successors(parent=%s)", parent, extra={"event.action": "get_successors"})
        return [
            Node(
                pos_x,
                pos_y,
                self.target.pos_x,
                self.target.pos_y,
                parent.g_cost + 1,
                parent,
            )
            for action in delta
            if (
                0 <= (pos_x := parent.pos_x + action[1]) < len(self.grid[0])
                and 0 <= (pos_y := parent.pos_y + action[0]) < len(self.grid)
                and self.grid[pos_y][pos_x] == 0
            )
        ]

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


if __name__ == "__main__":
    for idx, grid in enumerate(TEST_GRIDS):
        print(f"==grid-{idx + 1}==")

        init = (0, 0)
        goal = (len(grid) - 1, len(grid[0]) - 1)
        for elem in grid:
            print(elem)

        print("------")

        greedy_bf = GreedyBestFirst(grid, init, goal)
        path = greedy_bf.search()
        if path:
            for pos_x, pos_y in path:
                grid[pos_x][pos_y] = 2

            for elem in grid:
                print(elem)
