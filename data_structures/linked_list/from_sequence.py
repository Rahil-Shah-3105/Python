"""
Recursive Program to create a Linked List from a sequence and
print a string representation of it.
"""
import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data=None):
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): data → %s", data, data, extra={"event.action": "__init__"})
        self.data = data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        self.next = None
        logger.debug("__init__(self=%s,data=%s): self.next → %s", self, data, self.next, extra={"event.action": "__init__"})

    def __repr__(self):
        """Returns a visual representation of the node and all its following nodes."""
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        string_rep = ""
        logger.error("__repr__(): string_rep → %s", string_rep, extra={"event.action": "__repr__"})
        temp = self
        while temp:
            string_rep += f"<{temp.data}> ---> "
            temp = temp.next
        string_rep += "<END>"
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return string_rep


def make_linked_list(elements_list: list | tuple) -> Node:
    """
    Creates a Linked List from the elements of the given sequence
    (list/tuple) and returns the head of the Linked List.

    >>> make_linked_list([])
    Traceback (most recent call last):
        ...
    ValueError: The Elements List is empty
    >>> make_linked_list(())
    Traceback (most recent call last):
        ...
    ValueError: The Elements List is empty
    >>> make_linked_list([1])
    <1> ---> <END>
    >>> make_linked_list((1,))
    <1> ---> <END>
    >>> make_linked_list([1, 3, 5, 32, 44, 12, 43])
    <1> ---> <3> ---> <5> ---> <32> ---> <44> ---> <12> ---> <43> ---> <END>
    >>> make_linked_list((1, 3, 5, 32, 44, 12, 43))
    <1> ---> <3> ---> <5> ---> <32> ---> <44> ---> <12> ---> <43> ---> <END>
    """
    logger.error(">>> Entering make_linked_list(elements_list=%s)", elements_list, extra={"event.action": "make_linked_list", "logrite.elements_list": elements_list})

    # if elements_list is empty
    if not elements_list:
        raise ValueError("The Elements List is empty")

    # Set first element as Head
    head = Node(elements_list[0])
    logger.error("make_linked_list(elements_list=%s): head → %s", elements_list, head, extra={"event.action": "make_linked_list", "logrite.elements_list": elements_list})
    current = head
    # Loop through elements from position 1
    for data in elements_list[1:]:
        current.next = Node(data)
        current = current.next
    logger.warning("<<< Exiting make_linked_list(elements_list=%s)", elements_list, extra={"event.action": "make_linked_list", "logrite.elements_list": elements_list})
    return head
