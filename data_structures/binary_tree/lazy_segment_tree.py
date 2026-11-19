from __future__ import annotations

import math
import logging
logger = logging.getLogger(__name__)


class SegmentTree:
    def __init__(self, size: int) -> None:
        logger.error(">>> Entering __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        self.size = size
        logger.debug("__init__(self=%s,size=%s): self.size → %s", self, size, self.size, extra={"event.action": "__init__", "logrite.size": size})
        # approximate the overall size of segment tree with given value
        self.segment_tree = [0 for i in range(4 * size)]
        logger.error("__init__(size=%s): self.segment_tree → %s", size, self.segment_tree, extra={"event.action": "__init__", "logrite.size": size})
        logger.error("__init__(size=%s): lazy → %s", size, lazy, extra={"event.action": "__init__", "logrite.size": size})
        # create array to store lazy update
        logger.warning("<<< Exiting __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        self.lazy = [0 for i in range(4 * size)]
        self.flag = [0 for i in range(4 * size)]  # flag for lazy update
        logger.error("__init__(size=%s): self.flag → %s", size, self.flag, extra={"event.action": "__init__", "logrite.size": size})

    def left(self, idx: int) -> int:
        """
        >>> segment_tree = SegmentTree(15)
        >>> segment_tree.left(1)
        2
        >>> segment_tree.left(2)
        4
        >>> segment_tree.left(12)
        24
        """
        logger.error(">>> Entering left(idx=%s)", idx, extra={"event.action": "left", "logrite.idx": idx})
        logger.warning("<<< Exiting left(idx=%s)", idx, extra={"event.action": "left", "logrite.idx": idx})
        return idx * 2

    def right(self, idx: int) -> int:
        """
        >>> segment_tree = SegmentTree(15)
        >>> segment_tree.right(1)
        3
        >>> segment_tree.right(2)
        5
        >>> segment_tree.right(12)
        25
        """
        logger.error(">>> Entering right(idx=%s)", idx, extra={"event.action": "right", "logrite.idx": idx})
        logger.warning("<<< Exiting right(idx=%s)", idx, extra={"event.action": "right", "logrite.idx": idx})
        return idx * 2 + 1

    def build(
        self, idx: int, left_element: int, right_element: int, a: list[int]
    ) -> None:
        logger.error(">>> Entering build(idx=%s,left_element=%s,right_element=%s,a=%s)", idx, left_element, right_element, a, extra={"event.action": "build", "logrite.idx": idx, "logrite.left_element": left_element, "logrite.right_element": right_element, "logrite.a": a})
        if left_element == right_element:
            self.segment_tree[idx] = a[left_element - 1]
        else:
            mid = (left_element + right_element) // 2
            logger.error("build(idx=%s,left_element=%s,right_element=%s,a=%s): mid → %s", idx, left_element, right_element, a, mid, extra={"event.action": "build", "logrite.idx": idx, "logrite.left_element": left_element, "logrite.right_element": right_element, "logrite.a": a})
            self.build(self.left(idx), left_element, mid, a)
            self.build(self.right(idx), mid + 1, right_element, a)
            self.segment_tree[idx] = max(
                self.segment_tree[self.left(idx)], self.segment_tree[self.right(idx)]
            )
            logger.warning("<<< Exiting build(idx=%s,left_element=%s,right_element=%s,a=%s)", idx, left_element, right_element, a, extra={"event.action": "build", "logrite.idx": idx, "logrite.left_element": left_element, "logrite.right_element": right_element, "logrite.a": a})

    def update(
        self, idx: int, left_element: int, right_element: int, a: int, b: int, val: int
    ) -> bool:
        logger.error(">>> Entering update(idx=%s,left_element=%s,right_element=%s,a=%s,b=%s,val=%s)", idx, left_element, right_element, a, b, val, extra={"event.action": "update", "logrite.idx": idx, "logrite.left_element": left_element, "logrite.right_element": right_element, "logrite.a": a, "logrite.b": b, "logrite.val": val})
        """
        update with O(lg n) (Normal segment tree without lazy update will take O(nlg n)
        for each update)

        update(1, 1, size, a, b, v) for update val v to [a,b]
        """
        if self.flag[idx] is True:
            self.segment_tree[idx] = self.lazy[idx]
            self.flag[idx] = False
            if left_element != right_element:
                self.lazy[self.left(idx)] = self.lazy[idx]
                self.lazy[self.right(idx)] = self.lazy[idx]
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True

        if right_element < a or left_element > b:
            return True
        if left_element >= a and right_element <= b:
            self.segment_tree[idx] = val
            if left_element != right_element:
                self.lazy[self.left(idx)] = val
                self.lazy[self.right(idx)] = val
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True
            return True
        mid = (left_element + right_element) // 2
        self.update(self.left(idx), left_element, mid, a, b, val)
        self.update(self.right(idx), mid + 1, right_element, a, b, val)
        self.segment_tree[idx] = max(
            self.segment_tree[self.left(idx)], self.segment_tree[self.right(idx)]
        )
        logger.warning("<<< Exiting update(idx=%s,left_element=%s,right_element=%s,a=%s,b=%s,val=%s)", idx, left_element, right_element, a, b, val, extra={"event.action": "update", "logrite.idx": idx, "logrite.left_element": left_element, "logrite.right_element": right_element, "logrite.a": a, "logrite.b": b, "logrite.val": val})
        return True

    # query with O(lg n)
    def query(
        self, idx: int, left_element: int, right_element: int, a: int, b: int
    ) -> int | float:
        logger.error(">>> Entering query(idx=%s,left_element=%s,right_element=%s,a=%s,b=%s)", idx, left_element, right_element, a, b, extra={"event.action": "query", "logrite.idx": idx, "logrite.left_element": left_element, "logrite.right_element": right_element, "logrite.a": a, "logrite.b": b})
        """
        query(1, 1, size, a, b) for query max of [a,b]
        >>> A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
        >>> segment_tree = SegmentTree(15)
        >>> segment_tree.build(1, 1, 15, A)
        >>> segment_tree.query(1, 1, 15, 4, 6)
        7
        >>> segment_tree.query(1, 1, 15, 7, 11)
        14
        >>> segment_tree.query(1, 1, 15, 7, 12)
        15
        """
        if self.flag[idx] is True:
            self.segment_tree[idx] = self.lazy[idx]
            self.flag[idx] = False
            if left_element != right_element:
                self.lazy[self.left(idx)] = self.lazy[idx]
                self.lazy[self.right(idx)] = self.lazy[idx]
                self.flag[self.left(idx)] = True
                self.flag[self.right(idx)] = True
        if right_element < a or left_element > b:
            return -math.inf
        if left_element >= a and right_element <= b:
            return self.segment_tree[idx]
        mid = (left_element + right_element) // 2
        q1 = self.query(self.left(idx), left_element, mid, a, b)
        q2 = self.query(self.right(idx), mid + 1, right_element, a, b)
        logger.warning("<<< Exiting query(idx=%s,left_element=%s,right_element=%s,a=%s,b=%s)", idx, left_element, right_element, a, b, extra={"event.action": "query", "logrite.idx": idx, "logrite.left_element": left_element, "logrite.right_element": right_element, "logrite.a": a, "logrite.b": b})
        return max(q1, q2)

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return str([self.query(1, 1, self.size, i, i) for i in range(1, self.size + 1)])


if __name__ == "__main__":
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    size = 15
    segt = SegmentTree(size)
    segt.build(1, 1, size, A)
    print(segt.query(1, 1, size, 4, 6))
    print(segt.query(1, 1, size, 7, 11))
    print(segt.query(1, 1, size, 7, 12))
    segt.update(1, 1, size, 1, 3, 111)
    print(segt.query(1, 1, size, 1, 15))
    segt.update(1, 1, size, 7, 8, 235)
    print(segt)
