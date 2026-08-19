from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    data: Any
    next_node: Node | None = None


@dataclass
class CircularLinkedList:
    head: Node | None = None  # Reference to the head (first node)
    tail: Node | None = None  # Reference to the tail (last node)

    def __iter__(self) -> Iterator[Any]:
        """
        Iterate through all nodes in the Circular Linked List yielding their data.
        Yields:
            The data of each node in the linked list.
        """
        logger.debug(">>> Entering __iter__()")
        node = self.head
        while node:
            yield node.data
            node = node.next_node
            if node == self.head:
                break
                logger.debug("<<< Exiting __iter__()")

    def __len__(self) -> int:
        """
        Get the length (number of nodes) in the Circular Linked List.
        """
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """
        Generate a string representation of the Circular Linked List.
        Returns:
            A string of the format "1->2->....->N".
        """
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return "->".join(str(item) for item in iter(self))

    def insert_tail(self, data: Any) -> None:
        """
        Insert a node with the given data at the end of the Circular Linked List.
        """
        logger.debug(">>> Entering insert_tail(data=%s)", data)
        self.insert_nth(len(self), data)
        logger.debug("<<< Exiting insert_tail(data=%s)", data)

    def insert_head(self, data: Any) -> None:
        """
        Insert a node with the given data at the beginning of the Circular Linked List.
        """
        logger.debug(">>> Entering insert_head(data=%s)", data)
        self.insert_nth(0, data)
        logger.debug("<<< Exiting insert_head(data=%s)", data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert the data of the node at the nth pos in the Circular Linked List.
        Args:
            index: The index at which the data should be inserted.
            data: The data to be inserted.

        Raises:
            IndexError: If the index is out of range.
        """
        logger.debug(">>> Entering insert_nth(index=%s,data=%s)", index, data)
        if index < 0 or index > len(self):
            raise IndexError("list index out of range.")
        new_node: Node = Node(data)
        logger.debug("insert_nth(index=%s,data=%s): new_node → %s", index, data, new_node)
        if self.head is None:
            new_node.next_node = new_node  # First node points to itself
            logger.debug("insert_nth(self=%s,index=%s,data=%s): new_node.next_node → %s", self, index, data, new_node.next_node)
            self.tail = self.head = new_node
            logger.debug("insert_nth(self=%s,index=%s,data=%s): self.tail → %s", self, index, data, self.tail)
        elif index == 0:  # Insert at the head
            new_node.next_node = self.head
            assert self.tail is not None  # List is not empty, tail exists
            self.head = self.tail.next_node = new_node
            logger.debug("insert_nth(self=%s,index=%s,data=%s): self.head → %s", self, index, data, self.head)
        else:
            temp: Node | None = self.head
            for _ in range(index - 1):
                assert temp is not None
                temp = temp.next_node
            assert temp is not None
            new_node.next_node = temp.next_node
            temp.next_node = new_node
            logger.debug("insert_nth(self=%s,index=%s,data=%s): temp.next_node → %s", self, index, data, temp.next_node)
            if index == len(self) - 1:  # Insert at the tail
                logger.debug("<<< Exiting insert_nth(index=%s,data=%s)", index, data)
                self.tail = new_node

    def delete_front(self) -> Any:
        """
        Delete and return the data of the node at the front of the Circular Linked List.
        Raises:
            IndexError: If the list is empty.
        """
        logger.debug(">>> Entering delete_front()")
        logger.debug("<<< Exiting delete_front()")
        return self.delete_nth(0)

    def delete_tail(self) -> Any:
        """
        Delete and return the data of the node at the end of the Circular Linked List.
        Returns:
            Any: The data of the deleted node.
        Raises:
            IndexError: If the index is out of range.
        """
        logger.debug(">>> Entering delete_tail()")
        logger.debug("<<< Exiting delete_tail()")
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0) -> Any:
        """
        Delete and return the data of the node at the nth pos in Circular Linked List.
        Args:
            index (int): The index of the node to be deleted. Defaults to 0.
        Returns:
            Any: The data of the deleted node.
        Raises:
            IndexError: If the index is out of range.
        """
        logger.debug(">>> Entering delete_nth(index=%s)", index)
        if not 0 <= index < len(self):
            raise IndexError("list index out of range.")

        assert self.head is not None
        assert self.tail is not None
        delete_node: Node = self.head
        if self.head == self.tail:  # Just one node
            self.head = self.tail = None
            logger.debug("delete_nth(self=%s,index=%s): self.head → %s", self, index, self.head)
        elif index == 0:  # Delete head node
            assert self.tail.next_node is not None
            self.tail.next_node = self.tail.next_node.next_node
            self.head = self.head.next_node
        else:
            temp: Node | None = self.head
            for _ in range(index - 1):
                assert temp is not None
                temp = temp.next_node
            assert temp is not None
            assert temp.next_node is not None
            delete_node = temp.next_node
            logger.debug("delete_nth(self=%s,index=%s): delete_node → %s", self, index, delete_node)
            temp.next_node = temp.next_node.next_node
            logger.debug("delete_nth(self=%s,index=%s): temp.next_node → %s", self, index, temp.next_node)
            if index == len(self) - 1:  # Delete at tail
                self.tail = temp
                logger.debug("delete_nth(self=%s,index=%s): self.tail → %s", self, index, self.tail)
        logger.debug("<<< Exiting delete_nth(index=%s)", index)
        return delete_node.data

    def is_empty(self) -> bool:
        """
        Check if the Circular Linked List is empty.
        Returns:
            bool: True if the list is empty, False otherwise.
        """
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return len(self) == 0


def test_circular_linked_list() -> None:
    """
    Test cases for the CircularLinkedList class.
    >>> test_circular_linked_list()
    """
    logger.debug(">>> Entering test_circular_linked_list()")
    circular_linked_list = CircularLinkedList()
    logger.debug("test_circular_linked_list(): circular_linked_list → %s", circular_linked_list)
    assert len(circular_linked_list) == 0
    assert circular_linked_list.is_empty() is True
    assert str(circular_linked_list) == ""

    try:
        circular_linked_list.delete_front()
        raise AssertionError  # This should not happen
    except IndexError:
        logger.error("Exception in test_circular_linked_list()", exc_info=True)
        assert True  # This should happen

    try:
        circular_linked_list.delete_tail()
        raise AssertionError  # This should not happen
    except IndexError:
        assert True  # This should happen

    try:
        circular_linked_list.delete_nth(-1)
        raise AssertionError
    except IndexError:
        assert True

    try:
        circular_linked_list.delete_nth(0)
        raise AssertionError
    except IndexError:
        assert True

    assert circular_linked_list.is_empty() is True
    for i in range(5):
        assert len(circular_linked_list) == i
        circular_linked_list.insert_nth(i, i + 1)
    assert str(circular_linked_list) == "->".join(str(i) for i in range(1, 6))

    circular_linked_list.insert_tail(6)
    assert str(circular_linked_list) == "->".join(str(i) for i in range(1, 7))
    circular_linked_list.insert_head(0)
    assert str(circular_linked_list) == "->".join(str(i) for i in range(7))

    assert circular_linked_list.delete_front() == 0
    assert circular_linked_list.delete_tail() == 6
    assert str(circular_linked_list) == "->".join(str(i) for i in range(1, 6))
    assert circular_linked_list.delete_nth(2) == 3

    circular_linked_list.insert_nth(2, 3)
    assert str(circular_linked_list) == "->".join(str(i) for i in range(1, 6))

    assert circular_linked_list.is_empty() is False
    logger.debug("<<< Exiting test_circular_linked_list()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
