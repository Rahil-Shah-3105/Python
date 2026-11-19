from __future__ import annotations

from typing import Any
import logging
logger = logging.getLogger(__name__)


class ContainsLoopError(Exception):
    pass


class Node:
    def __init__(self, data: Any) -> None:
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data: Any = data
        self.next_node: Node | None = None
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

    def __iter__(self):
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        node = self
        visited = set()
        logger.error("__iter__(): visited → %s", visited, extra={"event.action": "__iter__"})
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.add(node)
            yield node.data
            node = node.next_node
            logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})

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
        logger.error(">>> Entering has_loop()", extra={"event.action": "has_loop"})
        try:
            list(self)
            return False
        except ContainsLoopError:
            logger.error("Exception in has_loop()", exc_info=True, extra={"event.action": "has_loop", "event.category": "process"})
            logger.warning("<<< Exiting has_loop()", extra={"event.action": "has_loop"})
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
