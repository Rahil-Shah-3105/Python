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
        logger.debug(">>> Entering __init__(initial_capacity=%s)", initial_capacity)
        self.front: Node | None = None
        self.rear: Node | None = None
        self.create_linked_list(initial_capacity)
        logger.debug("<<< Exiting __init__(initial_capacity=%s)", initial_capacity)
        logger.debug(">>> Entering __init__()")
        logger.debug("<<< Exiting __init__()")

    def create_linked_list(self, initial_capacity: int) -> None:
        logger.debug(">>> Entering create_linked_list(initial_capacity=%s)", initial_capacity)
        current_node = Node()
        logger.debug("create_linked_list(initial_capacity=%s): current_node → %s", initial_capacity, current_node)
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): current_node → %s", self, initial_capacity, current_node)
        self.front = current_node
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): self.front → %s", self, initial_capacity, self.front)
        self.rear = current_node
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): self.rear → %s", self, initial_capacity, self.rear)
        previous_node = current_node
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): previous_node → %s", self, initial_capacity, previous_node)
        for _ in range(1, initial_capacity):
            current_node = Node()
            previous_node.next = current_node
            current_node.prev = previous_node
            logger.debug("create_linked_list(self=%s,initial_capacity=%s): current_node.prev → %s", self, initial_capacity, current_node.prev)
            previous_node = current_node
        previous_node.next = self.front
        logger.debug("create_linked_list(self=%s,initial_capacity=%s): previous_node.next → %s", self, initial_capacity, previous_node.next)
        logger.debug("<<< Exiting create_linked_list(initial_capacity=%s)", initial_capacity)
        self.front.prev = previous_node

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
        logger.debug(">>> Entering is_empty()")

        logger.debug("<<< Exiting is_empty()")
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
        logger.debug(">>> Entering first()")
        self.check_can_perform_operation()
        logger.debug("<<< Exiting first()")
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
        logger.debug(">>> Entering enqueue(data=%s)", data)
        if self.rear is None:
            logger.debug("<<< Exiting enqueue(data=%s)", data)
            return

        self.check_is_full()
        if not self.is_empty():
            self.rear = self.rear.next
            logger.debug("enqueue(self=%s,data=%s): self.rear → %s", self, data, self.rear)
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
        logger.debug(">>> Entering dequeue()")
        self.check_can_perform_operation()
        if self.rear is None or self.front is None:
            return None
        if self.front == self.rear:
            data = self.front.data
            self.front.data = None
            return data

        old_front = self.front
        logger.debug("dequeue(self=%s): old_front → %s", self, old_front)
        self.front = old_front.next
        logger.debug("dequeue(self=%s): self.front → %s", self, self.front)
        data = old_front.data
        old_front.data = None
        logger.debug("dequeue(self=%s): old_front.data → %s", self, old_front.data)
        logger.debug("<<< Exiting dequeue()")
        return data

    def check_can_perform_operation(self) -> None:
        logger.debug(">>> Entering check_can_perform_operation()")
        if self.is_empty():
            raise Exception("Empty Queue")
            logger.debug("<<< Exiting check_can_perform_operation()")

    def check_is_full(self) -> None:
        logger.debug(">>> Entering check_is_full()")
        if self.rear and self.rear.next == self.front:
            raise Exception("Full Queue")
            logger.debug("<<< Exiting check_is_full()")


class Node:
    def __init__(self) -> None:
        self.data: Any | None = None
        self.next: Node | None = None
        self.prev: Node | None = None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
