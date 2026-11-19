"""
Algorithm that merges two sorted linked lists into one sorted linked list.
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)

test_data_odd = (3, 9, -11, 0, 7, 5, 1, -1)
test_data_even = (4, 6, 2, 0, 8, 10, 3, -2)


@dataclass
class Node:
    data: int
    next_node: Node | None


class SortedLinkedList:
    def __init__(self, ints: Iterable[int]) -> None:
        logger.error(">>> Entering __init__(ints=%s)", ints, extra={"event.action": "__init__", "logrite.ints": ints})
        self.head: Node | None = None
        logger.error("__init__(ints=%s): self.head → %s", ints, self.head, extra={"event.action": "__init__", "logrite.ints": ints})
        for i in sorted(ints, reverse=True):
            logger.warning("<<< Exiting __init__(ints=%s)", ints, extra={"event.action": "__init__", "logrite.ints": ints})
            self.head = Node(i, self.head)

    def __iter__(self) -> Iterator[int]:
        """
        >>> tuple(SortedLinkedList(test_data_odd)) == tuple(sorted(test_data_odd))
        True
        >>> tuple(SortedLinkedList(test_data_even)) == tuple(sorted(test_data_even))
        True
        """
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        node = self.head
        while node:
            yield node.data
            node = node.next_node
            logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})

    def __len__(self) -> int:
        """
        >>> for i in range(3):
        ...     len(SortedLinkedList(range(i))) == i
        True
        True
        True
        >>> len(SortedLinkedList(test_data_odd))
        8
        """
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return sum(1 for _ in self)

    def __str__(self) -> str:
        """
        >>> str(SortedLinkedList([]))
        ''
        >>> str(SortedLinkedList(test_data_odd))
        '-11 -> -1 -> 0 -> 1 -> 3 -> 5 -> 7 -> 9'
        >>> str(SortedLinkedList(test_data_even))
        '-2 -> 0 -> 2 -> 3 -> 4 -> 6 -> 8 -> 10'
        """
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return " -> ".join([str(node) for node in self])


def merge_lists(
    sll_one: SortedLinkedList, sll_two: SortedLinkedList
) -> SortedLinkedList:
    logger.error(">>> Entering merge_lists(sll_one=%s,sll_two=%s)", sll_one, sll_two, extra={"event.action": "merge_lists", "logrite.sll_one": sll_one, "logrite.sll_two": sll_two})
    """
    >>> SSL = SortedLinkedList
    >>> merged = merge_lists(SSL(test_data_odd), SSL(test_data_even))
    >>> len(merged)
    16
    >>> str(merged)
    '-11 -> -2 -> -1 -> 0 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10'
    >>> list(merged) == list(sorted(test_data_odd + test_data_even))
    True
    """
    logger.warning("<<< Exiting merge_lists(sll_one=%s,sll_two=%s)", sll_one, sll_two, extra={"event.action": "merge_lists", "logrite.sll_one": sll_one, "logrite.sll_two": sll_two})
    return SortedLinkedList(list(sll_one) + list(sll_two))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    SSL = SortedLinkedList
    print(merge_lists(SSL(test_data_odd), SSL(test_data_even)))
