from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    """
    Create and initialize Node class instance.
    >>> Node(20)
    Node(20)
    >>> Node("Hello, world!")
    Node(Hello, world!)
    >>> Node(None)
    Node(None)
    >>> Node(True)
    Node(True)
    """

    data: Any
    next_node: Node | None = None

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        >>> Node(10).__repr__()
        'Node(10)'
        >>> repr(Node(10))
        'Node(10)'
        >>> str(Node(10))
        'Node(10)'
        >>> Node(10)
        Node(10)
        """
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return f"Node({self.data})"


class LinkedList:
    def __init__(self):
        """
        Create and initialize LinkedList class instance.
        >>> linked_list = LinkedList()
        >>> linked_list.head is None
        True
        """
        logger.debug(">>> Entering __init__()")
        self.head = None
        logger.debug("__init__(self=%s): self.head → %s", self, self.head)
        logger.debug("<<< Exiting __init__()")

    def __iter__(self) -> Iterator[Any]:
        """
        This function is intended for iterators to access
        and iterate through data inside linked list.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("tail")
        >>> linked_list.insert_tail("tail_1")
        >>> linked_list.insert_tail("tail_2")
        >>> for node in linked_list: # __iter__ used here.
        ...     node
        'tail'
        'tail_1'
        'tail_2'
        """
        logger.debug(">>> Entering __iter__()")
        node = self.head
        logger.debug("__iter__(self=%s): node → %s", self, node)
        while node:
            yield node.data
            logger.debug("<<< Exiting __iter__()")
            node = node.next_node

    def __len__(self) -> int:
        """
        Return length of linked list i.e. number of nodes
        >>> linked_list = LinkedList()
        >>> len(linked_list)
        0
        >>> linked_list.insert_tail("tail")
        >>> len(linked_list)
        1
        >>> linked_list.insert_head("head")
        >>> len(linked_list)
        2
        >>> _ = linked_list.delete_tail()
        >>> len(linked_list)
        1
        >>> _ = linked_list.delete_head()
        >>> len(linked_list)
        0
        """
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return sum(1 for _ in self)

    def __repr__(self) -> str:
        """
        String representation/visualization of a Linked Lists
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail(1)
        >>> linked_list.insert_tail(3)
        >>> linked_list.__repr__()
        '1 -> 3'
        >>> repr(linked_list)
        '1 -> 3'
        >>> str(linked_list)
        '1 -> 3'
        >>> linked_list.insert_tail(5)
        >>> f"{linked_list}"
        '1 -> 3 -> 5'
        """
        return " -> ".join([str(item) for item in self])

    def __getitem__(self, index: int) -> Any:
        """
        Indexing Support. Used to get a node at particular position
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> all(str(linked_list[i]) == str(i) for i in range(0, 10))
        True
        >>> linked_list[-10]
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        >>> linked_list[len(linked_list)]
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        """
        logger.debug(">>> Entering __getitem__(index=%s)", index)
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i, node in enumerate(self):
            if i == index:
                return node
        logger.debug("<<< Exiting __getitem__(index=%s)", index)
        return None

    # Used to change the data of a particular node
    def __setitem__(self, index: int, data: Any) -> None:
        """
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> linked_list[0] = 666
        >>> linked_list[0]
        666
        >>> linked_list[5] = -666
        >>> linked_list[5]
        -666
        >>> linked_list[-10] = 666
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        >>> linked_list[len(linked_list)] = 666
        Traceback (most recent call last):
            ...
        ValueError: list index out of range.
        """
        logger.debug(">>> Entering __setitem__(index=%s,data=%s)", index, data)
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        logger.debug("__setitem__(self=%s,index=%s,data=%s): current → %s", self, index, data, current)
        for _ in range(index):
            logger.debug("<<< Exiting __setitem__(index=%s,data=%s)", index, data)
            current = current.next_node
        current.data = data
        logger.debug("__setitem__(self=%s,index=%s,data=%s): current.data → %s", self, index, data, current.data)

    def insert_tail(self, data: Any) -> None:
        """
        Insert data to the end of linked list.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("tail")
        >>> linked_list
        tail
        >>> linked_list.insert_tail("tail_2")
        >>> linked_list
        tail -> tail_2
        >>> linked_list.insert_tail("tail_3")
        >>> linked_list
        tail -> tail_2 -> tail_3
        """
        logger.debug(">>> Entering insert_tail(data=%s)", data)
        self.insert_nth(len(self), data)
        logger.debug("<<< Exiting insert_tail(data=%s)", data)

    def insert_head(self, data: Any) -> None:
        """
        Insert data to the beginning of linked list.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_head("head")
        >>> linked_list
        head
        >>> linked_list.insert_head("head_2")
        >>> linked_list
        head_2 -> head
        >>> linked_list.insert_head("head_3")
        >>> linked_list
        head_3 -> head_2 -> head
        """
        logger.debug(">>> Entering insert_head(data=%s)", data)
        self.insert_nth(0, data)
        logger.debug("<<< Exiting insert_head(data=%s)", data)

    def insert_nth(self, index: int, data: Any) -> None:
        """
        Insert data at given index.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.insert_nth(1, "fourth")
        >>> linked_list
        first -> fourth -> second -> third
        >>> linked_list.insert_nth(3, "fifth")
        >>> linked_list
        first -> fourth -> second -> fifth -> third
        """
        logger.debug(">>> Entering insert_nth(index=%s,data=%s)", index, data)
        if not 0 <= index <= len(self):
            raise IndexError("list index out of range")
        new_node = Node(data)
        logger.debug("insert_nth(self=%s,index=%s,data=%s): new_node → %s", self, index, data, new_node)
        logger.debug("insert_nth(index=%s,data=%s): new_node → %s", index, data, new_node)
        if self.head is None:
            self.head = new_node
            logger.debug("insert_nth(self=%s,index=%s,data=%s): self.head → %s", self, index, data, self.head)
        elif index == 0:
            new_node.next_node = self.head  # link new_node to head
            logger.debug("insert_nth(self=%s,index=%s,data=%s): new_node.next_node → %s", self, index, data, new_node.next_node)
            self.head = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next_node
                logger.debug("<<< Exiting insert_nth(index=%s,data=%s)", index, data)
            new_node.next_node = temp.next_node
            temp.next_node = new_node
            logger.debug("insert_nth(self=%s,index=%s,data=%s): temp.next_node → %s", self, index, data, temp.next_node)

    def print_list(self) -> None:  # print every node data
        """
        This method prints every node data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        """
        logger.debug(">>> Entering print_list()")
        logger.debug("<<< Exiting print_list()")
        print(self)

    def delete_head(self) -> Any:
        """
        Delete the first node and return the
        node's data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.delete_head()
        'first'
        >>> linked_list
        second -> third
        >>> linked_list.delete_head()
        'second'
        >>> linked_list
        third
        >>> linked_list.delete_head()
        'third'
        >>> linked_list.delete_head()
        Traceback (most recent call last):
            ...
        IndexError: List index out of range.
        """
        logger.debug(">>> Entering delete_head()")
        logger.debug("<<< Exiting delete_head()")
        return self.delete_nth(0)

    def delete_tail(self) -> Any:  # delete from tail
        """
        Delete the tail end node and return the
        node's data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.delete_tail()
        'third'
        >>> linked_list
        first -> second
        >>> linked_list.delete_tail()
        'second'
        >>> linked_list
        first
        >>> linked_list.delete_tail()
        'first'
        >>> linked_list.delete_tail()
        Traceback (most recent call last):
            ...
        IndexError: List index out of range.
        """
        logger.debug(">>> Entering delete_tail()")
        logger.debug("<<< Exiting delete_tail()")
        return self.delete_nth(len(self) - 1)

    def delete_nth(self, index: int = 0) -> Any:
        """
        Delete node at given index and return the
        node's data.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.delete_nth(1) # delete middle
        'second'
        >>> linked_list
        first -> third
        >>> linked_list.delete_nth(5) # this raises error
        Traceback (most recent call last):
            ...
        IndexError: List index out of range.
        >>> linked_list.delete_nth(-1) # this also raises error
        Traceback (most recent call last):
            ...
        IndexError: List index out of range.
        """
        logger.debug(">>> Entering delete_nth(index=%s)", index)
        if not 0 <= index <= len(self) - 1:  # test if index is valid
            raise IndexError("List index out of range.")
        delete_node = self.head  # default first node
        logger.debug("delete_nth(self=%s,index=%s): delete_node → %s", self, index, delete_node)
        if index == 0:
            self.head = self.head.next_node
            logger.debug("delete_nth(self=%s,index=%s): self.head → %s", self, index, self.head)
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next_node
            delete_node = temp.next_node
            temp.next_node = temp.next_node.next_node
            logger.debug("delete_nth(self=%s,index=%s): temp.next_node → %s", self, index, temp.next_node)
        logger.debug("<<< Exiting delete_nth(index=%s)", index)
        return delete_node.data

    def is_empty(self) -> bool:
        """
        Check if linked list is empty.
        >>> linked_list = LinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_head("first")
        >>> linked_list.is_empty()
        False
        """
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return self.head is None

    def reverse(self) -> None:
        """
        This reverses the linked list order.
        >>> linked_list = LinkedList()
        >>> linked_list.insert_tail("first")
        >>> linked_list.insert_tail("second")
        >>> linked_list.insert_tail("third")
        >>> linked_list
        first -> second -> third
        >>> linked_list.reverse()
        >>> linked_list
        third -> second -> first
        """
        logger.debug(">>> Entering reverse()")
        prev = None
        logger.debug("reverse(self=%s): prev → %s", self, prev)
        current = self.head
        logger.debug("reverse(self=%s): current → %s", self, current)

        while current:
            # Store the current node's next node.
            next_node = current.next_node
            logger.debug("reverse(self=%s): next_node → %s", self, next_node)
            # Make the current node's next_node point backwards
            current.next_node = prev
            logger.debug("reverse(self=%s): current.next_node → %s", self, current.next_node)
            # Make the previous node be the current node
            prev = current
            # Make the current node the next_node node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        logger.debug("<<< Exiting reverse()")
        self.head = prev
        logger.debug("reverse(self=%s): self.head → %s", self, self.head)


def test_singly_linked_list() -> None:
    """
    >>> test_singly_linked_list()
    """
    logger.debug(">>> Entering test_singly_linked_list()")
    linked_list = LinkedList()
    logger.debug("test_singly_linked_list(): linked_list → %s", linked_list)
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        raise AssertionError  # This should not happen.
    except IndexError:
        logger.error("Exception in test_singly_linked_list()", exc_info=True)
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        raise AssertionError  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_nth(i, i + 1)
    assert str(linked_list) == " -> ".join(str(i) for i in range(1, 11))

    linked_list.insert_head(0)
    linked_list.insert_tail(11)
    assert str(linked_list) == " -> ".join(str(i) for i in range(12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == " -> ".join(str(i) for i in range(1, 10))

    assert all(linked_list[i] == i + 1 for i in range(9)) is True

    for i in range(9):
        linked_list[i] = -i
    assert all(linked_list[i] == -i for i in range(9)) is True

    linked_list.reverse()
    assert str(linked_list) == " -> ".join(str(i) for i in range(-8, 1))
    logger.debug("<<< Exiting test_singly_linked_list()")


def test_singly_linked_list_2() -> None:
    """
    This section of the test used varying data types for input.
    >>> test_singly_linked_list_2()
    """
    logger.debug(">>> Entering test_singly_linked_list_2()")
    test_input = [
    logger.debug("test_singly_linked_list_2(): test_input → %s", test_input)
        -9,
        100,
        Node(77345112),
        "dlrow olleH",
        7,
        5555,
        0,
        -192.55555,
        "Hello, world!",
        77.9,
        Node(10),
        None,
        None,
        12.20,
    ]
    linked_list = LinkedList()
    logger.debug("test_singly_linked_list_2(): linked_list → %s", linked_list)

    for i in test_input:
        linked_list.insert_tail(i)

    # Check if it's empty or not
    assert linked_list.is_empty() is False
    assert (
        str(linked_list)
        == "-9 -> 100 -> Node(77345112) -> dlrow olleH -> 7 -> 5555 -> "
        "0 -> -192.55555 -> Hello, world! -> 77.9 -> Node(10) -> None -> None -> 12.2"
    )

    # Delete the head
    result = linked_list.delete_head()
    logger.debug("test_singly_linked_list_2(): result → %s", result)
    assert result == -9
    assert (
        str(linked_list) == "100 -> Node(77345112) -> dlrow olleH -> 7 -> 5555 -> 0 -> "
        "-192.55555 -> Hello, world! -> 77.9 -> Node(10) -> None -> None -> 12.2"
    )

    # Delete the tail
    result = linked_list.delete_tail()
    assert result == 12.2
    assert (
        str(linked_list) == "100 -> Node(77345112) -> dlrow olleH -> 7 -> 5555 -> 0 -> "
        "-192.55555 -> Hello, world! -> 77.9 -> Node(10) -> None -> None"
    )

    # Delete a node in specific location in linked list
    result = linked_list.delete_nth(10)
    assert result is None
    assert (
        str(linked_list) == "100 -> Node(77345112) -> dlrow olleH -> 7 -> 5555 -> 0 -> "
        "-192.55555 -> Hello, world! -> 77.9 -> Node(10) -> None"
    )

    # Add a Node instance to its head
    linked_list.insert_head(Node("Hello again, world!"))
    assert (
        str(linked_list)
        == "Node(Hello again, world!) -> 100 -> Node(77345112) -> dlrow olleH -> "
        "7 -> 5555 -> 0 -> -192.55555 -> Hello, world! -> 77.9 -> Node(10) -> None"
    )

    # Add None to its tail
    linked_list.insert_tail(None)
    assert (
        str(linked_list)
        == "Node(Hello again, world!) -> 100 -> Node(77345112) -> dlrow olleH -> 7 -> "
        "5555 -> 0 -> -192.55555 -> Hello, world! -> 77.9 -> Node(10) -> None -> None"
    )

    # Reverse the linked list
    linked_list.reverse()
    assert (
        str(linked_list)
        == "None -> None -> Node(10) -> 77.9 -> Hello, world! -> -192.55555 -> 0 -> "
        "5555 -> 7 -> dlrow olleH -> Node(77345112) -> 100 -> Node(Hello again, world!)"
    )
    logger.debug("<<< Exiting test_singly_linked_list_2()")


def main():
    logger.debug(">>> Entering main()")
    from doctest import testmod

    testmod()

    linked_list = LinkedList()
    logger.debug("main(): linked_list → %s", linked_list)
    linked_list.insert_head(input("Inserting 1st at head ").strip())
    linked_list.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    linked_list.insert_tail(input("\nInserting 1st at tail ").strip())
    linked_list.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    print("\nDelete head")
    linked_list.delete_head()
    print("Delete tail")
    linked_list.delete_tail()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nReverse linked list")
    linked_list.reverse()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nString representation of linked list:")
    print(linked_list)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {linked_list[1]}")
    linked_list[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(linked_list)
    print(f"length of linked_list is : {len(linked_list)}")
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
