"""A Queue using a linked list like structure"""

from __future__ import annotations

from collections.abc import Iterator
from typing import Any
import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data: Any) -> None:
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data: Any = data
        self.next: Node | None = None
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
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
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.front: Node | None = None
        self.rear: Node | None = None
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def __iter__(self) -> Iterator[Any]:
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        node = self.front
        while node:
            yield node.data
            node = node.next
            logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})

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
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
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
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
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
        logger.error(">>> Entering put(item=%s)", item, extra={"event.action": "put", "logrite.item": item})
        node = Node(item)
        logger.error("put(item=%s): node → %s", item, node, extra={"event.action": "put", "logrite.item": item})
        if self.is_empty():
            self.front = self.rear = node
        else:
            logger.debug("put(self=%s,item=%s): self.front → %s", self, item, self.front, extra={"event.action": "put", "logrite.item": item})
            assert isinstance(self.rear, Node)
            self.rear.next = node
            logger.warning("<<< Exiting put(item=%s)", item, extra={"event.action": "put", "logrite.item": item})
            self.rear = node
            logger.debug("put(self=%s,item=%s): self.rear → %s", self, item, self.rear, extra={"event.action": "put", "logrite.item": item})

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
        logger.error(">>> Entering get()", extra={"event.action": "get"})
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        assert isinstance(self.front, Node)
        node = self.front
        self.front = self.front.next
        logger.debug("get(self=%s): self.front → %s", self, self.front, extra={"event.action": "get"})
        if self.front is None:
            self.rear = None
        logger.debug("get(self=%s): self.rear → %s", self, self.rear, extra={"event.action": "get"})
        logger.warning("<<< Exiting get()", extra={"event.action": "get"})
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
        logger.error(">>> Entering clear()", extra={"event.action": "clear"})
        self.front = self.rear = None
        logger.warning("<<< Exiting clear()", extra={"event.action": "clear"})
        logger.debug("clear(self=%s): self.front → %s", self, self.front, extra={"event.action": "clear"})


if __name__ == "__main__":
    from doctest import testmod

    testmod()
