from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        if self.left:
            yield from self.left
        yield self.data
        if self.right:
            yield from self.right
            logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})

    def __len__(self) -> int:
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return sum(1 for _ in self)

    def is_full(self) -> bool:
        logger.error(">>> Entering is_full()", extra={"event.action": "is_full"})
        if not self or (not self.left and not self.right):
            return True
        if self.left and self.right:
            return self.left.is_full() and self.right.is_full()
        logger.warning("<<< Exiting is_full()", extra={"event.action": "is_full"})
        return False


@dataclass
class BinaryTree:
    root: Node

    def __iter__(self) -> Iterator[int]:
        return iter(self.root)

    def __len__(self) -> int:
        return len(self.root)

    @classmethod
    def small_tree(cls) -> BinaryTree:
        """
        Return a small binary tree with 3 nodes.
        >>> binary_tree = BinaryTree.small_tree()
        >>> len(binary_tree)
        3
        >>> list(binary_tree)
        [1, 2, 3]
        """
        logger.error(">>> Entering small_tree()", extra={"event.action": "small_tree"})
        binary_tree = BinaryTree(Node(2))
        logger.error("small_tree(): binary_tree → %s", binary_tree, extra={"event.action": "small_tree"})
        binary_tree.root.left = Node(1)
        binary_tree.root.right = Node(3)
        logger.warning("<<< Exiting small_tree()", extra={"event.action": "small_tree"})
        return binary_tree

    @classmethod
    def medium_tree(cls) -> BinaryTree:
        """
        Return a medium binary tree with 3 nodes.
        >>> binary_tree = BinaryTree.medium_tree()
        >>> len(binary_tree)
        7
        >>> list(binary_tree)
        [1, 2, 3, 4, 5, 6, 7]
        """
        logger.error(">>> Entering medium_tree()", extra={"event.action": "medium_tree"})
        binary_tree = BinaryTree(Node(4))
        logger.error("medium_tree(): binary_tree → %s", binary_tree, extra={"event.action": "medium_tree"})
        binary_tree.root.left = two = Node(2)
        two.left = Node(1)
        two.right = Node(3)
        binary_tree.root.right = five = Node(5)
        five.right = six = Node(6)
        six.right = Node(7)
        logger.warning("<<< Exiting medium_tree()", extra={"event.action": "medium_tree"})
        return binary_tree

    def depth(self) -> int:
        """
        Returns the depth of the tree

        >>> BinaryTree(Node(1)).depth()
        1
        >>> BinaryTree.small_tree().depth()
        2
        >>> BinaryTree.medium_tree().depth()
        4
        """
        logger.error(">>> Entering depth()", extra={"event.action": "depth"})
        logger.warning("<<< Exiting depth()", extra={"event.action": "depth"})
        return self._depth(self.root)

    def _depth(self, node: Node | None) -> int:
        logger.error(">>> Entering _depth(node=%s)", node, extra={"event.action": "_depth", "logrite.node": node})
        if not node:
            return 0
        logger.warning("<<< Exiting _depth(node=%s)", node, extra={"event.action": "_depth", "logrite.node": node})
        return 1 + max(self._depth(node.left), self._depth(node.right))

    def is_full(self) -> bool:
        """
        Returns True if the tree is full

        >>> BinaryTree(Node(1)).is_full()
        True
        >>> BinaryTree.small_tree().is_full()
        True
        >>> BinaryTree.medium_tree().is_full()
        False
        """
        return self.root.is_full()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
