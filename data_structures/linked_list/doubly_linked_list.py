import logging
logger = logging.getLogger(__name__)
"""
https://en.wikipedia.org/wiki/Doubly_linked_list
"""


class Node:
    def __init__(self, data):
        logger.debug(">>> Entering __init__(data=%s)", data)
        self.data = data
        logger.debug("__init__(data=%s): self.data → %s", data, self.data)
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data)
        self.previous = None
        logger.debug("__init__(self=%s,data=%s): self.previous → %s", self, data, self.previous)
        self.next = None
        logger.debug("__init__(self=%s,data=%s): self.next → %s", self, data, self.next)
        logger.debug("<<< Exiting __init__(data=%s)", data)
        logger.debug(">>> Entering __init__()")
        logger.debug("__init__(self=%s): self.head → %s", self, self.head)
        logger.debug("<<< Exiting __init__()")

    def __str__(self):
        logger.debug(">>> Entering __str__()")
        logger.debug("<<< Exiting __str__()")
        return f"{self.data}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        logger.debug("__init__(self=%s): self.tail → %s", self, self.tail)

    def __iter__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_head('b')
        >>> linked_list.insert_at_head('a')
        >>> linked_list.insert_at_tail('c')
        >>> tuple(linked_list)
        ('a', 'b', 'c')
        """
        logger.debug(">>> Entering __iter__()")
        node = self.head
        logger.debug("__iter__(self=%s): node → %s", self, node)
        while node:
            yield node.data
            logger.debug("<<< Exiting __iter__()")
            node = node.next

    def __str__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_tail('a')
        >>> linked_list.insert_at_tail('b')
        >>> linked_list.insert_at_tail('c')
        >>> str(linked_list)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> for i in range(0, 5):
        ...     linked_list.insert_at_nth(i, i + 1)
        >>> len(linked_list) == 5
        True
        """
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return sum(1 for _ in self)

    def insert_at_head(self, data):
        logger.debug(">>> Entering insert_at_head(data=%s)", data)
        self.insert_at_nth(0, data)
        logger.debug("<<< Exiting insert_at_head(data=%s)", data)

    def insert_at_tail(self, data):
        logger.debug(">>> Entering insert_at_tail(data=%s)", data)
        self.insert_at_nth(len(self), data)
        logger.debug("<<< Exiting insert_at_tail(data=%s)", data)

    def insert_at_nth(self, index: int, data):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_nth(-1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(0, 2)
        >>> linked_list.insert_at_nth(0, 1)
        >>> linked_list.insert_at_nth(2, 4)
        >>> linked_list.insert_at_nth(2, 3)
        >>> str(linked_list)
        '1->2->3->4'
        >>> linked_list.insert_at_nth(5, 5)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        """
        logger.debug(">>> Entering insert_at_nth(index=%s,data=%s)", index, data)
        length = len(self)
        logger.debug("insert_at_nth(index=%s,data=%s): length → %s", index, data, length)
        logger.debug("insert_at_nth(self=%s,index=%s,data=%s): length → %s", self, index, data, length)

        if not 0 <= index <= length:
            raise IndexError("list index out of range")
        new_node = Node(data)
        logger.debug("insert_at_nth(self=%s,index=%s,data=%s): new_node → %s", self, index, data, new_node)
        logger.debug("insert_at_nth(index=%s,data=%s): new_node → %s", index, data, new_node)
        if self.head is None:
            self.head = self.tail = new_node
            logger.debug("insert_at_nth(self=%s,index=%s,data=%s): self.head → %s", self, index, data, self.head)
        elif index == 0:
            self.head.previous = new_node
            new_node.next = self.head
            logger.debug("insert_at_nth(self=%s,index=%s,data=%s): new_node.next → %s", self, index, data, new_node.next)
            self.head = new_node
        elif index == length:
            self.tail.next = new_node
            new_node.previous = self.tail
            logger.debug("insert_at_nth(self=%s,index=%s,data=%s): new_node.previous → %s", self, index, data, new_node.previous)
            self.tail = new_node
            logger.debug("insert_at_nth(self=%s,index=%s,data=%s): self.tail → %s", self, index, data, self.tail)
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.previous.next = new_node
            logger.debug("<<< Exiting insert_at_nth(index=%s,data=%s)", index, data)
            new_node.previous = temp.previous
            new_node.next = temp
            temp.previous = new_node
            logger.debug("insert_at_nth(self=%s,index=%s,data=%s): temp.previous → %s", self, index, data, temp.previous)

    def delete_head(self):
        logger.debug(">>> Entering delete_head()")
        logger.debug("<<< Exiting delete_head()")
        return self.delete_at_nth(0)

    def delete_tail(self):
        logger.debug(">>> Entering delete_tail()")
        logger.debug("<<< Exiting delete_tail()")
        return self.delete_at_nth(len(self) - 1)

    def delete_at_nth(self, index: int):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.delete_at_nth(0)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> for i in range(0, 5):
        ...     linked_list.insert_at_nth(i, i + 1)
        >>> linked_list.delete_at_nth(0) == 1
        True
        >>> linked_list.delete_at_nth(3) == 5
        True
        >>> linked_list.delete_at_nth(1) == 3
        True
        >>> str(linked_list)
        '2->4'
        >>> linked_list.delete_at_nth(2)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        """
        logger.debug(">>> Entering delete_at_nth(index=%s)", index)
        length = len(self)
        logger.debug("delete_at_nth(index=%s): length → %s", index, length)

        if not 0 <= index <= length - 1:
            raise IndexError("list index out of range")
        delete_node = self.head  # default first node
        logger.debug("delete_at_nth(self=%s,index=%s): delete_node → %s", self, index, delete_node)
        if length == 1:
            self.head = self.tail = None
            logger.debug("delete_at_nth(self=%s,index=%s): self.head → %s", self, index, self.head)
        elif index == 0:
            self.head = self.head.next
            self.head.previous = None
        elif index == length - 1:
            delete_node = self.tail
            self.tail = self.tail.previous
            logger.debug("delete_at_nth(self=%s,index=%s): self.tail → %s", self, index, self.tail)
            self.tail.next = None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            delete_node = temp
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
        logger.debug("<<< Exiting delete_at_nth(index=%s)", index)
        return delete_node.data

    def delete(self, data) -> str:
        logger.debug(">>> Entering delete(data=%s)", data)
        current = self.head

        while current.data != data:  # Find the position to delete
            if current.next:
                current = current.next
            else:  # We have reached the end an no value matches
                raise ValueError("No data matching given value")

        if current == self.head:
            self.delete_head()

        elif current == self.tail:
            self.delete_tail()

        else:  # Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next  # 1 --> 3
            current.next.previous = current.previous  # 1 <--> 3
        logger.debug("<<< Exiting delete(data=%s)", data)
        return data

    def is_empty(self):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_at_tail(1)
        >>> linked_list.is_empty()
        False
        """
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return len(self) == 0


def test_doubly_linked_list() -> None:
    """
    >>> test_doubly_linked_list()
    """
    logger.debug(">>> Entering test_doubly_linked_list()")
    linked_list = DoublyLinkedList()
    logger.debug("test_doubly_linked_list(): linked_list → %s", linked_list)
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        raise AssertionError  # This should not happen.
    except IndexError:
        logger.error("Exception in test_doubly_linked_list()", exc_info=True)
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        raise AssertionError  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_at_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_at_head(0)
    linked_list.insert_at_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_at_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))
    logger.debug("<<< Exiting test_doubly_linked_list()")


if __name__ == "__main__":
    from doctest import testmod

    testmod()
