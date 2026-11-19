# Implementation of Circular Queue using linked lists
# https://en.wikipedia.org/wiki/Circular_buffer

from __future__ import annotations

from typing import Any
import logging
logger = logging.getLogger(__name__)


class CircularQueueLinkedList:
    """
    Circular FIFO list with the given capacity (default queue length : 6)

    >>> cq = CircularQueueLinkedList(2)
    >>> cq.enqueue('a')
    >>> cq.enqueue('b')
    >>> cq.enqueue('c')
    Traceback (most recent call last):
       ...
    Exception: Full Queue
    """

    def __init__(self, initial_capacity: int = 6) -> None:
        logger.error(">>> Entering __init__(initial_capacity=%s)", initial_capacity, extra={"event.action": "__init__", "logrite.initial_capacity": initial_capacity})
        self.front: Node | None = None
        self.rear: Node | None = None
        self.create_linked_list(initial_capacity)
        logger.warning("<<< Exiting __init__(initial_capacity=%s)", initial_capacity, extra={"event.action": "__init__", "logrite.initial_capacity": initial_capacity})

    def create_linked_list(self, initial_capacity: int) -> None:
        logger.error(">>> Entering create_linked_list(initial_capacity=%s)", initial_capacity, extra={"event.action": "create_linked_list", "logrite.initial_capacity": initial_capacity})
        current_node = Node()
        logger.error("create_linked_list(initial_capacity=%s): current_node → %s", initial_capacity, current_node, extra={"event.action": "create_linked_list", "logrite.initial_capacity": initial_capacity})
        self.front = current_node
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): self.front → %s", self, initial_capacity, self.front, extra={"event.action": "create_linked_list", "logrite.initial_capacity": initial_capacity})
        self.rear = current_node
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): self.rear → %s", self, initial_capacity, self.rear, extra={"event.action": "create_linked_list", "logrite.initial_capacity": initial_capacity})
        previous_node = current_node
        for _ in range(1, initial_capacity):
            current_node = Node()
            previous_node.next = current_node
            current_node.prev = previous_node
            logger.debug("create_linked_list(self=%s,initial_capacity=%s): current_node.prev → %s", self, initial_capacity, current_node.prev, extra={"event.action": "create_linked_list", "logrite.initial_capacity": initial_capacity})
            previous_node = current_node
        previous_node.next = self.front
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): previous_node.next → %s", self, initial_capacity, previous_node.next, extra={"event.action": "create_linked_list", "logrite.initial_capacity": initial_capacity})
        self.front.prev = previous_node
        logger.warning("<<< Exiting create_linked_list(initial_capacity=%s)", initial_capacity, extra={"event.action": "create_linked_list", "logrite.initial_capacity": initial_capacity})

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty or not
        >>> cq = CircularQueueLinkedList()
        >>> cq.is_empty()
        True
        >>> cq.enqueue('a')
        >>> cq.is_empty()
        False
        >>> cq.dequeue()
        'a'
        >>> cq.is_empty()
        True
        """
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})

        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return (
            self.front == self.rear
            and self.front is not None
            and self.front.data is None
        )

    def first(self) -> Any | None:
        """
        Returns the first element of the queue
        >>> cq = CircularQueueLinkedList()
        >>> cq.first()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('a')
        >>> cq.first()
        'a'
        >>> cq.dequeue()
        'a'
        >>> cq.first()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('b')
        >>> cq.enqueue('c')
        >>> cq.first()
        'b'
        """
        logger.error(">>> Entering first()", extra={"event.action": "first"})
        self.check_can_perform_operation()
        logger.warning("<<< Exiting first()", extra={"event.action": "first"})
        return self.front.data if self.front else None

    def enqueue(self, data: Any) -> None:
        """
        Saves data at the end of the queue

        >>> cq = CircularQueueLinkedList()
        >>> cq.enqueue('a')
        >>> cq.enqueue('b')
        >>> cq.dequeue()
        'a'
        >>> cq.dequeue()
        'b'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """
        logger.error(">>> Entering enqueue(data=%s)", data, extra={"event.action": "enqueue"})
        if self.rear is None:
            logger.warning("<<< Exiting enqueue(data=%s)", data, extra={"event.action": "enqueue"})
            return

        self.check_is_full()
        if not self.is_empty():
            self.rear = self.rear.next
            logger.debug("enqueue(self=%s,data=%s): self.rear → %s", self, data, self.rear, extra={"event.action": "enqueue"})
        if self.rear:
            self.rear.data = data

    def dequeue(self) -> Any:
        """
        Removes and retrieves the first element of the queue

        >>> cq = CircularQueueLinkedList()
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('a')
        >>> cq.dequeue()
        'a'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """
        logger.error(">>> Entering dequeue()", extra={"event.action": "dequeue"})
        self.check_can_perform_operation()
        if self.rear is None or self.front is None:
            return None
        if self.front == self.rear:
            data = self.front.data
            self.front.data = None
            return data

        old_front = self.front
        self.front = old_front.next
        logger.debug("dequeue(self=%s): self.front → %s", self, self.front, extra={"event.action": "dequeue"})
        data = old_front.data
        old_front.data = None
        logger.debug("dequeue(self=%s): old_front.data → %s", self, old_front.data, extra={"event.action": "dequeue"})
        logger.warning("<<< Exiting dequeue()", extra={"event.action": "dequeue"})
        return data

    def check_can_perform_operation(self) -> None:
        logger.error(">>> Entering check_can_perform_operation()", extra={"event.action": "check_can_perform_operation"})
        if self.is_empty():
            raise Exception("Empty Queue")
            logger.warning("<<< Exiting check_can_perform_operation()", extra={"event.action": "check_can_perform_operation"})

    def check_is_full(self) -> None:
        logger.error(">>> Entering check_is_full()", extra={"event.action": "check_is_full"})
        if self.rear and self.rear.next == self.front:
            raise Exception("Full Queue")
            logger.warning("<<< Exiting check_is_full()", extra={"event.action": "check_is_full"})


class Node:
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.data: Any | None = None
        self.next: Node | None = None
        self.prev: Node | None = None
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
