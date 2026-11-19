"""
Given the root of a binary tree and an integer target,
find the number of paths where the sum of the values
along the path equals target.


Leetcode reference: https://leetcode.com/problems/path-sum-iii/
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


class Node:
    """
    A Node has value variable and pointers to Nodes to its left and right.
    """

    def __init__(self, value: int) -> None:
        logger.error(">>> Entering __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})
        self.value = value
        logger.debug("__init__(self=%s,value=%s): self.value → %s", self, value, self.value, extra={"event.action": "__init__", "logrite.value": value})
        self.left: Node | None = None
        self.right: Node | None = None
        logger.warning("<<< Exiting __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})


class BinaryTreePathSum:
    r"""
    The below tree looks like this
          10
         /  \
        5   -3
       / \    \
      3   2    11
     / \   \
    3  -2   1


    >>> tree = Node(10)
    >>> tree.left = Node(5)
    >>> tree.right = Node(-3)
    >>> tree.left.left = Node(3)
    >>> tree.left.right = Node(2)
    >>> tree.right.right = Node(11)
    >>> tree.left.left.left = Node(3)
    >>> tree.left.left.right = Node(-2)
    >>> tree.left.right.right = Node(1)

    >>> BinaryTreePathSum().path_sum(tree, 8)
    3
    >>> BinaryTreePathSum().path_sum(tree, 7)
    2
    >>> tree.right.right = Node(10)
    >>> BinaryTreePathSum().path_sum(tree, 8)
    2
    >>> BinaryTreePathSum().path_sum(None, 0)
    0
    >>> BinaryTreePathSum().path_sum(tree, 0)
    0

    The second tree looks like this
          0
         / \
        5   5

    >>> tree2 = Node(0)
    >>> tree2.left = Node(5)
    >>> tree2.right = Node(5)

    >>> BinaryTreePathSum().path_sum(tree2, 5)
    4
    >>> BinaryTreePathSum().path_sum(tree2, -1)
    0
    >>> BinaryTreePathSum().path_sum(tree2, 0)
    1
    """

    target: int

    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.paths = 0
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.paths → %s", self, self.paths, extra={"event.action": "__init__"})

    def depth_first_search(self, node: Node | None, path_sum: int) -> None:
        logger.error(">>> Entering depth_first_search(node=%s,path_sum=%s)", node, path_sum, extra={"event.action": "depth_first_search", "logrite.node": node, "logrite.path_sum": path_sum})
        if node is None:
            logger.warning("<<< Exiting depth_first_search(node=%s,path_sum=%s)", node, path_sum, extra={"event.action": "depth_first_search", "logrite.node": node, "logrite.path_sum": path_sum})
            return

        if path_sum == self.target:
            self.paths += 1

        if node.left:
            self.depth_first_search(node.left, path_sum + node.left.value)
        if node.right:
            self.depth_first_search(node.right, path_sum + node.right.value)

    def path_sum(self, node: Node | None, target: int | None = None) -> int:
        logger.error(">>> Entering path_sum(node=%s,target=%s)", node, target, extra={"event.action": "path_sum", "logrite.node": node, "logrite.target": target})
        if node is None:
            return 0
        if target is not None:
            self.target = target
            logger.debug("path_sum(self=%s,node=%s,target=%s): self.target → %s", self, node, target, self.target, extra={"event.action": "path_sum", "logrite.node": node, "logrite.target": target})

        self.depth_first_search(node, node.value)
        self.path_sum(node.left)
        self.path_sum(node.right)

        logger.warning("<<< Exiting path_sum(node=%s,target=%s)", node, target, extra={"event.action": "path_sum", "logrite.node": node, "logrite.target": target})
        return self.paths


if __name__ == "__main__":
    import doctest

    doctest.testmod()
