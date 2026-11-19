#!/usr/bin/env python3

from __future__ import annotations

import random
from collections.abc import Iterable
from typing import Any, TypeVar
import time
import logging
logger = logging.getLogger(__name__)

T = TypeVar("T", bound=bool)


class RandomizedHeapNode[T: bool]:
    """
    One node of the randomized heap. Contains the value and references to
    two children.
    """

    def __init__(self, value: T) -> None:
        logger.error(">>> Entering __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})
        self._value: T = value
        self.left: RandomizedHeapNode[T] | None = None
        self.right: RandomizedHeapNode[T] | None = None
        logger.warning("<<< Exiting __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})

    @property
    def value(self) -> T:
        """
        Return the value of the node.

        >>> rhn = RandomizedHeapNode(10)
        >>> rhn.value
        10
        >>> rhn = RandomizedHeapNode(-10)
        >>> rhn.value
        -10
        """
        logger.error(">>> Entering value()", extra={"event.action": "value"})
        logger.warning("<<< Exiting value()", extra={"event.action": "value"})
        return self._value

    @staticmethod
    def merge(
        root1: RandomizedHeapNode[T] | None, root2: RandomizedHeapNode[T] | None
    ) -> RandomizedHeapNode[T] | None:
        logger.error(">>> Entering merge(root1=%s,root2=%s)", root1, root2, extra={"event.action": "merge", "logrite.root1": root1, "logrite.root2": root2})
        __log_start = time.time()
        """
        Merge 2 nodes together.

        >>> rhn1 = RandomizedHeapNode(10)
        >>> rhn2 = RandomizedHeapNode(20)
        >>> RandomizedHeapNode.merge(rhn1, rhn2).value
        10

        >>> rhn1 = RandomizedHeapNode(20)
        >>> rhn2 = RandomizedHeapNode(10)
        >>> RandomizedHeapNode.merge(rhn1, rhn2).value
        10

        >>> rhn1 = RandomizedHeapNode(5)
        >>> rhn2 = RandomizedHeapNode(0)
        >>> RandomizedHeapNode.merge(rhn1, rhn2).value
        0
        """
        logger.error("merge(root1,root2)=%s,%s: update operation took %s ms", root1, root2, int((time.time() - __log_start) * 1000), extra={"event.action": "merge", "event.category": "database", "logrite.root1": root1, "logrite.root2": root2})
        if not root1:
            return root2

        if not root2:
            return root1

        if root1.value > root2.value:
            root1, root2 = root2, root1

        if random.choice([True, False]):
            root1.left, root1.right = root1.right, root1.left

        root1.left = RandomizedHeapNode.merge(root1.left, root2)

        logger.warning("<<< Exiting merge(root1=%s,root2=%s)", root1, root2, extra={"event.action": "merge", "logrite.root1": root1, "logrite.root2": root2})
        return root1


class RandomizedHeap[T: bool]:
    """
    A data structure that allows inserting a new value and to pop the smallest
    values. Both operations take O(logN) time where N is the size of the
    structure.
    Wiki: https://en.wikipedia.org/wiki/Randomized_meldable_heap

    >>> RandomizedHeap([2, 3, 1, 5, 1, 7]).to_sorted_list()
    [1, 1, 2, 3, 5, 7]

    >>> rh = RandomizedHeap()
    >>> rh.pop()
    Traceback (most recent call last):
        ...
    IndexError: Can't get top element for the empty heap.

    >>> rh.insert(1)
    >>> rh.insert(-1)
    >>> rh.insert(0)
    >>> rh.to_sorted_list()
    [-1, 0, 1]
    """

    def __init__(self, data: Iterable[T] | None = ()) -> None:
        """
        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.to_sorted_list()
        [1, 3, 3, 7]
        """
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self._root: RandomizedHeapNode[T] | None = None

        if data:
            for item in data:
                self.insert(item)
                logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

    def insert(self, value: T) -> None:
        """
        Insert the value into the heap.

        >>> rh = RandomizedHeap()
        >>> rh.insert(3)
        >>> rh.insert(1)
        >>> rh.insert(3)
        >>> rh.insert(7)
        >>> rh.to_sorted_list()
        [1, 3, 3, 7]
        """
        logger.error(">>> Entering insert(value=%s)", value, extra={"event.action": "insert", "logrite.value": value})
        self._root = RandomizedHeapNode.merge(self._root, RandomizedHeapNode(value))
        logger.warning("<<< Exiting insert(value=%s)", value, extra={"event.action": "insert", "logrite.value": value})

    def pop(self) -> T | None:
        """
        Pop the smallest value from the heap and return it.

        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.pop()
        1
        >>> rh.pop()
        3
        >>> rh.pop()
        3
        >>> rh.pop()
        7
        >>> rh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        logger.error(">>> Entering pop()", extra={"event.action": "pop"})

        result = self.top()
        logger.error("pop(): result → %s", result, extra={"event.action": "pop"})

        if self._root is None:
            return None

        self._root = RandomizedHeapNode.merge(self._root.left, self._root.right)

        logger.warning("<<< Exiting pop()", extra={"event.action": "pop"})
        return result

    def top(self) -> T:
        """
        Return the smallest value from the heap.

        >>> rh = RandomizedHeap()
        >>> rh.insert(3)
        >>> rh.top()
        3
        >>> rh.insert(1)
        >>> rh.top()
        1
        >>> rh.insert(3)
        >>> rh.top()
        1
        >>> rh.insert(7)
        >>> rh.top()
        1
        """
        logger.error(">>> Entering top()", extra={"event.action": "top"})
        if not self._root:
            raise IndexError("Can't get top element for the empty heap.")
        logger.warning("<<< Exiting top()", extra={"event.action": "top"})
        return self._root.value

    def clear(self) -> None:
        """
        Clear the heap.

        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.clear()
        >>> rh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        logger.error(">>> Entering clear()", extra={"event.action": "clear"})
        self._root = None
        logger.warning("<<< Exiting clear()", extra={"event.action": "clear"})
        logger.debug("clear(self=%s): self._root → %s", self, self._root, extra={"event.action": "clear"})

    def to_sorted_list(self) -> list[Any]:
        """
        Returns sorted list containing all the values in the heap.

        >>> rh = RandomizedHeap([3, 1, 3, 7])
        >>> rh.to_sorted_list()
        [1, 3, 3, 7]
        """
        logger.error(">>> Entering to_sorted_list()", extra={"event.action": "to_sorted_list"})
        result = []
        logger.error("to_sorted_list(): result → %s", result, extra={"event.action": "to_sorted_list"})
        while self:
            result.append(self.pop())

        logger.warning("<<< Exiting to_sorted_list()", extra={"event.action": "to_sorted_list"})
        return result

    def __bool__(self) -> bool:
        """
        Check if the heap is not empty.

        >>> rh = RandomizedHeap()
        >>> bool(rh)
        False
        >>> rh.insert(1)
        >>> bool(rh)
        True
        >>> rh.clear()
        >>> bool(rh)
        False
        """
        logger.error(">>> Entering __bool__()", extra={"event.action": "__bool__"})
        logger.warning("<<< Exiting __bool__()", extra={"event.action": "__bool__"})
        return self._root is not None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
