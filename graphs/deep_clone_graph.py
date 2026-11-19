"""
LeetCode 133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its
neighbors.
"""

from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    value: int = 0
    neighbors: list["Node"] | None = None

    def __post_init__(self) -> None:
        """
        >>> Node(3).neighbors
        []
        """
        logger.error(">>> Entering __post_init__()", extra={"event.action": "__post_init__"})
        self.neighbors = self.neighbors or []
        logger.warning("<<< Exiting __post_init__()", extra={"event.action": "__post_init__"})
        logger.debug("__post_init__(self=%s): self.neighbors → %s", self, self.neighbors, extra={"event.action": "__post_init__"})

    def __hash__(self) -> int:
        """
        >>> hash(Node(3)) != 0
        True
        """
        logger.error(">>> Entering __hash__()", extra={"event.action": "__hash__"})
        logger.warning("<<< Exiting __hash__()", extra={"event.action": "__hash__"})
        return id(self)


def clone_graph(node: Node | None) -> Node | None:
    """
    This function returns a clone of a connected undirected graph.
    >>> clone_graph(Node(1))
    Node(value=1, neighbors=[])
    >>> clone_graph(Node(1, [Node(2)]))
    Node(value=1, neighbors=[Node(value=2, neighbors=[])])
    >>> clone_graph(None) is None
    True
    """
    logger.error(">>> Entering clone_graph(node=%s)", node, extra={"event.action": "clone_graph", "logrite.node": node})
    if not node:
        return None

    originals_to_clones = {}  # map nodes to clones

    stack = [node]

    while stack:
        original = stack.pop()

        if original in originals_to_clones:
            continue

        originals_to_clones[original] = Node(original.value)

        stack.extend(original.neighbors or [])

    for original, clone in originals_to_clones.items():
        for neighbor in original.neighbors or []:
            cloned_neighbor = originals_to_clones[neighbor]

            if not clone.neighbors:
                clone.neighbors = []
                logger.debug("clone_graph(node=%s): clone.neighbors → %s", node, clone.neighbors, extra={"event.action": "clone_graph", "logrite.node": node})

            clone.neighbors.append(cloned_neighbor)

    logger.warning("<<< Exiting clone_graph(node=%s)", node, extra={"event.action": "clone_graph", "logrite.node": node})
    return originals_to_clones[node]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
