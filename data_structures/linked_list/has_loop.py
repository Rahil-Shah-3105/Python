from __future__ import annotations

from typing import Any
import logging
logger = logging.getLogger(__name__)


class ContainsLoopError(Exception):
    pass


class Node:
    def __init__(self, data: Any) -> None:
        logger.debug(">>> Entering __init__(data=%s)", data)
        self.data: Any = data
        self.next_node: Node | None = None
        logger.debug("<<< Exiting __init__(data=%s)", data)

    def __iter__(self):
        logger.debug(">>> Entering __iter__()")
        node = self
        logger.debug("__iter__(self=%s): node → %s", self, node)
        visited = set()
        logger.debug("__iter__(): visited → %s", visited)
        logger.debug("__iter__(self=%s): visited → %s", self, visited)
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.add(node)
            yield node.data
            logger.debug("<<< Exiting __iter__()")
            node = node.next_node

    @property
    def has_loop(self) -> bool:
        """
        A loop is when the exact same Node appears more than once in a linked list.
        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.next_node.next_node = Node(4)
        >>> root_node.has_loop
        False
        >>> root_node.next_node.next_node.next_node = root_node.next_node
        >>> root_node.has_loop
        True
        """
        logger.debug(">>> Entering has_loop()")
        try:
            list(self)
            return False
        except ContainsLoopError:
            logger.error("Exception in has_loop()", exc_info=True)
            logger.debug("<<< Exiting has_loop()")
            return True


if __name__ == "__main__":
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)
    print(root_node.has_loop)  # False
    root_node.next_node.next_node.next_node = root_node.next_node
    print(root_node.has_loop)  # True

    root_node = Node(5)
    root_node.next_node = Node(6)
    root_node.next_node.next_node = Node(5)
    root_node.next_node.next_node.next_node = Node(6)
    print(root_node.has_loop)  # False

    root_node = Node(1)
    print(root_node.has_loop)  # False
