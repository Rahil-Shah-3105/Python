"""
Given the root of a binary tree, mirror the tree, and return its root.

Leetcode problem reference: https://leetcode.com/problems/mirror-binary-tree/
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    """
    A Node has value variable and pointers to Nodes to its left and right.
    """

    value: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        logger.debug(">>> Entering __iter__()")
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right
            logger.debug("<<< Exiting __iter__()")

    def __len__(self) -> int:
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return sum(1 for _ in self)

    def mirror(self) -> Node:
        """
        Mirror the binary tree rooted at this node by swapping left and right children.

        >>> tree = Node(0)
        >>> list(tree)
        [0]
        >>> list(tree.mirror())
        [0]
        >>> tree = Node(1, Node(0), Node(3, Node(2), Node(4, None, Node(5))))
        >>> tuple(tree)
        (0, 1, 2, 3, 4, 5)
        >>> tuple(tree.mirror())
        (5, 4, 3, 2, 1, 0)
        """
        logger.debug(">>> Entering mirror()")
        self.left, self.right = self.right, self.left
        if self.left:
            self.left.mirror()
        if self.right:
            self.right.mirror()
        logger.debug("<<< Exiting mirror()")
        return self


def make_tree_seven() -> Node:
    r"""
    Return a binary tree with 7 nodes that looks like this:
    ::

           1
         /   \
        2     3
       / \   / \
      4   5 6   7

    >>> tree_seven = make_tree_seven()
    >>> len(tree_seven)
    7
    >>> list(tree_seven)
    [4, 2, 5, 1, 6, 3, 7]
    """
    logger.debug(">>> Entering make_tree_seven()")
    tree = Node(1)
    logger.debug("make_tree_seven(): tree → %s", tree)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    logger.debug("<<< Exiting make_tree_seven()")
    return tree


def make_tree_nine() -> Node:
    r"""
    Return a binary tree with 9 nodes that looks like this:
    ::

            1
           / \
          2   3
         / \   \
        4   5   6
       / \   \
      7   8   9

    >>> tree_nine = make_tree_nine()
    >>> len(tree_nine)
    9
    >>> list(tree_nine)
    [7, 4, 8, 2, 5, 9, 1, 3, 6]
    """
    logger.debug(">>> Entering make_tree_nine()")
    tree = Node(1)
    logger.debug("make_tree_nine(): tree → %s", tree)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.right = Node(6)
    tree.left.left.left = Node(7)
    tree.left.left.right = Node(8)
    tree.left.right.right = Node(9)
    logger.debug("<<< Exiting make_tree_nine()")
    return tree


def main() -> None:
    r"""
    Mirror binary trees with the given root and returns the root

    >>> tree = make_tree_nine()
    >>> tuple(tree)
    (7, 4, 8, 2, 5, 9, 1, 3, 6)
    >>> tuple(tree.mirror())
    (6, 3, 1, 9, 5, 2, 8, 4, 7)

    nine_tree::

            1
           / \
          2   3
         / \   \
        4   5   6
       / \   \
      7   8   9

    The mirrored tree looks like this::

          1
         / \
        3   2
       /   / \
      6   5   4
         /   / \
        9   8   7
    """
    logger.debug(">>> Entering main()")
    trees = {"zero": Node(0), "seven": make_tree_seven(), "nine": make_tree_nine()}
    logger.debug("main(): trees → %s", trees)
    for name, tree in trees.items():
        print(f"      The {name} tree: {tuple(tree)}")
        # (0,)
        # (4, 2, 5, 1, 6, 3, 7)
        # (7, 4, 8, 2, 5, 9, 1, 3, 6)
        print(f"Mirror of {name} tree: {tuple(tree.mirror())}")
        logger.debug("<<< Exiting main()")
        # (0,)
        # (7, 3, 6, 1, 5, 2, 4)
        # (6, 3, 1, 9, 5, 2, 8, 4, 7)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
