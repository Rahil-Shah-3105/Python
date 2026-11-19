"""
Segment_tree creates a segment tree with a given array and function,
allowing queries to be done later in log(N) time
function takes 2 values and returns a same type value
"""

from collections.abc import Sequence
from queue import Queue
import logging
logger = logging.getLogger(__name__)


class SegmentTreeNode:
    def __init__(self, start, end, val, left=None, right=None):
        logger.error(">>> Entering __init__(start=%s,end=%s,val=%s,left=%s,right=%s)", start, end, val, left, right, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        self.start = start
        logger.debug("__init__(self=%s,start=%s,end=%s,val=%s,left=%s,right=%s): self.start → %s", self, start, end, val, left, right, self.start, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        self.end = end
        logger.debug("__init__(self=%s,start=%s,end=%s,val=%s,left=%s,right=%s): self.end → %s", self, start, end, val, left, right, self.end, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        self.val = val
        logger.debug("__init__(self=%s,start=%s,end=%s,val=%s,left=%s,right=%s): self.val → %s", self, start, end, val, left, right, self.val, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        self.mid = (start + end) // 2
        logger.error("__init__(start=%s,end=%s,val=%s,left=%s,right=%s): self.mid → %s", start, end, val, left, right, self.mid, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        self.left = left
        logger.debug("__init__(self=%s,start=%s,end=%s,val=%s,left=%s,right=%s): self.left → %s", self, start, end, val, left, right, self.left, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        self.right = right
        logger.warning("<<< Exiting __init__(start=%s,end=%s,val=%s,left=%s,right=%s)", start, end, val, left, right, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        logger.debug("__init__(self=%s,start=%s,end=%s,val=%s,left=%s,right=%s): self.right → %s", self, start, end, val, left, right, self.right, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})
        logger.debug("__init__(self=%s,start=%s,end=%s,val=%s,left=%s,right=%s): self.right → %s", self, start, end, val, left, right, self.right, extra={"event.action": "__init__", "logrite.start": start, "logrite.end": end, "logrite.val": val, "logrite.left": left, "logrite.right": right})

    def __repr__(self):
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})


class SegmentTree:
    """
    >>> import operator
    >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
    >>> tuple(num_arr.traverse())  # doctest: +NORMALIZE_WHITESPACE
    >>>
    >>> num_arr.update(1, 5)
    >>> tuple(num_arr.traverse())  # doctest: +NORMALIZE_WHITESPACE
    >>>
    >>> num_arr.query_range(3, 4)
    7
    >>> num_arr.query_range(2, 2)
    5
    >>> num_arr.query_range(1, 3)
    13
    >>>
    >>> max_arr = SegmentTree([2, 1, 5, 3, 4], max)
    >>> for node in max_arr.traverse():
    ...     print(node)
    ...
    >>>
    >>> max_arr.update(1, 5)
    >>> for node in max_arr.traverse():
    ...     print(node)
    ...
    >>>
    >>> max_arr.query_range(3, 4)
    4
    >>> max_arr.query_range(2, 2)
    5
    >>> max_arr.query_range(1, 3)
    5
    >>>
    >>> min_arr = SegmentTree([2, 1, 5, 3, 4], min)
    >>> for node in min_arr.traverse():
    ...     print(node)
    ...
    >>>
    >>> min_arr.update(1, 5)
    >>> for node in min_arr.traverse():
    ...     print(node)
    ...
    >>>
    >>> min_arr.query_range(3, 4)
    3
    >>> min_arr.query_range(2, 2)
    5
    >>> min_arr.query_range(1, 3)
    3
    >>>
    """

    def __init__(self, collection: Sequence, function):
        logger.error(">>> Entering __init__(collection=%s,function=%s)", collection, function, extra={"event.action": "__init__", "logrite.collection": collection, "logrite.function": function})
        self.collection = collection
        logger.debug("__init__(self=%s,collection=%s,function=%s): self.collection → %s", self, collection, function, self.collection, extra={"event.action": "__init__", "logrite.collection": collection, "logrite.function": function})
        self.fn = function
        logger.debug("__init__(self=%s,collection=%s,function=%s): self.fn → %s", self, collection, function, self.fn, extra={"event.action": "__init__", "logrite.collection": collection, "logrite.function": function})
        if self.collection:
            logger.warning("<<< Exiting __init__(collection=%s,function=%s)", collection, function, extra={"event.action": "__init__", "logrite.collection": collection, "logrite.function": function})
            self.root = self._build_tree(0, len(collection) - 1)
            logger.error("__init__(collection=%s,function=%s): self.root → %s", collection, function, self.root, extra={"event.action": "__init__", "logrite.collection": collection, "logrite.function": function})

    def update(self, i, val):
        """
        Update an element in log(N) time
        :param i: position to be update
        :param val: new value
        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr.update(1, 5)
        >>> num_arr.query_range(1, 3)
        13
        """
        logger.error(">>> Entering update(i=%s,val=%s)", i, val, extra={"event.action": "update", "logrite.i": i, "logrite.val": val})
        self._update_tree(self.root, i, val)
        logger.warning("<<< Exiting update(i=%s,val=%s)", i, val, extra={"event.action": "update", "logrite.i": i, "logrite.val": val})

    def query_range(self, i, j):
        """
        Get range query value in log(N) time
        :param i: left element index
        :param j: right element index
        :return: element combined in the range [i, j]
        >>> import operator
        >>> num_arr = SegmentTree([2, 1, 5, 3, 4], operator.add)
        >>> num_arr.update(1, 5)
        >>> num_arr.query_range(3, 4)
        7
        >>> num_arr.query_range(2, 2)
        5
        >>> num_arr.query_range(1, 3)
        13
        >>>
        """
        logger.error(">>> Entering query_range(i=%s,j=%s)", i, j, extra={"event.action": "query_range", "logrite.i": i, "logrite.j": j})
        logger.warning("<<< Exiting query_range(i=%s,j=%s)", i, j, extra={"event.action": "query_range", "logrite.i": i, "logrite.j": j})
        return self._query_range(self.root, i, j)

    def _build_tree(self, start, end):
        logger.error(">>> Entering _build_tree(start=%s,end=%s)", start, end, extra={"event.action": "_build_tree", "logrite.start": start, "logrite.end": end})
        if start == end:
            return SegmentTreeNode(start, end, self.collection[start])
        mid = (start + end) // 2
        left = self._build_tree(start, mid)
        right = self._build_tree(mid + 1, end)
        logger.warning("<<< Exiting _build_tree(start=%s,end=%s)", start, end, extra={"event.action": "_build_tree", "logrite.start": start, "logrite.end": end})
        return SegmentTreeNode(start, end, self.fn(left.val, right.val), left, right)

    def _update_tree(self, node, i, val):
        logger.error(">>> Entering _update_tree(node=%s,i=%s,val=%s)", node, i, val, extra={"event.action": "_update_tree", "logrite.node": node, "logrite.i": i, "logrite.val": val})
        if node.start == i and node.end == i:
            node.val = val
            logger.debug("_update_tree(self=%s,node=%s,i=%s,val=%s): node.val → %s", self, node, i, val, node.val, extra={"event.action": "_update_tree", "logrite.node": node, "logrite.i": i, "logrite.val": val})
            logger.warning("<<< Exiting _update_tree(node=%s,i=%s,val=%s)", node, i, val, extra={"event.action": "_update_tree", "logrite.node": node, "logrite.i": i, "logrite.val": val})
            return
        if i <= node.mid:
            self._update_tree(node.left, i, val)
        else:
            self._update_tree(node.right, i, val)
        node.val = self.fn(node.left.val, node.right.val)

    def _query_range(self, node, i, j):
        logger.error(">>> Entering _query_range(node=%s,i=%s,j=%s)", node, i, j, extra={"event.action": "_query_range", "logrite.node": node, "logrite.i": i, "logrite.j": j})
        if node.start == i and node.end == j:
            return node.val

        if i <= node.mid:
            if j <= node.mid:
                # range in left child tree
                return self._query_range(node.left, i, j)
            else:
                # range in left child tree and right child tree
                return self.fn(
                    self._query_range(node.left, i, node.mid),
                    self._query_range(node.right, node.mid + 1, j),
                )
        else:
            # range in right child tree
            logger.warning("<<< Exiting _query_range(node=%s,i=%s,j=%s)", node, i, j, extra={"event.action": "_query_range", "logrite.node": node, "logrite.i": i, "logrite.j": j})
            return self._query_range(node.right, i, j)

    def traverse(self):
        logger.error(">>> Entering traverse()", extra={"event.action": "traverse"})
        if self.root is not None:
            queue = Queue()
            logger.error("traverse(): queue → %s", queue, extra={"event.action": "traverse"})
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                logger.error("traverse(): node → %s", node, extra={"event.action": "traverse"})
                yield node

                if node.left is not None:
                    queue.put(node.left)

                if node.right is not None:
                    queue.put(node.right)
                    logger.warning("<<< Exiting traverse()", extra={"event.action": "traverse"})


if __name__ == "__main__":
    import operator

    for fn in [operator.add, max, min]:
        print("*" * 50)
        arr = SegmentTree([2, 1, 5, 3, 4], fn)
        for node in arr.traverse():
            print(node)
        print()

        arr.update(1, 5)
        for node in arr.traverse():
            print(node)
        print()

        print(arr.query_range(3, 4))  # 7
        print(arr.query_range(2, 2))  # 5
        print(arr.query_range(1, 3))  # 13
        print()
