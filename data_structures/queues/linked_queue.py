"""A Queue using a linked list like structure"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any
import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data: Any) -> None:
        logger.debug(">>> Entering __init__(data=%s)", data)
        self.data: Any = data
        self.next: Node | None = None
        logger.debug("<<< Exiting __init__(data=%s)", data)
        logger.debug(">>> Entering __init__()")
        logger.debug("<<< Exiting __init__()")

    def __str__(self) -> str:
        logger.debug(">>> Entering __str__()")
        logger.debug("<<< Exiting __str__()")
        return f"{self.data}"


class LinkedQueue:
    """
    >>> queue = LinkedQueue()
    >>> queue.is_empty()
    True
    >>> queue.put(5)
    >>> queue.put(9)
    >>> queue.put('python')
    >>> queue.is_empty()
    False
    >>> queue.get()
    5
    >>> queue.put('algorithms')
    >>> queue.get()
    9
    >>> queue.get()
    'python'
    >>> queue.get()
    'algorithms'
    >>> queue.is_empty()
    True
    >>> queue.get()
    Traceback (most recent call last):
        ...
    IndexError: dequeue from empty queue
    """

    def __init__(self) -> None:
        self.front: Node | None = None
        self.rear: Node | None = None

    def __iter__(self) -> Iterator[Any]:
        logger.debug(">>> Entering __iter__()")
        node = self.front
        logger.debug("__iter__(self=%s): node → %s", self, node)
        while node:
            yield node.data
            logger.debug("<<< Exiting __iter__()")
            node = node.next

    def __len__(self) -> int:
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> len(queue)
        5
        >>> for i in range(1, 6):
        ...     assert len(queue) == 6 - i
        ...     _ = queue.get()
        >>> len(queue)
        0
        """
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return len(tuple(iter(self)))

    def __str__(self) -> str:
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 4):
        ...     queue.put(i)
        >>> queue.put("Python")
        >>> queue.put(3.14)
        >>> queue.put(True)
        >>> str(queue)
        '1 <- 2 <- 3 <- Python <- 3.14 <- True'
        """
        return " <- ".join(str(item) for item in self)

    def is_empty(self) -> bool:
        """
        >>> queue = LinkedQueue()
        >>> queue.is_empty()
        True
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> queue.is_empty()
        False
        """
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return len(self) == 0

    def put(self, item: Any) -> None:
        """
        >>> queue = LinkedQueue()
        >>> queue.get()
        Traceback (most recent call last):
            ...
        IndexError: dequeue from empty queue
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> str(queue)
        '1 <- 2 <- 3 <- 4 <- 5'
        """
        logger.debug(">>> Entering put(item=%s)", item)
        logger.debug("put(self=%s,item=%s): self.front → %s", self, item, self.front)
        node = Node(item)
        logger.debug("put(self=%s,item=%s): node → %s", self, item, node)
        logger.debug("put(item=%s): node → %s", item, node)
        if self.is_empty():
            self.front = self.rear = node
        else:
            assert isinstance(self.rear, Node)
            self.rear.next = node
            logger.debug("<<< Exiting put(item=%s)", item)
            self.rear = node
            logger.debug("put(self=%s,item=%s): self.rear → %s", self, item, self.rear)

    def get(self) -> Any:
        """
        >>> queue = LinkedQueue()
        >>> queue.get()
        Traceback (most recent call last):
            ...
        IndexError: dequeue from empty queue
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> for i in range(1, 6):
        ...     assert queue.get() == i
        >>> len(queue)
        0
        """
        logger.debug(">>> Entering get()")
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        assert isinstance(self.front, Node)
        node = self.front
        logger.debug("get(self=%s): node → %s", self, node)
        self.front = self.front.next
        logger.debug("get(self=%s): self.front → %s", self, self.front)
        if self.front is None:
            self.rear = None
            logger.debug("get(self=%s): self.rear → %s", self, self.rear)
        logger.debug("<<< Exiting get()")
        return node.data

    def clear(self) -> None:
        """
        >>> queue = LinkedQueue()
        >>> for i in range(1, 6):
        ...     queue.put(i)
        >>> queue.clear()
        >>> len(queue)
        0
        >>> str(queue)
        ''
        """
        logger.debug(">>> Entering clear()")
        self.front = self.rear = None
        logger.debug("clear(self=%s): self.front → %s", self, self.front)
        logger.debug("<<< Exiting clear()")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
