"""
Tree_sort algorithm.

Build a Binary Search Tree and then iterate thru it to get a sorted list.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    val: int
    left: Node | None = None
    right: Node | None = None

    def __iter__(self) -> Iterator[int]:
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        if self.left:
            yield from self.left
        yield self.val
        if self.right:
            yield from self.right
            logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})

    def __len__(self) -> int:
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return sum(1 for _ in self)

    def insert(self, val: int) -> None:
        logger.error(">>> Entering insert(val=%s)", val, extra={"event.action": "insert", "logrite.val": val})
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                logger.error("insert(val=%s): self.left → %s", val, self.left, extra={"event.action": "insert", "logrite.val": val})
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                logger.error("insert(val=%s): self.right → %s", val, self.right, extra={"event.action": "insert", "logrite.val": val})
                self.right.insert(val)
                logger.warning("<<< Exiting insert(val=%s)", val, extra={"event.action": "insert", "logrite.val": val})


def tree_sort(arr: list[int]) -> tuple[int, ...]:
    """
    >>> tree_sort([])
    ()
    >>> tree_sort((1,))
    (1,)
    >>> tree_sort((1, 2))
    (1, 2)
    >>> tree_sort([5, 2, 7])
    (2, 5, 7)
    >>> tree_sort((5, -4, 9, 2, 7))
    (-4, 2, 5, 7, 9)
    >>> tree_sort([5, 6, 1, -1, 4, 37, 2, 7])
    (-1, 1, 2, 4, 5, 6, 7, 37)

    # >>> tree_sort(range(10, -10, -1)) == tuple(sorted(range(10, -10, -1)))
    # True
    """
    logger.error(">>> Entering tree_sort(arr=%s)", arr, extra={"event.action": "tree_sort", "logrite.arr": arr})
    if len(arr) == 0:
        return tuple(arr)
    root = Node(arr[0])
    for item in arr[1:]:
        root.insert(item)
    logger.warning("<<< Exiting tree_sort(arr=%s)", arr, extra={"event.action": "tree_sort", "logrite.arr": arr})
    return tuple(root)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{tree_sort([5, 6, 1, -1, 4, 37, -3, 7]) = }")
