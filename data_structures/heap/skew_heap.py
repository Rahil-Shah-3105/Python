#!/usr/bin/env python3

from __future__ import annotations

from collections.abc import Iterable, Iterator
from typing import Any, TypeVar
import time
import logging
logger = logging.getLogger(__name__)

T = TypeVar("T", bound=bool)


class SkewNode[T: bool]:
    """
    One node of the skew heap. Contains the value and references to
    two children.
    """

    def __init__(self, value: T) -> None:
        logger.error(">>> Entering __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})
        self._value: T = value
        self.left: SkewNode[T] | None = None
        self.right: SkewNode[T] | None = None
        logger.warning("<<< Exiting __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})

    @property
    def value(self) -> T:
        """
        Return the value of the node.

        >>> SkewNode(0).value
        0
        >>> SkewNode(3.14159).value
        3.14159
        >>> SkewNode("hello").value
        'hello'
        >>> SkewNode(None).value

        >>> SkewNode(True).value
        True
        >>> SkewNode([]).value
        []
        >>> SkewNode({}).value
        {}
        >>> SkewNode(set()).value
        set()
        >>> SkewNode(0.0).value
        0.0
        >>> SkewNode(-1e-10).value
        -1e-10
        >>> SkewNode(10).value
        10
        >>> SkewNode(-10.5).value
        -10.5
        >>> SkewNode().value
        Traceback (most recent call last):
        ...
        TypeError: SkewNode.__init__() missing 1 required positional argument: 'value'
        """
        logger.error(">>> Entering value()", extra={"event.action": "value"})
        logger.warning("<<< Exiting value()", extra={"event.action": "value"})
        return self._value

    @staticmethod
    def merge(
        root1: SkewNode[T] | None, root2: SkewNode[T] | None
    ) -> SkewNode[T] | None:
        logger.error(">>> Entering merge(root1=%s,root2=%s)", root1, root2, extra={"event.action": "merge", "logrite.root1": root1, "logrite.root2": root2})
        __log_start = time.time()
        """
        Merge 2 nodes together.
        >>> SkewNode.merge(SkewNode(10),SkewNode(-10.5)).value
        -10.5
        >>> SkewNode.merge(SkewNode(10),SkewNode(10.5)).value
        10
        >>> SkewNode.merge(SkewNode(10),SkewNode(10)).value
        10
        >>> SkewNode.merge(SkewNode(-100),SkewNode(-10.5)).value
        -100
        """
        logger.error("merge(root1,root2)=%s,%s: update operation took %s ms", root1, root2, int((time.time() - __log_start) * 1000), extra={"event.action": "merge", "event.category": "database", "logrite.root1": root1, "logrite.root2": root2})
        if not root1:
            return root2

        if not root2:
            return root1

        if root1.value > root2.value:
            root1, root2 = root2, root1

        result = root1
        temp = root1.right
        result.right = root1.left
        logger.debug("merge(root1=%s,root2=%s): result.right → %s", root1, root2, result.right, extra={"event.action": "merge", "logrite.root1": root1, "logrite.root2": root2})
        result.left = SkewNode.merge(temp, root2)

        logger.warning("<<< Exiting merge(root1=%s,root2=%s)", root1, root2, extra={"event.action": "merge", "logrite.root1": root1, "logrite.root2": root2})
        return result


class SkewHeap[T: bool]:
    """
    A data structure that allows inserting a new value and to pop the smallest
    values. Both operations take O(logN) time where N is the size of the
    structure.
    Wiki: https://en.wikipedia.org/wiki/Skew_heap
    Visualization: https://www.cs.usfca.edu/~galles/visualization/SkewHeap.html

    >>> list(SkewHeap([2, 3, 1, 5, 1, 7]))
    [1, 1, 2, 3, 5, 7]

    >>> sh = SkewHeap()
    >>> sh.pop()
    Traceback (most recent call last):
        ...
    IndexError: Can't get top element for the empty heap.

    >>> sh.insert(1)
    >>> sh.insert(-1)
    >>> sh.insert(0)
    >>> list(sh)
    [-1, 0, 1]
    """

    def __init__(self, data: Iterable[T] | None = ()) -> None:
        """
        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> list(sh)
        [1, 3, 3, 7]
        """
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self._root: SkewNode[T] | None = None
        if data:
            for item in data:
                self.insert(item)
                logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

    def __bool__(self) -> bool:
        """
        Check if the heap is not empty.

        >>> sh = SkewHeap()
        >>> bool(sh)
        False
        >>> sh.insert(1)
        >>> bool(sh)
        True
        >>> sh.clear()
        >>> bool(sh)
        False
        """
        logger.error(">>> Entering __bool__()", extra={"event.action": "__bool__"})
        logger.warning("<<< Exiting __bool__()", extra={"event.action": "__bool__"})
        return self._root is not None

    def __iter__(self) -> Iterator[T]:
        """
        Returns sorted list containing all the values in the heap.

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> list(sh)
        [1, 3, 3, 7]
        """
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        result: list[Any] = []
        while self:
            result.append(self.pop())

        # Pushing items back to the heap not to clear it.
        for item in result:
            self.insert(item)

        logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})
        return iter(result)

    def insert(self, value: T) -> None:
        """
        Insert the value into the heap.

        >>> sh = SkewHeap()
        >>> sh.insert(3)
        >>> sh.insert(1)
        >>> sh.insert(3)
        >>> sh.insert(7)
        >>> list(sh)
        [1, 3, 3, 7]
        """
        logger.error(">>> Entering insert(value=%s)", value, extra={"event.action": "insert", "logrite.value": value})
        self._root = SkewNode.merge(self._root, SkewNode(value))
        logger.warning("<<< Exiting insert(value=%s)", value, extra={"event.action": "insert", "logrite.value": value})

    def pop(self) -> T | None:
        """
        Pop the smallest value from the heap and return it.

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> sh.pop()
        1
        >>> sh.pop()
        3
        >>> sh.pop()
        3
        >>> sh.pop()
        7
        >>> sh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        logger.error(">>> Entering pop()", extra={"event.action": "pop"})
        result = self.top()
        self._root = (
            SkewNode.merge(self._root.left, self._root.right) if self._root else None
        )
        logger.error("pop(): result → %s", result, extra={"event.action": "pop"})

        logger.warning("<<< Exiting pop()", extra={"event.action": "pop"})
        return result

    def top(self) -> T:
        """
        Return the smallest value from the heap.

        >>> sh = SkewHeap()
        >>> sh.insert(3)
        >>> sh.top()
        3
        >>> sh.insert(1)
        >>> sh.top()
        1
        >>> sh.insert(3)
        >>> sh.top()
        1
        >>> sh.insert(7)
        >>> sh.top()
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

        >>> sh = SkewHeap([3, 1, 3, 7])
        >>> sh.clear()
        >>> sh.pop()
        Traceback (most recent call last):
            ...
        IndexError: Can't get top element for the empty heap.
        """
        logger.error(">>> Entering clear()", extra={"event.action": "clear"})
        self._root = None
        logger.warning("<<< Exiting clear()", extra={"event.action": "clear"})
        logger.debug("clear(self=%s): self._root → %s", self, self._root, extra={"event.action": "clear"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
