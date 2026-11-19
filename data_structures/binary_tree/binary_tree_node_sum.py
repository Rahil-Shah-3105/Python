"""
Sum of all nodes in a binary tree.

Python implementation:
    O(n) time complexity - Recurses through :meth:`depth_first_search`
                            with each element.
    O(n) space complexity - At any point in time maximum number of stack
                            frames that could be in memory is `n`
"""

from __future__ import annotations

from collections.abc import Iterator
import logging
logger = logging.getLogger(__name__)


class Node:
    """
    A Node has a value variable and pointers to Nodes to its left and right.
    """

    def __init__(self, value: int) -> None:
        logger.error(">>> Entering __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})
        self.value = value
        logger.debug("__init__(self=%s,value=%s): self.value → %s", self, value, self.value, extra={"event.action": "__init__", "logrite.value": value})
        self.left: Node | None = None
        self.right: Node | None = None
        logger.warning("<<< Exiting __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})


class BinaryTreeNodeSum:
    r"""
    The below tree looks like this
        10
       /  \
      5   -3
     /    / \
    12   8  0

    >>> tree = Node(10)
    >>> sum(BinaryTreeNodeSum(tree))
    10

    >>> tree.left = Node(5)
    >>> sum(BinaryTreeNodeSum(tree))
    15

    >>> tree.right = Node(-3)
    >>> sum(BinaryTreeNodeSum(tree))
    12

    >>> tree.left.left = Node(12)
    >>> sum(BinaryTreeNodeSum(tree))
    24

    >>> tree.right.left = Node(8)
    >>> tree.right.right = Node(0)
    >>> sum(BinaryTreeNodeSum(tree))
    32
    """

    def __init__(self, tree: Node) -> None:
        logger.error(">>> Entering __init__(tree=%s)", tree, extra={"event.action": "__init__", "logrite.tree": tree})
        self.tree = tree
        logger.warning("<<< Exiting __init__(tree=%s)", tree, extra={"event.action": "__init__", "logrite.tree": tree})
        logger.debug("__init__(self=%s,tree=%s): self.tree → %s", self, tree, self.tree, extra={"event.action": "__init__", "logrite.tree": tree})

    def depth_first_search(self, node: Node | None) -> int:
        logger.error(">>> Entering depth_first_search(node=%s)", node, extra={"event.action": "depth_first_search", "logrite.node": node})
        if node is None:
            logger.warning("<<< Exiting depth_first_search(node=%s)", node, extra={"event.action": "depth_first_search", "logrite.node": node})
            return 0
        return node.value + (
            self.depth_first_search(node.left) + self.depth_first_search(node.right)
        )

    def __iter__(self) -> Iterator[int]:
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        yield self.depth_first_search(self.tree)
        logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
