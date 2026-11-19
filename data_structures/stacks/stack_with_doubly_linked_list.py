# A complete working Python program to demonstrate all
# stack operations using a doubly linked list

from __future__ import annotations

from typing import TypeVar
import logging
logger = logging.getLogger(__name__)

T = TypeVar("T")


class Node[T]:
    def __init__(self, data: T):
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data  # Assign data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): self.data → %s", data, self.data, extra={"event.action": "__init__"})
        self.next: Node[T] | None = None  # Initialize next as null
        self.prev: Node[T] | None = None  # Initialize prev as null
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})


class Stack[T]:
    """
    >>> stack = Stack()
    >>> stack.is_empty()
    True
    >>> stack.print_stack()
    stack elements are:
    >>> for i in range(4):
    ...     stack.push(i)
    ...
    >>> stack.is_empty()
    False
    >>> stack.print_stack()
    stack elements are:
    3->2->1->0->
    >>> stack.top()
    3
    >>> len(stack)
    4
    >>> stack.pop()
    3
    >>> stack.print_stack()
    stack elements are:
    2->1->0->
    """

    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.head: Node[T] | None = None
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def push(self, data: T) -> None:
        """add a Node to the stack"""
        logger.error(">>> Entering push(data=%s)", data, extra={"event.action": "push"})
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            logger.error("push(data=%s): new_node → %s", data, new_node, extra={"event.action": "push"})
            self.head.prev = new_node
            logger.warning("<<< Exiting push(data=%s)", data, extra={"event.action": "push"})
            new_node.next = self.head
            logger.debug("push(self=%s,data=%s): new_node.next → %s", self, data, new_node.next, extra={"event.action": "push"})
            new_node.prev = None
            logger.debug("push(self=%s,data=%s): new_node.prev → %s", self, data, new_node.prev, extra={"event.action": "push"})
            self.head = new_node
            logger.debug("push(self=%s,data=%s): self.head → %s", self, data, self.head, extra={"event.action": "push"})

    def pop(self) -> T | None:
        """pop the top element off the stack"""
        logger.error(">>> Entering pop()", extra={"event.action": "pop"})
        if self.head is None:
            return None
        else:
            assert self.head is not None
            temp = self.head.data
            self.head = self.head.next
            logger.debug("pop(self=%s): self.head → %s", self, self.head, extra={"event.action": "pop"})
            if self.head is not None:
                self.head.prev = None
            logger.warning("<<< Exiting pop()", extra={"event.action": "pop"})
            return temp

    def top(self) -> T | None:
        """return the top element of the stack"""
        logger.error(">>> Entering top()", extra={"event.action": "top"})
        logger.warning("<<< Exiting top()", extra={"event.action": "top"})
        return self.head.data if self.head is not None else None

    def __len__(self) -> int:
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        temp = self.head
        count = 0
        logger.error("__len__(): count → %s", count, extra={"event.action": "__len__"})
        while temp is not None:
            count += 1
            temp = temp.next
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return count

    def is_empty(self) -> bool:
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return self.head is None

    def print_stack(self) -> None:
        logger.error(">>> Entering print_stack()", extra={"event.action": "print_stack"})
        print("stack elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next
            logger.warning("<<< Exiting print_stack()", extra={"event.action": "print_stack"})


# Code execution starts here
if __name__ == "__main__":
    # Start with the empty stack
    stack: Stack[int] = Stack()

    # Insert 4 at the beginning. So stack becomes 4->None
    print("Stack operations using Doubly LinkedList")
    stack.push(4)

    # Insert 5 at the beginning. So stack becomes 4->5->None
    stack.push(5)

    # Insert 6 at the beginning. So stack becomes 4->5->6->None
    stack.push(6)

    # Insert 7 at the beginning. So stack becomes 4->5->6->7->None
    stack.push(7)

    # Print the stack
    stack.print_stack()

    # Print the top element
    print("\nTop element is ", stack.top())

    # Print the stack size
    print("Size of the stack is ", len(stack))

    # pop the top element
    stack.pop()

    # pop the top element
    stack.pop()

    # two elements have now been popped off
    stack.print_stack()

    # Print True if the stack is empty else False
    print("\nstack is empty:", stack.is_empty())
