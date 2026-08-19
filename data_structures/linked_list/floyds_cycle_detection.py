"""
Floyd's cycle detection algorithm is a popular algorithm used to detect cycles
in a linked list. It uses two pointers, a slow pointer and a fast pointer,
to traverse the linked list. The slow pointer moves one node at a time while the fast
pointer moves two nodes at a time. If there is a cycle in the linked list,
the fast pointer will eventually catch up to the slow pointer and they will
meet at the same node. If there is no cycle, the fast pointer will reach the end of
the linked list and the algorithm will terminate.

For more information: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
"""

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, Self
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    """
    A class representing a node in a singly linked list.
    """

    data: Any
    next_node: Self | None = None


@dataclass
class LinkedList:
    """
    A class representing a singly linked list.
    """

    head: Node | None = None

    def __iter__(self) -> Iterator:
        """
        Iterates through the linked list.

        Returns:
            Iterator: An iterator over the linked list.

        Examples:
        >>> linked_list = LinkedList()
        >>> list(linked_list)
        []
        >>> linked_list.add_node(1)
        >>> tuple(linked_list)
        (1,)
        """
        logger.debug(">>> Entering __iter__()")
        visited = []
        logger.debug("__iter__(self=%s): visited → %s", self, visited)
        node = self.head
        logger.debug("__iter__(self=%s): node → %s", self, node)
        while node:
            # Avoid infinite loop in there's a cycle
            if node in visited:
                logger.debug("<<< Exiting __iter__()")
                return
            visited.append(node)
            yield node.data
            node = node.next_node

    def add_node(self, data: Any) -> None:
        """
        Adds a new node to the end of the linked list.

        Args:
            data (Any): The data to be stored in the new node.

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.add_node(1)
        >>> linked_list.add_node(2)
        >>> linked_list.add_node(3)
        >>> linked_list.add_node(4)
        >>> tuple(linked_list)
        (1, 2, 3, 4)
        """
        logger.debug(">>> Entering add_node(data=%s)", data)
        new_node = Node(data)
        logger.debug("add_node(self=%s,data=%s): new_node → %s", self, data, new_node)
        logger.debug("add_node(data=%s): new_node → %s", data, new_node)

        if self.head is None:
            self.head = new_node
            logger.debug("add_node(self=%s,data=%s): self.head → %s", self, data, self.head)
            logger.debug("<<< Exiting add_node(data=%s)", data)
            return

        current_node = self.head
        logger.debug("add_node(self=%s,data=%s): current_node → %s", self, data, current_node)
        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = new_node
        logger.debug("add_node(self=%s,data=%s): current_node.next_node → %s", self, data, current_node.next_node)

    def detect_cycle(self) -> bool:
        """
        Detects if there is a cycle in the linked list using
        Floyd's cycle detection algorithm.

        Returns:
            bool: True if there is a cycle, False otherwise.

        Examples:
        >>> linked_list = LinkedList()
        >>> linked_list.add_node(1)
        >>> linked_list.add_node(2)
        >>> linked_list.add_node(3)
        >>> linked_list.add_node(4)

        >>> linked_list.detect_cycle()
        False

        # Create a cycle in the linked list
        >>> linked_list.head.next_node.next_node.next_node = linked_list.head.next_node

        >>> linked_list.detect_cycle()
        True
        """
        logger.debug(">>> Entering detect_cycle()")
        if self.head is None:
            return False

        slow_pointer: Node | None = self.head
        fast_pointer: Node | None = self.head

        while fast_pointer is not None and fast_pointer.next_node is not None:
            slow_pointer = slow_pointer.next_node if slow_pointer else None
            fast_pointer = fast_pointer.next_node.next_node
            logger.debug("detect_cycle(self=%s): fast_pointer → %s", self, fast_pointer)
            if slow_pointer == fast_pointer:
                return True

        logger.debug("<<< Exiting detect_cycle()")
        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    linked_list = LinkedList()
    linked_list.add_node(1)
    linked_list.add_node(2)
    linked_list.add_node(3)
    linked_list.add_node(4)

    # Create a cycle in the linked list
    # It first checks if the head, next_node, and next_node.next_node attributes of the
    # linked list are not None to avoid any potential type errors.
    if (
        linked_list.head
        and linked_list.head.next_node
        and linked_list.head.next_node.next_node
    ):
        linked_list.head.next_node.next_node.next_node = linked_list.head.next_node

    has_cycle = linked_list.detect_cycle()
    print(has_cycle)  # Output: True
