import logging
logger = logging.getLogger(__name__)
"""
Implementing Deque using DoublyLinkedList ...
Operations:
    1. insertion in the front -> O(1)
    2. insertion in the end -> O(1)
    3. remove from the front -> O(1)
    4. remove from the end -> O(1)
"""


class _DoublyLinkedBase:
    """A Private class (to be inherited)"""

    class _Node:
        __slots__ = "_data", "_next", "_prev"

        def __init__(self, link_p, element, link_n):
            logger.debug(">>> Entering __init__(link_p=%s,element=%s,link_n=%s)", link_p, element, link_n)
            self._prev = link_p
            logger.debug("__init__(self=%s,link_p=%s,element=%s,link_n=%s): self._prev → %s", self, link_p, element, link_n, self._prev)
            self._data = element
            logger.debug("__init__(link_p=%s,element=%s,link_n=%s): self._data → %s", link_p, element, link_n, self._data)
            logger.debug("__init__(self=%s,link_p=%s,element=%s,link_n=%s): self._data → %s", self, link_p, element, link_n, self._data)
            self._next = link_n
            logger.debug("__init__(self=%s,link_p=%s,element=%s,link_n=%s): self._next → %s", self, link_p, element, link_n, self._next)
            logger.debug(">>> Entering __init__()")
            logger.debug("__init__(): self._header → %s", self._header)
            logger.debug("__init__(): self._trailer → %s", self._trailer)
            logger.debug("<<< Exiting __init__(link_p=%s,element=%s,link_n=%s)", link_p, element, link_n)
            logger.debug("<<< Exiting __init__()")

        def has_next_and_prev(self):
            logger.debug(">>> Entering has_next_and_prev()")
            logger.debug("<<< Exiting has_next_and_prev()")
            return (
                f" Prev -> {self._prev is not None}, Next -> {self._next is not None}"
            )

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
        logger.debug("__init__(self=%s): self._size → %s", self, self._size)

    def __len__(self):
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return self._size

    def is_empty(self):
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return self.__len__() == 0

    def _insert(self, predecessor, e, successor):
        logger.debug(">>> Entering _insert(predecessor=%s,e=%s,successor=%s)", predecessor, e, successor)
        # Create new_node by setting it's prev.link -> header
        # setting it's next.link -> trailer
        new_node = self._Node(predecessor, e, successor)
        logger.debug("_insert(self=%s,predecessor=%s,e=%s,successor=%s): new_node → %s", self, predecessor, e, successor, new_node)
        logger.debug("_insert(predecessor=%s,e=%s,successor=%s): new_node → %s", predecessor, e, successor, new_node)
        predecessor._next = new_node
        logger.debug("_insert(self=%s,predecessor=%s,e=%s,successor=%s): predecessor._next → %s", self, predecessor, e, successor, predecessor._next)
        successor._prev = new_node
        logger.debug("_insert(self=%s,predecessor=%s,e=%s,successor=%s): successor._prev → %s", self, predecessor, e, successor, successor._prev)
        self._size += 1
        logger.debug("<<< Exiting _insert(predecessor=%s,e=%s,successor=%s)", predecessor, e, successor)
        return self

    def _delete(self, node):
        logger.debug(">>> Entering _delete(node=%s)", node)
        predecessor = node._prev
        logger.debug("_delete(self=%s,node=%s): predecessor → %s", self, node, predecessor)
        successor = node._next
        logger.debug("_delete(self=%s,node=%s): successor → %s", self, node, successor)

        predecessor._next = successor
        logger.debug("_delete(self=%s,node=%s): predecessor._next → %s", self, node, predecessor._next)
        successor._prev = predecessor
        logger.debug("_delete(self=%s,node=%s): successor._prev → %s", self, node, successor._prev)
        self._size -= 1
        temp = node._data
        node._prev = node._next = node._data = None
        logger.debug("_delete(self=%s,node=%s): node._prev → %s", self, node, node._prev)
        del node
        logger.debug("<<< Exiting _delete(node=%s)", node)
        return temp


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        """return first element
        >>> d = LinkedDeque()
        >>> d.add_first('A').first()
        'A'
        >>> d.add_first('B').first()
        'B'
        """
        logger.debug(">>> Entering first()")
        if self.is_empty():
            raise Exception("List is empty")
        logger.debug("<<< Exiting first()")
        return self._header._next._data

    def last(self):
        """return last element
        >>> d = LinkedDeque()
        >>> d.add_last('A').last()
        'A'
        >>> d.add_last('B').last()
        'B'
        """
        logger.debug(">>> Entering last()")
        if self.is_empty():
            raise Exception("List is empty")
        logger.debug("<<< Exiting last()")
        return self._trailer._prev._data

    # DEque Insert Operations (At the front, At the end)

    def add_first(self, element):
        """insertion in the front
        >>> LinkedDeque().add_first('AV').first()
        'AV'
        """
        logger.debug(">>> Entering add_first(element=%s)", element)
        logger.debug("<<< Exiting add_first(element=%s)", element)
        return self._insert(self._header, element, self._header._next)

    def add_last(self, element):
        """insertion in the end
        >>> LinkedDeque().add_last('B').last()
        'B'
        """
        logger.debug(">>> Entering add_last(element=%s)", element)
        logger.debug("<<< Exiting add_last(element=%s)", element)
        return self._insert(self._trailer._prev, element, self._trailer)

    # DEqueu Remove Operations (At the front, At the end)

    def remove_first(self):
        """removal from the front
        >>> d = LinkedDeque()
        >>> d.is_empty()
        True
        >>> d.remove_first()
        Traceback (most recent call last):
           ...
        IndexError: remove_first from empty list
        >>> d.add_first('A') # doctest: +ELLIPSIS
        <data_structures.linked_list.deque_doubly.LinkedDeque object at ...
        >>> d.remove_first()
        'A'
        >>> d.is_empty()
        True
        """
        logger.debug(">>> Entering remove_first()")
        if self.is_empty():
            raise IndexError("remove_first from empty list")
        logger.debug("<<< Exiting remove_first()")
        return self._delete(self._header._next)

    def remove_last(self):
        """removal in the end
        >>> d = LinkedDeque()
        >>> d.is_empty()
        True
        >>> d.remove_last()
        Traceback (most recent call last):
           ...
        IndexError: remove_first from empty list
        >>> d.add_first('A') # doctest: +ELLIPSIS
        <data_structures.linked_list.deque_doubly.LinkedDeque object at ...
        >>> d.remove_last()
        'A'
        >>> d.is_empty()
        True
        """
        logger.debug(">>> Entering remove_last()")
        if self.is_empty():
            raise IndexError("remove_first from empty list")
        logger.debug("<<< Exiting remove_last()")
        return self._delete(self._trailer._prev)
