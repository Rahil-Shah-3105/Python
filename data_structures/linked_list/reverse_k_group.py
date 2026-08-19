from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    data: int
    next_node: Node | None = None


class LinkedList:
    def __init__(self, ints: Iterable[int]) -> None:
        logger.debug(">>> Entering __init__(ints=%s)", ints)
        self.head: Node | None = None
        for i in ints:
            self.append(i)
            logger.debug("<<< Exiting __init__(ints=%s)", ints)

    def __iter__(self) -> Iterator[int]:
        """
        >>> ints = []
        >>> list(LinkedList(ints)) == ints
        True
        >>> ints = tuple(range(5))
        >>> tuple(LinkedList(ints)) == ints
        True
        """
        logger.debug(">>> Entering __iter__()")
        node = self.head
        logger.debug("__iter__(self=%s): node → %s", self, node)
        while node:
            yield node.data
            logger.debug("<<< Exiting __iter__()")
            node = node.next_node

    def __len__(self) -> int:
        """
        >>> for i in range(3):
        ...     len(LinkedList(range(i))) == i
        True
        True
        True
        >>> len(LinkedList("abcdefgh"))
        8
        """
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return sum(1 for _ in self)

    def __str__(self) -> str:
        """
        >>> str(LinkedList([]))
        ''
        >>> str(LinkedList(range(5)))
        '0 -> 1 -> 2 -> 3 -> 4'
        """
        logger.debug(">>> Entering __str__()")
        logger.debug("<<< Exiting __str__()")
        return " -> ".join([str(node) for node in self])

    def append(self, data: int) -> None:
        """
        >>> ll = LinkedList([1, 2])
        >>> tuple(ll)
        (1, 2)
        >>> ll.append(3)
        >>> tuple(ll)
        (1, 2, 3)
        >>> ll.append(4)
        >>> tuple(ll)
        (1, 2, 3, 4)
        >>> len(ll)
        4
        """
        logger.debug(">>> Entering append(data=%s)", data)
        if not self.head:
            self.head = Node(data)
            logger.debug("append(data=%s): self.head → %s", data, self.head)
            logger.debug("append(self=%s,data=%s): node → %s", self, data, node)
            logger.debug("<<< Exiting append(data=%s)", data)
            return
        node = self.head
        while node.next_node:
            node = node.next_node
        node.next_node = Node(data)

    def reverse_k_nodes(self, group_size: int) -> None:
        """
        reverse nodes within groups of size k
        >>> ll = LinkedList([1, 2, 3, 4, 5])
        >>> ll.reverse_k_nodes(2)
        >>> tuple(ll)
        (2, 1, 4, 3, 5)
        >>> str(ll)
        '2 -> 1 -> 4 -> 3 -> 5'
        """
        logger.debug(">>> Entering reverse_k_nodes(group_size=%s)", group_size)
        if self.head is None or self.head.next_node is None:
            logger.debug("<<< Exiting reverse_k_nodes(group_size=%s)", group_size)
            return

        length = len(self)
        logger.debug("reverse_k_nodes(self=%s,group_size=%s): length → %s", self, group_size, length)
        dummy_head = Node(0)
        logger.debug("reverse_k_nodes(self=%s,group_size=%s): dummy_head → %s", self, group_size, dummy_head)
        dummy_head.next_node = self.head
        logger.debug("reverse_k_nodes(self=%s,group_size=%s): dummy_head.next_node → %s", self, group_size, dummy_head.next_node)
        previous_node = dummy_head
        logger.debug("reverse_k_nodes(self=%s,group_size=%s): previous_node → %s", self, group_size, previous_node)

        while length >= group_size:
            current_node = previous_node.next_node
            logger.debug("reverse_k_nodes(self=%s,group_size=%s): current_node → %s", self, group_size, current_node)
            assert current_node
            next_node = current_node.next_node
            logger.debug("reverse_k_nodes(self=%s,group_size=%s): next_node → %s", self, group_size, next_node)
            for _ in range(1, group_size):
                assert next_node, current_node
                current_node.next_node = next_node.next_node
                logger.debug("reverse_k_nodes(self=%s,group_size=%s): current_node.next_node → %s", self, group_size, current_node.next_node)
                assert previous_node
                next_node.next_node = previous_node.next_node
                logger.debug("reverse_k_nodes(self=%s,group_size=%s): next_node.next_node → %s", self, group_size, next_node.next_node)
                previous_node.next_node = next_node
                logger.debug("reverse_k_nodes(self=%s,group_size=%s): previous_node.next_node → %s", self, group_size, previous_node.next_node)
                next_node = current_node.next_node
            previous_node = current_node
            length -= group_size
        self.head = dummy_head.next_node
        logger.debug("reverse_k_nodes(self=%s,group_size=%s): self.head → %s", self, group_size, self.head)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ll = LinkedList([1, 2, 3, 4, 5])
    print(f"Original Linked List: {ll}")
    k = 2
    ll.reverse_k_nodes(k)
    print(f"After reversing groups of size {k}: {ll}")
