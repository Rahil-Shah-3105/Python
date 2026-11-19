from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable
from typing import Protocol, TypeVar
import logging
logger = logging.getLogger(__name__)


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        logger.error(">>> Entering __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        pass
        logger.warning("<<< Exiting __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})

    @abstractmethod
    def __gt__(self: T, other: T) -> bool:
        logger.error(">>> Entering __gt__(other=%s)", other, extra={"event.action": "__gt__", "logrite.other": other})
        pass
        logger.warning("<<< Exiting __gt__(other=%s)", other, extra={"event.action": "__gt__", "logrite.other": other})

    @abstractmethod
    def __eq__(self: T, other: object) -> bool:
        logger.error(">>> Entering __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        pass
        logger.warning("<<< Exiting __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})


T = TypeVar("T", bound=Comparable)


class Heap[T: Comparable]:
    """A Max Heap Implementation

    >>> unsorted = [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5]
    >>> h = Heap()
    >>> h.build_max_heap(unsorted)
    >>> h
    [209, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]
    >>>
    >>> h.extract_max()
    209
    >>> h
    [201, 107, 25, 103, 11, 15, 1, 9, 7, 5]
    >>>
    >>> h.insert(100)
    >>> h
    [201, 107, 25, 103, 100, 15, 1, 9, 7, 5, 11]
    >>>
    >>> h.heap_sort()
    >>> h
    [1, 5, 7, 9, 11, 15, 25, 100, 103, 107, 201]
    """

    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.h: list[T] = []
        self.heap_size: int = 0
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return str(self.h)

    def parent_index(self, child_idx: int) -> int | None:
        """
        returns the parent index based on the given child index

        >>> h = Heap()
        >>> h.build_max_heap([103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5])
        >>> h
        [209, 201, 25, 103, 107, 15, 1, 9, 7, 11, 5]

        >>> h.parent_index(-1)  # returns none if index is <=0

        >>> h.parent_index(0)   # returns none if index is <=0

        >>> h.parent_index(1)
        0
        >>> h.parent_index(2)
        0
        >>> h.parent_index(3)
        1
        >>> h.parent_index(4)
        1
        >>> h.parent_index(5)
        2
        >>> h.parent_index(10.5)
        4.0
        >>> h.parent_index(209.0)
        104.0
        >>> h.parent_index("Test")
        Traceback (most recent call last):
        ...
        TypeError: '>' not supported between instances of 'str' and 'int'
        """
        logger.error(">>> Entering parent_index(child_idx=%s)", child_idx, extra={"event.action": "parent_index", "logrite.child_idx": child_idx})
        if child_idx > 0:
            return (child_idx - 1) // 2
        logger.warning("<<< Exiting parent_index(child_idx=%s)", child_idx, extra={"event.action": "parent_index", "logrite.child_idx": child_idx})
        return None

    def left_child_idx(self, parent_idx: int) -> int | None:
        """
        return the left child index if the left child exists.
        if not, return None.
        """
        logger.error(">>> Entering left_child_idx(parent_idx=%s)", parent_idx, extra={"event.action": "left_child_idx", "logrite.parent_idx": parent_idx})
        left_child_index = 2 * parent_idx + 1
        if left_child_index < self.heap_size:
            return left_child_index
        logger.warning("<<< Exiting left_child_idx(parent_idx=%s)", parent_idx, extra={"event.action": "left_child_idx", "logrite.parent_idx": parent_idx})
        return None

    def right_child_idx(self, parent_idx: int) -> int | None:
        """
        return the right child index if the right child exists.
        if not, return None.
        """
        logger.error(">>> Entering right_child_idx(parent_idx=%s)", parent_idx, extra={"event.action": "right_child_idx", "logrite.parent_idx": parent_idx})
        right_child_index = 2 * parent_idx + 2
        if right_child_index < self.heap_size:
            return right_child_index
        logger.warning("<<< Exiting right_child_idx(parent_idx=%s)", parent_idx, extra={"event.action": "right_child_idx", "logrite.parent_idx": parent_idx})
        return None

    def max_heapify(self, index: int) -> None:
        """
        correct a single violation of the heap property in a subtree's root.

        It is the function that is responsible for restoring the property
        of Max heap i.e the maximum element is always at top.
        """
        logger.error(">>> Entering max_heapify(index=%s)", index, extra={"event.action": "max_heapify", "logrite.index": index})
        if index < self.heap_size:
            violation: int = index
            left_child = self.left_child_idx(index)
            logger.error("max_heapify(index=%s): left_child → %s", index, left_child, extra={"event.action": "max_heapify", "logrite.index": index})
            right_child = self.right_child_idx(index)
            logger.error("max_heapify(index=%s): right_child → %s", index, right_child, extra={"event.action": "max_heapify", "logrite.index": index})
            # check which child is larger than its parent
            if left_child is not None and self.h[left_child] > self.h[violation]:
                violation = left_child
            if right_child is not None and self.h[right_child] > self.h[violation]:
                violation = right_child
            # if violation indeed exists
            if violation != index:
                # swap to fix the violation
                self.h[violation], self.h[index] = self.h[index], self.h[violation]
                # fix the subsequent violation recursively if any
                self.max_heapify(violation)
                logger.warning("<<< Exiting max_heapify(index=%s)", index, extra={"event.action": "max_heapify", "logrite.index": index})

    def build_max_heap(self, collection: Iterable[T]) -> None:
        """
        build max heap from an unsorted array

        >>> h = Heap()
        >>> h.build_max_heap([20,40,50,20,10])
        >>> h
        [50, 40, 20, 20, 10]

        >>> h = Heap()
        >>> h.build_max_heap([1,2,3,4,5,6,7,8,9,0])
        >>> h
        [9, 8, 7, 4, 5, 6, 3, 2, 1, 0]

        >>> h = Heap()
        >>> h.build_max_heap([514,5,61,57,8,99,105])
        >>> h
        [514, 57, 105, 5, 8, 99, 61]

        >>> h = Heap()
        >>> h.build_max_heap([514,5,61.6,57,8,9.9,105])
        >>> h
        [514, 57, 105, 5, 8, 9.9, 61.6]
        """
        logger.error(">>> Entering build_max_heap(collection=%s)", collection, extra={"event.action": "build_max_heap", "logrite.collection": collection})
        logger.error("build_max_heap(collection=%s): h → %s", collection, h, extra={"event.action": "build_max_heap", "logrite.collection": collection})
        self.h = list(collection)
        self.heap_size = len(self.h)
        logger.error("build_max_heap(collection=%s): self.heap_size → %s", collection, self.heap_size, extra={"event.action": "build_max_heap", "logrite.collection": collection})
        if self.heap_size > 1:
            # max_heapify from right to left but exclude leaves (last level)
            for i in range(self.heap_size // 2 - 1, -1, -1):
                self.max_heapify(i)

    def extract_max(self) -> T:
        """
        get and remove max from heap

        >>> h = Heap()
        >>> h.build_max_heap([20,40,50,20,10])
        >>> h.extract_max()
        50

        >>> h = Heap()
        >>> h.build_max_heap([514,5,61,57,8,99,105])
        >>> h.extract_max()
        514

        >>> h = Heap()
        >>> h.build_max_heap([1,2,3,4,5,6,7,8,9,0])
        >>> h.extract_max()
        9
        """
        if self.heap_size >= 2:
            me = self.h[0]
            self.h[0] = self.h.pop(-1)
            self.heap_size -= 1
            self.max_heapify(0)
            return me
        elif self.heap_size == 1:
            self.heap_size -= 1
            return self.h.pop(-1)
        else:
            raise Exception("Empty heap")

    def insert(self, value: T) -> None:
        """
        insert a new value into the max heap

        >>> h = Heap()
        >>> h.insert(10)
        >>> h
        [10]

        >>> h = Heap()
        >>> h.insert(10)
        >>> h.insert(10)
        >>> h
        [10, 10]

        >>> h = Heap()
        >>> h.insert(10)
        >>> h.insert(10.1)
        >>> h
        [10.1, 10]

        >>> h = Heap()
        >>> h.insert(0.1)
        >>> h.insert(0)
        >>> h.insert(9)
        >>> h.insert(5)
        >>> h
        [9, 5, 0.1, 0]
        """
        self.h.append(value)
        idx = (self.heap_size - 1) // 2
        self.heap_size += 1
        while idx >= 0:
            self.max_heapify(idx)
            idx = (idx - 1) // 2

    def heap_sort(self) -> None:
        size = self.heap_size
        for j in range(size - 1, 0, -1):
            self.h[0], self.h[j] = self.h[j], self.h[0]
            self.heap_size -= 1
            self.max_heapify(0)
        self.heap_size = size


if __name__ == "__main__":
    import doctest

    # run doc test
    doctest.testmod()

    # demo
    for unsorted in [
        [0],
        [2],
        [3, 5],
        [5, 3],
        [5, 5],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 3, 5],
        [0, 2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [-45, -2, -5],
    ]:
        print(f"unsorted array: {unsorted}")

        heap: Heap[int] = Heap()
        heap.build_max_heap(unsorted)
        print(f"after build heap: {heap}")

        print(f"max value: {heap.extract_max()}")
        print(f"after max value removed: {heap}")

        heap.insert(100)
        print(f"after new value 100 inserted: {heap}")

        heap.heap_sort()
        print(f"heap-sorted array: {heap}\n")
