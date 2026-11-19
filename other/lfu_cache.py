from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar
import logging
logger = logging.getLogger(__name__)

T = TypeVar("T")
U = TypeVar("U")


class DoubleLinkedListNode[T, U]:
    """
    Double Linked List Node built specifically for LFU Cache

    >>> node = DoubleLinkedListNode(1,1)
    >>> node
    Node: key: 1, val: 1, freq: 0, has next: False, has prev: False
    """

    def __init__(self, key: T | None, val: U | None):
        logger.error(">>> Entering __init__(key=%s,val=%s)", key, val, extra={"event.action": "__init__", "logrite.key": key, "logrite.val": val})
        self.key = key
        logger.debug("__init__(self=%s,key=%s,val=%s): self.key → %s", self, key, val, self.key, extra={"event.action": "__init__", "logrite.key": key, "logrite.val": val})
        logger.error("__init__(key=%s,val=%s): self.key → %s", key, val, self.key, extra={"event.action": "__init__", "logrite.key": key, "logrite.val": val})
        self.val = val
        self.freq: int = 0
        logger.debug("__init__(self=%s,key=%s,val=%s): self.val → %s", self, key, val, self.val, extra={"event.action": "__init__", "logrite.key": key, "logrite.val": val})
        self.next: DoubleLinkedListNode[T, U] | None = None
        self.prev: DoubleLinkedListNode[T, U] | None = None
        logger.warning("<<< Exiting __init__(key=%s,val=%s)", key, val, extra={"event.action": "__init__", "logrite.key": key, "logrite.val": val})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return (
            f"Node: key: {self.key}, val: {self.val}, freq: {self.freq}, "
            f"has next: {self.next is not None}, has prev: {self.prev is not None}"
        )


class DoubleLinkedList[T, U]:
    """
    Double Linked List built specifically for LFU Cache

    >>> dll: DoubleLinkedList = DoubleLinkedList()
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True

    >>> first_node = DoubleLinkedListNode(1,10)
    >>> first_node
    Node: key: 1, val: 10, freq: 0, has next: False, has prev: False


    >>> dll.add(first_node)
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: 1, val: 10, freq: 1, has next: True, has prev: True,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True

    >>> # node is mutated
    >>> first_node
    Node: key: 1, val: 10, freq: 1, has next: True, has prev: True

    >>> second_node = DoubleLinkedListNode(2,20)
    >>> second_node
    Node: key: 2, val: 20, freq: 0, has next: False, has prev: False

    >>> dll.add(second_node)
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: 1, val: 10, freq: 1, has next: True, has prev: True,
        Node: key: 2, val: 20, freq: 1, has next: True, has prev: True,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True

    >>> removed_node = dll.remove(first_node)
    >>> assert removed_node == first_node
    >>> dll
    DoubleLinkedList,
        Node: key: None, val: None, freq: 0, has next: True, has prev: False,
        Node: key: 2, val: 20, freq: 1, has next: True, has prev: True,
        Node: key: None, val: None, freq: 0, has next: False, has prev: True


    >>> # Attempt to remove node not on list
    >>> removed_node = dll.remove(first_node)
    >>> removed_node is None
    True

    >>> # Attempt to remove head or rear
    >>> dll.head
    Node: key: None, val: None, freq: 0, has next: True, has prev: False
    >>> dll.remove(dll.head) is None
    True

    >>> # Attempt to remove head or rear
    >>> dll.rear
    Node: key: None, val: None, freq: 0, has next: False, has prev: True
    >>> dll.remove(dll.rear) is None
    True


    """

    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.head: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.rear: DoubleLinkedListNode[T, U] = DoubleLinkedListNode(None, None)
        self.head.next, self.rear.prev = self.rear, self.head
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def __repr__(self) -> str:
        rep = ["DoubleLinkedList"]
        logger.error("__repr__(): rep → %s", rep, extra={"event.action": "__repr__"})
        node = self.head
        while node.next is not None:
            rep.append(str(node))
            node = node.next
        rep.append(str(self.rear))
        return ",\n    ".join(rep)

    def add(self, node: DoubleLinkedListNode[T, U]) -> None:
        """
        Adds the given node at the tail of the list and shifting it to proper position
        """
        logger.error(">>> Entering add(node=%s)", node, extra={"event.action": "add", "logrite.node": node})

        previous = self.rear.prev

        # All nodes other than self.head are guaranteed to have non-None previous
        assert previous is not None

        previous.next = node
        logger.debug("add(self=%s,node=%s): previous.next → %s", self, node, previous.next, extra={"event.action": "add", "logrite.node": node})
        node.prev = previous
        logger.debug("add(self=%s,node=%s): node.prev → %s", self, node, node.prev, extra={"event.action": "add", "logrite.node": node})
        self.rear.prev = node
        node.next = self.rear
        logger.debug("add(self=%s,node=%s): node.next → %s", self, node, node.next, extra={"event.action": "add", "logrite.node": node})
        node.freq += 1
        self._position_node(node)
        logger.warning("<<< Exiting add(node=%s)", node, extra={"event.action": "add", "logrite.node": node})

    def _position_node(self, node: DoubleLinkedListNode[T, U]) -> None:
        """
        Moves node forward to maintain invariant of sort by freq value
        """
        logger.error(">>> Entering _position_node(node=%s)", node, extra={"event.action": "_position_node", "logrite.node": node})

        while node.prev is not None and node.prev.freq > node.freq:
            # swap node with previous node
            previous_node = node.prev

            logger.warning("<<< Exiting _position_node(node=%s)", node, extra={"event.action": "_position_node", "logrite.node": node})
            node.prev = previous_node.prev
            logger.debug("_position_node(self=%s,node=%s): node.prev → %s", self, node, node.prev, extra={"event.action": "_position_node", "logrite.node": node})
            previous_node.next = node.prev
            logger.debug("_position_node(self=%s,node=%s): previous_node.next → %s", self, node, previous_node.next, extra={"event.action": "_position_node", "logrite.node": node})
            node.next = previous_node
            logger.debug("_position_node(self=%s,node=%s): node.next → %s", self, node, node.next, extra={"event.action": "_position_node", "logrite.node": node})
            previous_node.prev = node
            logger.debug("_position_node(self=%s,node=%s): previous_node.prev → %s", self, node, previous_node.prev, extra={"event.action": "_position_node", "logrite.node": node})

    def remove(
        self, node: DoubleLinkedListNode[T, U]
    ) -> DoubleLinkedListNode[T, U] | None:
        """
        Removes and returns the given node from the list

        Returns None if node.prev or node.next is None
        """

        if node.prev is None or node.next is None:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        logger.warning("<<< Exiting remove(node=%s)", node, extra={"event.action": "remove", "logrite.node": node})
        return node


class LFUCache[T, U]:
    """
    LFU Cache to store a given capacity of data. Can be used as a stand-alone object
    or as a function decorator.

    >>> cache = LFUCache(2)
    >>> cache.put(1, 1)
    >>> cache.put(2, 2)
    >>> cache.get(1)
    1
    >>> cache.put(3, 3)
    >>> cache.get(2) is None
    True
    >>> cache.put(4, 4)
    >>> cache.get(1) is None
    True
    >>> cache.get(3)
    3
    >>> cache.get(4)
    4
    >>> cache
    CacheInfo(hits=3, misses=2, capacity=2, current_size=2)
    >>> @LFUCache.decorator(100)
    ... def fib(num):
    ...     if num in (1, 2):
    ...         return 1
    ...     return fib(num - 1) + fib(num - 2)

    >>> for i in range(1, 101):
    ...     res = fib(i)

    >>> fib.cache_info()
    CacheInfo(hits=196, misses=100, capacity=100, current_size=100)
    """

    def __init__(self, capacity: int):
        logger.error(">>> Entering __init__(capacity=%s)", capacity, extra={"event.action": "__init__", "logrite.capacity": capacity})
        self.list: DoubleLinkedList[T, U] = DoubleLinkedList()
        self.capacity = capacity
        logger.debug("__init__(self=%s,capacity=%s): self.capacity → %s", self, capacity, self.capacity, extra={"event.action": "__init__", "logrite.capacity": capacity})
        self.num_keys = 0
        logger.debug("__init__(self=%s,capacity=%s): self.num_keys → %s", self, capacity, self.num_keys, extra={"event.action": "__init__", "logrite.capacity": capacity})
        self.hits = 0
        logger.debug("__init__(self=%s,capacity=%s): self.hits → %s", self, capacity, self.hits, extra={"event.action": "__init__", "logrite.capacity": capacity})
        self.miss = 0
        logger.debug("__init__(self=%s,capacity=%s): self.miss → %s", self, capacity, self.miss, extra={"event.action": "__init__", "logrite.capacity": capacity})
        self.cache: dict[T, DoubleLinkedListNode[T, U]] = {}
        logger.warning("<<< Exiting __init__(capacity=%s)", capacity, extra={"event.action": "__init__", "logrite.capacity": capacity})

    def __repr__(self) -> str:
        """
        Return the details for the cache instance
        [hits, misses, capacity, current_size]
        """

        return (
            f"CacheInfo(hits={self.hits}, misses={self.miss}, "
            f"capacity={self.capacity}, current_size={self.num_keys})"
        )

    def __contains__(self, key: T) -> bool:
        """
        >>> cache = LFUCache(1)

        >>> 1 in cache
        False

        >>> cache.put(1, 1)
        >>> 1 in cache
        True
        """
        logger.error(">>> Entering __contains__(key=%s)", key, extra={"event.action": "__contains__", "logrite.key": key})

        logger.warning("<<< Exiting __contains__(key=%s)", key, extra={"event.action": "__contains__", "logrite.key": key})
        return key in self.cache

    def get(self, key: T) -> U | None:
        """
        Returns the value for the input key and updates the Double Linked List. Returns
        Returns None if key is not present in cache
        """
        logger.error(">>> Entering get(key=%s)", key, extra={"event.action": "get", "logrite.key": key})

        if key in self.cache:
            self.hits += 1
            value_node: DoubleLinkedListNode[T, U] = self.cache[key]
            node = self.list.remove(self.cache[key])
            logger.error("get(key=%s): node → %s", key, node, extra={"event.action": "get", "logrite.key": key})
            assert node == value_node

            # node is guaranteed not None because it is in self.cache
            assert node is not None
            self.list.add(node)
            return node.val
        self.miss += 1
        logger.warning("<<< Exiting get(key=%s)", key, extra={"event.action": "get", "logrite.key": key})
        return None

    def put(self, key: T, value: U) -> None:
        """
        Sets the value for the input key and updates the Double Linked List
        """
        logger.error(">>> Entering put(key=%s,value=%s)", key, value, extra={"event.action": "put", "logrite.key": key, "logrite.value": value})

        if key not in self.cache:
            if self.num_keys >= self.capacity:
                # delete first node when over capacity
                first_node = self.list.head.next

                # guaranteed to have a non-None first node when num_keys > 0
                # explain to type checker via assertions
                assert first_node is not None
                assert first_node.key is not None
                assert self.list.remove(first_node) is not None
                # first_node guaranteed to be in list

                del self.cache[first_node.key]
                self.num_keys -= 1
            self.cache[key] = DoubleLinkedListNode(key, value)
            self.list.add(self.cache[key])
            self.num_keys += 1

        else:
            node = self.list.remove(self.cache[key])
            logger.error("put(key=%s,value=%s): node → %s", key, value, node, extra={"event.action": "put", "logrite.key": key, "logrite.value": value})
            assert node is not None  # node guaranteed to be in list
            node.val = value
            logger.debug("put(self=%s,key=%s,value=%s): node.val → %s", self, key, value, node.val, extra={"event.action": "put", "logrite.key": key, "logrite.value": value})
            self.list.add(node)
            logger.warning("<<< Exiting put(key=%s,value=%s)", key, value, extra={"event.action": "put", "logrite.key": key, "logrite.value": value})

    @classmethod
    def decorator(
        cls: type[LFUCache[T, U]], size: int = 128
    ) -> Callable[[Callable[[T], U]], Callable[..., U]]:
        logger.error(">>> Entering decorator(size=%s)", size, extra={"event.action": "decorator", "logrite.size": size})
        """
        Decorator version of LFU Cache

        Decorated function must be function of T -> U
        """
        logger.warning("<<< Exiting decorator(size=%s)", size, extra={"event.action": "decorator", "logrite.size": size})

        def cache_decorator_inner(func: Callable[[T], U]) -> Callable[..., U]:
            logger.error(">>> Entering cache_decorator_inner(func=%s)", func, extra={"event.action": "cache_decorator_inner", "logrite.func": func})
            # variable to map the decorator functions to their respective instance
            decorator_function_to_instance_map: dict[
                Callable[[T], U], LFUCache[T, U]
            ] = {}
            logger.warning("<<< Exiting cache_decorator_inner(func=%s)", func, extra={"event.action": "cache_decorator_inner", "logrite.func": func})

            def cache_decorator_wrapper(*args: T) -> U:
                logger.error(">>> Entering cache_decorator_wrapper()", extra={"event.action": "cache_decorator_wrapper"})
                if func not in decorator_function_to_instance_map:
                    decorator_function_to_instance_map[func] = LFUCache(size)

                result = decorator_function_to_instance_map[func].get(args[0])
                logger.error("cache_decorator_wrapper(): result → %s", result, extra={"event.action": "cache_decorator_wrapper"})
                if result is None:
                    result = func(*args)
                    decorator_function_to_instance_map[func].put(args[0], result)
                logger.warning("<<< Exiting cache_decorator_wrapper()", extra={"event.action": "cache_decorator_wrapper"})
                return result

            def cache_info() -> LFUCache[T, U]:
                logger.error(">>> Entering cache_info()", extra={"event.action": "cache_info"})
                logger.warning("<<< Exiting cache_info()", extra={"event.action": "cache_info"})
                return decorator_function_to_instance_map[func]

            setattr(cache_decorator_wrapper, "cache_info", cache_info)  # noqa: B010

            return cache_decorator_wrapper

        return cache_decorator_inner


if __name__ == "__main__":
    import doctest

    doctest.testmod()
