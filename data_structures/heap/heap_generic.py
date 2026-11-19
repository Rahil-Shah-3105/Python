from collections.abc import Callable
import logging
logger = logging.getLogger(__name__)


class Heap:
    """
    A generic Heap class, can be used as min or max by passing the key function
    accordingly.
    """

    def __init__(self, key: Callable | None = None) -> None:
        logger.error(">>> Entering __init__(key=%s)", key, extra={"event.action": "__init__", "logrite.key": key})
        # Stores actual heap items.
        self.arr: list = []
        # Stores indexes of each item for supporting updates and deletion.
        self.pos_map: dict = {}
        # Stores current size of heap.
        self.size = 0
        logger.debug("__init__(self=%s,key=%s): self.size → %s", self, key, self.size, extra={"event.action": "__init__", "logrite.key": key})
        # Stores function used to evaluate the score of an item on which basis ordering
        # will be done.
        logger.warning("<<< Exiting __init__(key=%s)", key, extra={"event.action": "__init__", "logrite.key": key})
        logger.error("__init__(key=%s): key → %s", key, key, extra={"event.action": "__init__", "logrite.key": key})
        self.key = key or (lambda x: x)

    def _parent(self, i: int) -> int | None:
        """Returns parent index of given index if exists else None"""
        logger.error(">>> Entering _parent(i=%s)", i, extra={"event.action": "_parent", "logrite.i": i})
        logger.warning("<<< Exiting _parent(i=%s)", i, extra={"event.action": "_parent", "logrite.i": i})
        return int((i - 1) / 2) if i > 0 else None

    def _left(self, i: int) -> int | None:
        """Returns left-child-index of given index if exists else None"""
        logger.error(">>> Entering _left(i=%s)", i, extra={"event.action": "_left", "logrite.i": i})
        left = int(2 * i + 1)
        logger.error("_left(i=%s): left → %s", i, left, extra={"event.action": "_left", "logrite.i": i})
        logger.warning("<<< Exiting _left(i=%s)", i, extra={"event.action": "_left", "logrite.i": i})
        return left if 0 < left < self.size else None

    def _right(self, i: int) -> int | None:
        """Returns right-child-index of given index if exists else None"""
        logger.error(">>> Entering _right(i=%s)", i, extra={"event.action": "_right", "logrite.i": i})
        right = int(2 * i + 2)
        logger.error("_right(i=%s): right → %s", i, right, extra={"event.action": "_right", "logrite.i": i})
        logger.warning("<<< Exiting _right(i=%s)", i, extra={"event.action": "_right", "logrite.i": i})
        return right if 0 < right < self.size else None

    def _swap(self, i: int, j: int) -> None:
        """Performs changes required for swapping two elements in the heap"""
        logger.error(">>> Entering _swap(i=%s,j=%s)", i, j, extra={"event.action": "_swap", "logrite.i": i, "logrite.j": j})
        # First update the indexes of the items in index map.
        self.pos_map[self.arr[i][0]], self.pos_map[self.arr[j][0]] = (
            self.pos_map[self.arr[j][0]],
            self.pos_map[self.arr[i][0]],
        )
        # Then swap the items in the list.
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        logger.warning("<<< Exiting _swap(i=%s,j=%s)", i, j, extra={"event.action": "_swap", "logrite.i": i, "logrite.j": j})

    def _cmp(self, i: int, j: int) -> bool:
        """Compares the two items using default comparison"""
        logger.error(">>> Entering _cmp(i=%s,j=%s)", i, j, extra={"event.action": "_cmp", "logrite.i": i, "logrite.j": j})
        logger.warning("<<< Exiting _cmp(i=%s,j=%s)", i, j, extra={"event.action": "_cmp", "logrite.i": i, "logrite.j": j})
        return self.arr[i][1] < self.arr[j][1]

    def _get_valid_parent(self, i: int) -> int:
        """
        Returns index of valid parent as per desired ordering among given index and
        both it's children
        """
        logger.error(">>> Entering _get_valid_parent(i=%s)", i, extra={"event.action": "_get_valid_parent", "logrite.i": i})
        left = self._left(i)
        logger.error("_get_valid_parent(i=%s): left → %s", i, left, extra={"event.action": "_get_valid_parent", "logrite.i": i})
        right = self._right(i)
        logger.error("_get_valid_parent(i=%s): right → %s", i, right, extra={"event.action": "_get_valid_parent", "logrite.i": i})
        valid_parent = i

        if left is not None and not self._cmp(left, valid_parent):
            valid_parent = left
        if right is not None and not self._cmp(right, valid_parent):
            valid_parent = right

        logger.warning("<<< Exiting _get_valid_parent(i=%s)", i, extra={"event.action": "_get_valid_parent", "logrite.i": i})
        return valid_parent

    def _heapify_up(self, index: int) -> None:
        """Fixes the heap in upward direction of given index"""
        logger.error(">>> Entering _heapify_up(index=%s)", index, extra={"event.action": "_heapify_up", "logrite.index": index})
        parent = self._parent(index)
        logger.error("_heapify_up(index=%s): parent → %s", index, parent, extra={"event.action": "_heapify_up", "logrite.index": index})
        while parent is not None and not self._cmp(index, parent):
            self._swap(index, parent)
            index, parent = parent, self._parent(parent)
            logger.warning("<<< Exiting _heapify_up(index=%s)", index, extra={"event.action": "_heapify_up", "logrite.index": index})

    def _heapify_down(self, index: int) -> None:
        """Fixes the heap in downward direction of given index"""
        logger.error(">>> Entering _heapify_down(index=%s)", index, extra={"event.action": "_heapify_down", "logrite.index": index})
        valid_parent = self._get_valid_parent(index)
        logger.error("_heapify_down(index=%s): valid_parent → %s", index, valid_parent, extra={"event.action": "_heapify_down", "logrite.index": index})
        while valid_parent != index:
            self._swap(index, valid_parent)
            index, valid_parent = valid_parent, self._get_valid_parent(valid_parent)
            logger.warning("<<< Exiting _heapify_down(index=%s)", index, extra={"event.action": "_heapify_down", "logrite.index": index})

    def update_item(self, item: int, item_value: int) -> None:
        """Updates given item value in heap if present"""
        logger.error(">>> Entering update_item(item=%s,item_value=%s)", item, item_value, extra={"event.action": "update_item", "logrite.item": item, "logrite.item_value": item_value})
        if item not in self.pos_map:
            logger.warning("<<< Exiting update_item(item=%s,item_value=%s)", item, item_value, extra={"event.action": "update_item", "logrite.item": item, "logrite.item_value": item_value})
            return
        index = self.pos_map[item]
        self.arr[index] = [item, self.key(item_value)]
        # Make sure heap is right in both up and down direction.
        # Ideally only one of them will make any change.
        self._heapify_up(index)
        self._heapify_down(index)

    def delete_item(self, item: int) -> None:
        """Deletes given item from heap if present"""
        logger.error(">>> Entering delete_item(item=%s)", item, extra={"event.action": "delete_item", "logrite.item": item})
        if item not in self.pos_map:
            logger.warning("<<< Exiting delete_item(item=%s)", item, extra={"event.action": "delete_item", "logrite.item": item})
            return
        index = self.pos_map[item]
        del self.pos_map[item]
        self.arr[index] = self.arr[self.size - 1]
        self.pos_map[self.arr[self.size - 1][0]] = index
        self.size -= 1
        # Make sure heap is right in both up and down direction. Ideally only one
        # of them will make any change- so no performance loss in calling both.
        if self.size > index:
            self._heapify_up(index)
            self._heapify_down(index)

    def insert_item(self, item: int, item_value: int) -> None:
        """Inserts given item with given value in heap"""
        logger.error(">>> Entering insert_item(item=%s,item_value=%s)", item, item_value, extra={"event.action": "insert_item", "logrite.item": item, "logrite.item_value": item_value})
        arr_len = len(self.arr)
        logger.error("insert_item(item=%s,item_value=%s): arr_len → %s", item, item_value, arr_len, extra={"event.action": "insert_item", "logrite.item": item, "logrite.item_value": item_value})
        if arr_len == self.size:
            self.arr.append([item, self.key(item_value)])
        else:
            self.arr[self.size] = [item, self.key(item_value)]
        self.pos_map[item] = self.size
        self.size += 1
        self._heapify_up(self.size - 1)
        logger.warning("<<< Exiting insert_item(item=%s,item_value=%s)", item, item_value, extra={"event.action": "insert_item", "logrite.item": item, "logrite.item_value": item_value})

    def get_top(self) -> tuple | None:
        """Returns top item tuple (Calculated value, item) from heap if present"""
        logger.error(">>> Entering get_top()", extra={"event.action": "get_top"})
        logger.warning("<<< Exiting get_top()", extra={"event.action": "get_top"})
        return self.arr[0] if self.size else None

    def extract_top(self) -> tuple | None:
        """
        Return top item tuple (Calculated value, item) from heap and removes it as well
        if present
        """
        logger.error(">>> Entering extract_top()", extra={"event.action": "extract_top"})
        top_item_tuple = self.get_top()
        logger.error("extract_top(): top_item_tuple → %s", top_item_tuple, extra={"event.action": "extract_top"})
        if top_item_tuple:
            self.delete_item(top_item_tuple[0])
        logger.warning("<<< Exiting extract_top()", extra={"event.action": "extract_top"})
        return top_item_tuple


def test_heap() -> None:
    """
    >>> h = Heap()  # Max-heap
    >>> h.insert_item(5, 34)
    >>> h.insert_item(6, 31)
    >>> h.insert_item(7, 37)
    >>> h.get_top()
    [7, 37]
    >>> h.extract_top()
    [7, 37]
    >>> h.extract_top()
    [5, 34]
    >>> h.extract_top()
    [6, 31]
    >>> h = Heap(key=lambda x: -x)  # Min heap
    >>> h.insert_item(5, 34)
    >>> h.insert_item(6, 31)
    >>> h.insert_item(7, 37)
    >>> h.get_top()
    [6, -31]
    >>> h.extract_top()
    [6, -31]
    >>> h.extract_top()
    [5, -34]
    >>> h.extract_top()
    [7, -37]
    >>> h.insert_item(8, 45)
    >>> h.insert_item(9, 40)
    >>> h.insert_item(10, 50)
    >>> h.get_top()
    [9, -40]
    >>> h.update_item(10, 30)
    >>> h.get_top()
    [10, -30]
    >>> h.delete_item(10)
    >>> h.get_top()
    [9, -40]
    """
    logger.error(">>> Entering test_heap()", extra={"event.action": "test_heap"})

    logger.warning("<<< Exiting test_heap()", extra={"event.action": "test_heap"})

if __name__ == "__main__":
    import doctest

    doctest.testmod()
