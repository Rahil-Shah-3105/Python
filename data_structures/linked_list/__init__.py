"""
Linked Lists consists of Nodes.
Nodes contain data and also may link to other nodes:
    - Head Node: First node, the address of the
                 head node gives us access of the complete list
    - Last node: points to null
"""

from __future__ import annotations

from typing import Any
import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, item: Any, next: Any) -> None:  # noqa: A002
        logger.error(">>> Entering __init__(item=%s,next=%s)", item, next, extra={"event.action": "__init__", "logrite.item": item})
        self.item = item
        logger.debug("__init__(self=%s,item=%s,next=%s): self.item → %s", self, item, next, self.item, extra={"event.action": "__init__", "logrite.item": item})
        self.next = next
        logger.warning("<<< Exiting __init__(item=%s,next=%s)", item, next, extra={"event.action": "__init__", "logrite.item": item})
        logger.debug("__init__(self=%s,item=%s,next=%s): self.next → %s", self, item, next, self.next, extra={"event.action": "__init__", "logrite.item": item})


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size = 0
        logger.debug("__init__(self=%s): self.size → %s", self, self.size, extra={"event.action": "__init__"})

    def add(self, item: Any, position: int = 0) -> None:
        """
        Add an item to the LinkedList at the specified position.
        Default position is 0 (the head).

        Args:
            item (Any): The item to add to the LinkedList.
            position (int, optional): The position at which to add the item.
                Defaults to 0.

        Raises:
            ValueError: If the position is negative or out of bounds.

        >>> linked_list = LinkedList()
        >>> linked_list.add(1)
        >>> linked_list.add(2)
        >>> linked_list.add(3)
        >>> linked_list.add(4, 2)
        >>> print(linked_list)
        3 --> 2 --> 4 --> 1

        # Test adding to a negative position
        >>> linked_list.add(5, -3)
        Traceback (most recent call last):
            ...
        ValueError: Position must be non-negative

        # Test adding to an out-of-bounds position
        >>> linked_list.add(5,7)
        Traceback (most recent call last):
            ...
        ValueError: Out of bounds
        >>> linked_list.add(5, 4)
        >>> print(linked_list)
        3 --> 2 --> 4 --> 1 --> 5
        """
        logger.error(">>> Entering add(item=%s,position=%s)", item, position, extra={"event.action": "add", "logrite.item": item, "logrite.position": position})
        if position < 0:
            raise ValueError("Position must be non-negative")

        if position == 0 or self.head is None:
            new_node = Node(item, self.head)
            logger.error("add(item=%s,position=%s): new_node → %s", item, position, new_node, extra={"event.action": "add", "logrite.item": item, "logrite.position": position})
            self.head = new_node
        else:
            logger.debug("add(self=%s,item=%s,position=%s): self.head → %s", self, item, position, self.head, extra={"event.action": "add", "logrite.item": item, "logrite.position": position})
            current = self.head
            for _ in range(position - 1):
                current = current.next
                if current is None:
                    raise ValueError("Out of bounds")
            new_node = Node(item, current.next)
            current.next = new_node
            logger.debug("add(self=%s,item=%s,position=%s): current.next → %s", self, item, position, current.next, extra={"event.action": "add", "logrite.item": item, "logrite.position": position})
        self.size += 1
        logger.warning("<<< Exiting add(item=%s,position=%s)", item, position, extra={"event.action": "add", "logrite.item": item, "logrite.position": position})

    def remove(self) -> Any:
        logger.error(">>> Entering remove()", extra={"event.action": "remove"})
        # Switched 'self.is_empty()' to 'self.head is None'
        # because mypy was considering the possibility that 'self.head'
        # can be None in below else part and giving error
        if self.head is None:
            return None
        else:
            item = self.head.item
            self.head = self.head.next
            logger.debug("remove(self=%s): self.head → %s", self, self.head, extra={"event.action": "remove"})
            self.size -= 1
            logger.warning("<<< Exiting remove()", extra={"event.action": "remove"})
            return item

    def is_empty(self) -> bool:
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return self.head is None

    def __str__(self) -> str:
        """
        >>> linked_list = LinkedList()
        >>> linked_list.add(23)
        >>> linked_list.add(14)
        >>> linked_list.add(9)
        >>> print(linked_list)
        9 --> 14 --> 23
        """
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        if self.is_empty():
            return ""
        else:
            iterate = self.head
            item_str = ""
            item_list: list[str] = []
            while iterate:
                item_list.append(str(iterate.item))
                iterate = iterate.next

            item_str = " --> ".join(item_list)

            logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
            return item_str

    def __len__(self) -> int:
        """
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.add("a")
        >>> len(linked_list)
        1
        >>> linked_list.add("b")
        >>> len(linked_list)
        2
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        1
        >>> _ = linked_list.remove()
        >>> len(linked_list)
        0
        """
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return self.size
