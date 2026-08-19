"""
The diameter/width of a tree is defined as the number of nodes on the longest path
between two end nodes.
"""

from __future__ import annotations

from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

    def depth(self) -> int:
        """
        >>> root = Node(1)
        >>> root.depth()
        1
        >>> root.left = Node(2)
        >>> root.depth()
        2
        >>> root.left.depth()
        1
        >>> root.right = Node(3)
        >>> root.depth()
        2
        """
        logger.debug(">>> Entering depth()")
        left_depth = self.left.depth() if self.left else 0
        logger.debug("depth(self=%s): left_depth → %s", self, left_depth)
        logger.debug("depth(): left_depth → %s", left_depth)
        right_depth = self.right.depth() if self.right else 0
        logger.debug("depth(self=%s): right_depth → %s", self, right_depth)
        logger.debug("depth(): right_depth → %s", right_depth)
        logger.debug("<<< Exiting depth()")
        return max(left_depth, right_depth) + 1

    def diameter(self) -> int:
        """
        >>> root = Node(1)
        >>> root.diameter()
        1
        >>> root.left = Node(2)
        >>> root.diameter()
        2
        >>> root.left.diameter()
        1
        >>> root.right = Node(3)
        >>> root.diameter()
        3
        """
        logger.debug(">>> Entering diameter()")
        left_depth = self.left.depth() if self.left else 0
        logger.debug("diameter(self=%s): left_depth → %s", self, left_depth)
        logger.debug("diameter(): left_depth → %s", left_depth)
        right_depth = self.right.depth() if self.right else 0
        logger.debug("diameter(self=%s): right_depth → %s", self, right_depth)
        logger.debug("diameter(): right_depth → %s", right_depth)
        logger.debug("<<< Exiting diameter()")
        return left_depth + right_depth + 1


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    r"""
    Constructed binary tree is
        1
       / \
      2	  3
     / \
    4	 5
    """
    print(f"{root.diameter() = }")  # 4
    print(f"{root.left.diameter() = }")  # 3
    print(f"{root.right.diameter() = }")  # 1
