from collections.abc import Callable
import logging
logger = logging.getLogger(__name__)


class Heap:
    """
    A generic Heap class, can be used as min or max by passing the key function
    accordingly.
    """

    def __init__(self, key: Callable | None = None) -> None:
        logger.debug(">>> Entering __init__(key=%s)", key)
        # Stores actual heap items.
        self.arr: list = []
        # Stores indexes of each item for supporting updates and deletion.
        self.pos_map: dict = {}
        # Stores current size of heap.
        self.size = 0
        logger.debug("__init__(self=%s,key=%s): self.size → %s", self, key, self.size)
        # Stores function used to evaluate the score of an item on which basis ordering
        # will be done.
        logger.debug("<<< Exiting __init__(key=%s)", key)
        logger.debug("__init__(key=%s): key → %s", key, key)
        self.key = key or (lambda x: x)

    def _parent(self, i: int) -> int | None:
        """Returns parent index of given index if exists else None"""
        logger.debug(">>> Entering _parent(i=%s)", i)
        logger.debug("<<< Exiting _parent(i=%s)", i)
        return int((i - 1) / 2) if i > 0 else None

    def _left(self, i: int) -> int | None:
        """Returns left-child-index of given index if exists else None"""
        logger.debug(">>> Entering _left(i=%s)", i)
        left = int(2 * i + 1)
        logger.debug("_left(self=%s,i=%s): left → %s", self, i, left)
        logger.debug("_left(i=%s): left → %s", i, left)
        logger.debug("<<< Exiting _left(i=%s)", i)
        return left if 0 < left < self.size else None

    def _right(self, i: int) -> int | None:
        """Returns right-child-index of given index if exists else None"""
        logger.debug(">>> Entering _right(i=%s)", i)
        right = int(2 * i + 2)
        logger.debug("_right(self=%s,i=%s): right → %s", self, i, right)
        logger.debug("_right(i=%s): right → %s", i, right)
        logger.debug("<<< Exiting _right(i=%s)", i)
        return right if 0 < right < self.size else None

    def _swap(self, i: int, j: int) -> None:
        """Performs changes required for swapping two elements in the heap"""
        logger.debug(">>> Entering _swap(i=%s,j=%s)", i, j)
        # First update the indexes of the items in index map.
        self.pos_map[self.arr[i][0]], self.pos_map[self.arr[j][0]] = (
            self.pos_map[self.arr[j][0]],
            self.pos_map[self.arr[i][0]],
        )
        # Then swap the items in the list.
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        logger.debug("<<< Exiting _swap(i=%s,j=%s)", i, j)

    def _cmp(self, i: int, j: int) -> bool:
        """Compares the two items using default comparison"""
        logger.debug(">>> Entering _cmp(i=%s,j=%s)", i, j)
        logger.debug("<<< Exiting _cmp(i=%s,j=%s)", i, j)
        return self.arr[i][1] < self.arr[j][1]

    def _get_valid_parent(self, i: int) -> int:
        """
        Returns index of valid parent as per desired ordering among given index and
        both it's children
        """
        logger.debug(">>> Entering _get_valid_parent(i=%s)", i)
        left = self._left(i)
        logger.debug("_get_valid_parent(self=%s,i=%s): left → %s", self, i, left)
        logger.debug("_get_valid_parent(i=%s): left → %s", i, left)
        right = self._right(i)
        logger.debug("_get_valid_parent(self=%s,i=%s): right → %s", self, i, right)
        logger.debug("_get_valid_parent(i=%s): right → %s", i, right)
        valid_parent = i
        logger.debug("_get_valid_parent(self=%s,i=%s): valid_parent → %s", self, i, valid_parent)

        if left is not None and not self._cmp(left, valid_parent):
            valid_parent = left
        if right is not None and not self._cmp(right, valid_parent):
            valid_parent = right

        logger.debug("<<< Exiting _get_valid_parent(i=%s)", i)
        return valid_parent

    def _heapify_up(self, index: int) -> None:
        """Fixes the heap in upward direction of given index"""
        logger.debug(">>> Entering _heapify_up(index=%s)", index)
        parent = self._parent(index)
        logger.debug("_heapify_up(self=%s,index=%s): parent → %s", self, index, parent)
        logger.debug("_heapify_up(index=%s): parent → %s", index, parent)
        while parent is not None and not self._cmp(index, parent):
            self._swap(index, parent)
            index, parent = parent, self._parent(parent)
            logger.debug("<<< Exiting _heapify_up(index=%s)", index)

    def _heapify_down(self, index: int) -> None:
        """Fixes the heap in downward direction of given index"""
        logger.debug(">>> Entering _heapify_down(index=%s)", index)
        valid_parent = self._get_valid_parent(index)
        logger.debug("_heapify_down(self=%s,index=%s): valid_parent → %s", self, index, valid_parent)
        logger.debug("_heapify_down(index=%s): valid_parent → %s", index, valid_parent)
        while valid_parent != index:
            self._swap(index, valid_parent)
            index, valid_parent = valid_parent, self._get_valid_parent(valid_parent)
            logger.debug("<<< Exiting _heapify_down(index=%s)", index)

    def update_item(self, item: int, item_value: int) -> None:
        """Updates given item value in heap if present"""
        logger.debug(">>> Entering update_item(item=%s,item_value=%s)", item, item_value)
        if item not in self.pos_map:
            logger.debug("<<< Exiting update_item(item=%s,item_value=%s)", item, item_value)
            logger.debug("update_item(self=%s,item=%s,item_value=%s): index → %s", self, item, item_value, index)
            return
        index = self.pos_map[item]
        self.arr[index] = [item, self.key(item_value)]
        # Make sure heap is right in both up and down direction.
        # Ideally only one of them will make any change.
        self._heapify_up(index)
        self._heapify_down(index)

    def delete_item(self, item: int) -> None:
        """Deletes given item from heap if present"""
        logger.debug(">>> Entering delete_item(item=%s)", item)
        if item not in self.pos_map:
            logger.debug("<<< Exiting delete_item(item=%s)", item)
            logger.debug("delete_item(self=%s,item=%s): index → %s", self, item, index)
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
        logger.debug(">>> Entering insert_item(item=%s,item_value=%s)", item, item_value)
        arr_len = len(self.arr)
        logger.debug("insert_item(item=%s,item_value=%s): arr_len → %s", item, item_value, arr_len)
        if arr_len == self.size:
            self.arr.append([item, self.key(item_value)])
        else:
            self.arr[self.size] = [item, self.key(item_value)]
        self.pos_map[item] = self.size
        self.size += 1
        self._heapify_up(self.size - 1)
        logger.debug("<<< Exiting insert_item(item=%s,item_value=%s)", item, item_value)

    def get_top(self) -> tuple | None:
        """Returns top item tuple (Calculated value, item) from heap if present"""
        logger.debug(">>> Entering get_top()")
        logger.debug("<<< Exiting get_top()")
        return self.arr[0] if self.size else None

    def extract_top(self) -> tuple | None:
        """
        Return top item tuple (Calculated value, item) from heap and removes it as well
        if present
        """
        logger.debug(">>> Entering extract_top()")
        top_item_tuple = self.get_top()
        logger.debug("extract_top(self=%s): top_item_tuple → %s", self, top_item_tuple)
        logger.debug("extract_top(): top_item_tuple → %s", top_item_tuple)
        if top_item_tuple:
            self.delete_item(top_item_tuple[0])
        logger.debug("<<< Exiting extract_top()")
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
    logger.debug(">>> Entering test_heap()")

    logger.debug("<<< Exiting test_heap()")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
