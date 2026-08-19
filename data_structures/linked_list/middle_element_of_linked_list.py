from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data: int) -> None:
        logger.debug(">>> Entering __init__(data=%s)", data)
        self.data = data
        logger.debug("__init__(data=%s): self.data → %s", data, self.data)
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data)
        self.next = None
        logger.debug("__init__(self=%s,data=%s): self.next → %s", self, data, self.next)

        logger.debug("<<< Exiting __init__(data=%s)", data)
        logger.debug(">>> Entering __init__()")
        logger.debug("<<< Exiting __init__()")

class LinkedList:
    def __init__(self):
        self.head = None
        logger.debug("__init__(self=%s): self.head → %s", self, self.head)

    def push(self, new_data: int) -> int:
        logger.debug(">>> Entering push(new_data=%s)", new_data)
        new_node = Node(new_data)
        logger.debug("push(new_data=%s): new_node → %s", new_data, new_node)
        logger.debug("push(self=%s,new_data=%s): new_node → %s", self, new_data, new_node)
        new_node.next = self.head
        logger.debug("push(self=%s,new_data=%s): new_node.next → %s", self, new_data, new_node.next)
        self.head = new_node
        logger.debug("push(self=%s,new_data=%s): self.head → %s", self, new_data, self.head)
        logger.debug("<<< Exiting push(new_data=%s)", new_data)
        return self.head.data

    def middle_element(self) -> int | None:
        """
        >>> link = LinkedList()
        >>> link.middle_element()
        No element found.
        >>> link.push(5)
        5
        >>> link.push(6)
        6
        >>> link.push(8)
        8
        >>> link.push(8)
        8
        >>> link.push(10)
        10
        >>> link.push(12)
        12
        >>> link.push(17)
        17
        >>> link.push(7)
        7
        >>> link.push(3)
        3
        >>> link.push(20)
        20
        >>> link.push(-20)
        -20
        >>> link.middle_element()
        12
        >>>
        """
        logger.debug(">>> Entering middle_element()")
        slow_pointer = self.head
        logger.debug("middle_element(self=%s): slow_pointer → %s", self, slow_pointer)
        fast_pointer = self.head
        logger.debug("middle_element(self=%s): fast_pointer → %s", self, fast_pointer)
        if self.head:
            while fast_pointer and fast_pointer.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            return slow_pointer.data
        else:
            print("No element found.")
            logger.debug("<<< Exiting middle_element()")
            return None


if __name__ == "__main__":
    link = LinkedList()
    for _ in range(int(input().strip())):
        data = int(input().strip())
        link.push(data)
    print(link.middle_element())
