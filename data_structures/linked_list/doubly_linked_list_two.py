"""
- A linked list is similar to an array, it holds values. However, links in a linked
    list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous
    pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - It can be traversed in both forward and backward direction.
     Delete operation is more efficient
"""

from dataclasses import dataclass
from typing import Self, TypeVar
import logging
logger = logging.getLogger(__name__)

DataType = TypeVar("DataType")


@dataclass
class Node[DataType]:
    data: DataType
    previous: Self | None = None
    next: Self | None = None

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return f"{self.data}"


class LinkedListIterator:
    def __init__(self, head):
        logger.error(">>> Entering __init__(head=%s)", head, extra={"event.action": "__init__", "logrite.head": head})
        self.current = head
        logger.warning("<<< Exiting __init__(head=%s)", head, extra={"event.action": "__init__", "logrite.head": head})
        logger.debug("__init__(self=%s,head=%s): self.current → %s", self, head, self.current, extra={"event.action": "__init__", "logrite.head": head})

    def __iter__(self):
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})
        return self

    def __next__(self):
        logger.error(">>> Entering __next__()", extra={"event.action": "__next__"})
        if not self.current:
            raise StopIteration
        else:
            value = self.current.data
            self.current = self.current.next
            logger.debug("__next__(self=%s): self.current → %s", self, self.current, extra={"event.action": "__next__"})
            logger.warning("<<< Exiting __next__()", extra={"event.action": "__next__"})
            return value


@dataclass
class LinkedList:
    head: Node | None = None  # First node in list
    tail: Node | None = None  # Last node in list

    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current.data)
            current = current.next
        return " ".join(str(node) for node in nodes)

    def __contains__(self, value: DataType):
        logger.error(">>> Entering __contains__(value=%s)", value, extra={"event.action": "__contains__", "logrite.value": value})
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        logger.warning("<<< Exiting __contains__(value=%s)", value, extra={"event.action": "__contains__", "logrite.value": value})
        return False

    def __iter__(self):
        return LinkedListIterator(self.head)

    def get_head_data(self):
        logger.error(">>> Entering get_head_data()", extra={"event.action": "get_head_data"})
        if self.head:
            return self.head.data
        logger.warning("<<< Exiting get_head_data()", extra={"event.action": "get_head_data"})
        return None

    def get_tail_data(self):
        logger.error(">>> Entering get_tail_data()", extra={"event.action": "get_tail_data"})
        if self.tail:
            return self.tail.data
        logger.warning("<<< Exiting get_tail_data()", extra={"event.action": "get_tail_data"})
        return None

    def set_head(self, node: Node) -> None:
        logger.error(">>> Entering set_head(node=%s)", node, extra={"event.action": "set_head", "logrite.node": node})
        if self.head is None:
            self.head = node
            logger.debug("set_head(self=%s,node=%s): self.head → %s", self, node, self.head, extra={"event.action": "set_head", "logrite.node": node})
            self.tail = node
        else:
            logger.debug("set_head(self=%s,node=%s): self.tail → %s", self, node, self.tail, extra={"event.action": "set_head", "logrite.node": node})
            self.insert_before_node(self.head, node)
            logger.warning("<<< Exiting set_head(node=%s)", node, extra={"event.action": "set_head", "logrite.node": node})

    def set_tail(self, node: Node) -> None:
        logger.error(">>> Entering set_tail(node=%s)", node, extra={"event.action": "set_tail", "logrite.node": node})
        if self.tail is None:
            self.head = node
            logger.debug("set_tail(self=%s,node=%s): self.head → %s", self, node, self.head, extra={"event.action": "set_tail", "logrite.node": node})
            self.tail = node
        else:
            logger.debug("set_tail(self=%s,node=%s): self.tail → %s", self, node, self.tail, extra={"event.action": "set_tail", "logrite.node": node})
            self.insert_after_node(self.tail, node)
            logger.warning("<<< Exiting set_tail(node=%s)", node, extra={"event.action": "set_tail", "logrite.node": node})

    def insert(self, value: DataType) -> None:
        logger.error(">>> Entering insert(value=%s)", value, extra={"event.action": "insert", "logrite.value": value})
        node = Node(value)
        logger.error("insert(value=%s): node → %s", value, node, extra={"event.action": "insert", "logrite.value": value})
        if self.head is None:
            self.set_head(node)
        else:
            self.set_tail(node)
            logger.warning("<<< Exiting insert(value=%s)", value, extra={"event.action": "insert", "logrite.value": value})

    def insert_before_node(self, node: Node, node_to_insert: Node) -> None:
        logger.error(">>> Entering insert_before_node(node=%s,node_to_insert=%s)", node, node_to_insert, extra={"event.action": "insert_before_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
        node_to_insert.next = node
        logger.debug("insert_before_node(self=%s,node=%s,node_to_insert=%s): node_to_insert.next → %s", self, node, node_to_insert, node_to_insert.next, extra={"event.action": "insert_before_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
        node_to_insert.previous = node.previous
        logger.debug("insert_before_node(self=%s,node=%s,node_to_insert=%s): node_to_insert.previous → %s", self, node, node_to_insert, node_to_insert.previous, extra={"event.action": "insert_before_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})

        if node.previous is None:
            self.head = node_to_insert
        else:
            logger.debug("insert_before_node(self=%s,node=%s,node_to_insert=%s): self.head → %s", self, node, node_to_insert, self.head, extra={"event.action": "insert_before_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
            node.previous.next = node_to_insert

            logger.warning("<<< Exiting insert_before_node(node=%s,node_to_insert=%s)", node, node_to_insert, extra={"event.action": "insert_before_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
        node.previous = node_to_insert
        logger.debug("insert_before_node(self=%s,node=%s,node_to_insert=%s): node.previous → %s", self, node, node_to_insert, node.previous, extra={"event.action": "insert_before_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})

    def insert_after_node(self, node: Node, node_to_insert: Node) -> None:
        logger.error(">>> Entering insert_after_node(node=%s,node_to_insert=%s)", node, node_to_insert, extra={"event.action": "insert_after_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
        node_to_insert.previous = node
        logger.debug("insert_after_node(self=%s,node=%s,node_to_insert=%s): node_to_insert.previous → %s", self, node, node_to_insert, node_to_insert.previous, extra={"event.action": "insert_after_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
        node_to_insert.next = node.next
        logger.debug("insert_after_node(self=%s,node=%s,node_to_insert=%s): node_to_insert.next → %s", self, node, node_to_insert, node_to_insert.next, extra={"event.action": "insert_after_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})

        if node.next is None:
            self.tail = node_to_insert
        else:
            logger.debug("insert_after_node(self=%s,node=%s,node_to_insert=%s): self.tail → %s", self, node, node_to_insert, self.tail, extra={"event.action": "insert_after_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
            node.next.previous = node_to_insert

            logger.warning("<<< Exiting insert_after_node(node=%s,node_to_insert=%s)", node, node_to_insert, extra={"event.action": "insert_after_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})
        node.next = node_to_insert
        logger.debug("insert_after_node(self=%s,node=%s,node_to_insert=%s): node.next → %s", self, node, node_to_insert, node.next, extra={"event.action": "insert_after_node", "logrite.node": node, "logrite.node_to_insert": node_to_insert})

    def insert_at_position(self, position: int, value: DataType) -> None:
        logger.error(">>> Entering insert_at_position(position=%s,value=%s)", position, value, extra={"event.action": "insert_at_position", "logrite.position": position, "logrite.value": value})
        current_position = 1
        new_node = Node(value)
        logger.error("insert_at_position(position=%s,value=%s): new_node → %s", position, value, new_node, extra={"event.action": "insert_at_position", "logrite.position": position, "logrite.value": value})
        node = self.head
        while node:
            if current_position == position:
                self.insert_before_node(node, new_node)
                logger.warning("<<< Exiting insert_at_position(position=%s,value=%s)", position, value, extra={"event.action": "insert_at_position", "logrite.position": position, "logrite.value": value})
                return
            current_position += 1
            node = node.next
        self.set_tail(new_node)

    def get_node(self, item: DataType) -> Node:
        logger.error(">>> Entering get_node(item=%s)", item, extra={"event.action": "get_node", "logrite.item": item})
        node = self.head
        while node:
            if node.data == item:
                logger.warning("<<< Exiting get_node(item=%s)", item, extra={"event.action": "get_node", "logrite.item": item})
                return node
            node = node.next
        raise Exception("Node not found")

    def delete_value(self, value):
        logger.error(">>> Entering delete_value(value=%s)", value, extra={"event.action": "delete_value", "logrite.value": value})
        if (node := self.get_node(value)) is not None:
            if node == self.head:
                self.head = self.head.next
                logger.debug("delete_value(self=%s,value=%s): self.head → %s", self, value, self.head, extra={"event.action": "delete_value", "logrite.value": value})

            if node == self.tail:
                self.tail = self.tail.previous
                logger.debug("delete_value(self=%s,value=%s): self.tail → %s", self, value, self.tail, extra={"event.action": "delete_value", "logrite.value": value})

            self.remove_node_pointers(node)
            logger.warning("<<< Exiting delete_value(value=%s)", value, extra={"event.action": "delete_value", "logrite.value": value})

    @staticmethod
    def remove_node_pointers(node: Node) -> None:
        logger.error(">>> Entering remove_node_pointers(node=%s)", node, extra={"event.action": "remove_node_pointers", "logrite.node": node})
        if node.next:
            node.next.previous = node.previous

        if node.previous:
            node.previous.next = node.next

            logger.warning("<<< Exiting remove_node_pointers(node=%s)", node, extra={"event.action": "remove_node_pointers", "logrite.node": node})
        node.next = None
        logger.debug("remove_node_pointers(node=%s): node.next → %s", node, node.next, extra={"event.action": "remove_node_pointers", "logrite.node": node})
        node.previous = None
        logger.debug("remove_node_pointers(node=%s): node.previous → %s", node, node.previous, extra={"event.action": "remove_node_pointers", "logrite.node": node})

    def is_empty(self):
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return self.head is None


def create_linked_list() -> None:
    """
    >>> new_linked_list = LinkedList()
    >>> new_linked_list.get_head_data() is None
    True
    >>> new_linked_list.get_tail_data() is None
    True
    >>> new_linked_list.is_empty()
    True
    >>> new_linked_list.insert(10)
    >>> new_linked_list.get_head_data()
    10
    >>> new_linked_list.get_tail_data()
    10
    >>> new_linked_list.insert_at_position(position=3, value=20)
    >>> new_linked_list.get_head_data()
    10
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.set_head(Node(1000))
    >>> new_linked_list.get_head_data()
    1000
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.set_tail(Node(2000))
    >>> new_linked_list.get_head_data()
    1000
    >>> new_linked_list.get_tail_data()
    2000
    >>> for value in new_linked_list:
    ...    print(value)
    1000
    10
    20
    2000
    >>> new_linked_list.is_empty()
    False
    >>> for value in new_linked_list:
    ...    print(value)
    1000
    10
    20
    2000
    >>> 10 in new_linked_list
    True
    >>> new_linked_list.delete_value(value=10)
    >>> 10 in new_linked_list
    False
    >>> new_linked_list.delete_value(value=2000)
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.delete_value(value=1000)
    >>> new_linked_list.get_tail_data()
    20
    >>> new_linked_list.get_head_data()
    20
    >>> for value in new_linked_list:
    ...    print(value)
    20
    >>> new_linked_list.delete_value(value=20)
    >>> for value in new_linked_list:
    ...    print(value)
    >>> for value in range(1,10):
    ...    new_linked_list.insert(value=value)
    >>> for value in new_linked_list:
    ...    print(value)
    1
    2
    3
    4
    5
    6
    7
    8
    9
    >>> linked_list = LinkedList()
    >>> linked_list.insert_at_position(position=1, value=10)
    >>> str(linked_list)
    '10'
    >>> linked_list.insert_at_position(position=2, value=20)
    >>> str(linked_list)
    '10 20'
    >>> linked_list.insert_at_position(position=1, value=30)
    >>> str(linked_list)
    '30 10 20'
    >>> linked_list.insert_at_position(position=3, value=40)
    >>> str(linked_list)
    '30 10 40 20'
    >>> linked_list.insert_at_position(position=5, value=50)
    >>> str(linked_list)
    '30 10 40 20 50'
    """
    logger.error(">>> Entering create_linked_list()", extra={"event.action": "create_linked_list"})
    logger.debug("create_linked_list(): new_linked_list → %s", new_linked_list, extra={"event.action": "create_linked_list"})

    logger.warning("<<< Exiting create_linked_list()", extra={"event.action": "create_linked_list"})

if __name__ == "__main__":
    import doctest

    doctest.testmod()
