"""A Stack using a linked list like structure"""

from __future__ import annotations

from collections.abc import Iterator
from typing import TypeVar
import logging
logger = logging.getLogger(__name__)

T = TypeVar("T")


class Node[T]:
    def __init__(self, data: T):
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): self.data → %s", data, self.data, extra={"event.action": "__init__"})
        self.next: Node[T] | None = None
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return f"{self.data}"


class LinkedStack[T]:
    """
    Linked List Stack implementing push (to top),
    pop (from top) and is_empty

    >>> stack = LinkedStack()
    >>> stack.is_empty()
    True
    >>> stack.push(5)
    >>> stack.push(9)
    >>> stack.push('python')
    >>> stack.is_empty()
    False
    >>> stack.pop()
    'python'
    >>> stack.push('algorithms')
    >>> stack.pop()
    'algorithms'
    >>> stack.pop()
    9
    >>> stack.pop()
    5
    >>> stack.is_empty()
    True
    >>> stack.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty stack
    """

    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.top: Node[T] | None = None
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def __iter__(self) -> Iterator[T]:
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        node = self.top
        while node:
            yield node.data
            node = node.next
            logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})

    def __str__(self) -> str:
        """
        >>> stack = LinkedStack()
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> str(stack)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self) -> int:
        """
        >>> stack = LinkedStack()
        >>> len(stack) == 0
        True
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> len(stack) == 3
        True
        """
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        """
        >>> stack = LinkedStack()
        >>> stack.is_empty()
        True
        >>> stack.push(1)
        >>> stack.is_empty()
        False
        """
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return self.top is None

    def push(self, item: T) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Python")
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> str(stack)
        'C->Java->Python'
        """
        logger.error(">>> Entering push(item=%s)", item, extra={"event.action": "push", "logrite.item": item})
        node = Node(item)
        logger.error("push(item=%s): node → %s", item, node, extra={"event.action": "push", "logrite.item": item})
        if not self.is_empty():
            logger.warning("<<< Exiting push(item=%s)", item, extra={"event.action": "push", "logrite.item": item})
            node.next = self.top
            logger.debug("push(self=%s,item=%s): node.next → %s", self, item, node.next, extra={"event.action": "push", "logrite.item": item})
        self.top = node
        logger.debug("push(self=%s,item=%s): self.top → %s", self, item, self.top, extra={"event.action": "push", "logrite.item": item})

    def pop(self) -> T:
        """
        >>> stack = LinkedStack()
        >>> stack.pop()
        Traceback (most recent call last):
            ...
        IndexError: pop from empty stack
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> stack.pop() == 'a'
        True
        >>> stack.pop() == 'b'
        True
        >>> stack.pop() == 'c'
        True
        """
        logger.error(">>> Entering pop()", extra={"event.action": "pop"})
        if self.is_empty():
            raise IndexError("pop from empty stack")
        assert isinstance(self.top, Node)
        pop_node = self.top
        self.top = self.top.next
        logger.debug("pop(self=%s): self.top → %s", self, self.top, extra={"event.action": "pop"})
        logger.warning("<<< Exiting pop()", extra={"event.action": "pop"})
        return pop_node.data

    def peek(self) -> T:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> stack.peek()
        'Python'
        """
        logger.error(">>> Entering peek()", extra={"event.action": "peek"})
        if self.is_empty():
            raise IndexError("peek from empty stack")

        assert self.top is not None
        logger.warning("<<< Exiting peek()", extra={"event.action": "peek"})
        return self.top.data

    def clear(self) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> str(stack)
        'Python->C->Java'
        >>> stack.clear()
        >>> len(stack) == 0
        True
        """
        logger.error(">>> Entering clear()", extra={"event.action": "clear"})
        self.top = None
        logger.warning("<<< Exiting clear()", extra={"event.action": "clear"})
        logger.debug("clear(self=%s): self.top → %s", self, self.top, extra={"event.action": "clear"})


if __name__ == "__main__":
    from doctest import testmod

    testmod()
