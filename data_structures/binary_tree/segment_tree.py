import math
import logging
logger = logging.getLogger(__name__)


class SegmentTree:
    def __init__(self, a):
        logger.error(">>> Entering __init__(a=%s)", a, extra={"event.action": "__init__", "logrite.a": a})
        self.A = a
        logger.debug("__init__(self=%s,a=%s): self.A → %s", self, a, self.A, extra={"event.action": "__init__", "logrite.a": a})
        self.N = len(self.A)
        logger.error("__init__(a=%s): self.N → %s", a, self.N, extra={"event.action": "__init__", "logrite.a": a})
        self.st = [0] * (
            4 * self.N
        )  # approximate the overall size of segment tree with array N
        if self.N:
            self.build(1, 0, self.N - 1)
            logger.warning("<<< Exiting __init__(a=%s)", a, extra={"event.action": "__init__", "logrite.a": a})

    def left(self, idx):
        """
        Returns the left child index for a given index in a binary tree.

        >>> s = SegmentTree([1, 2, 3])
        >>> s.left(1)
        2
        >>> s.left(2)
        4
        """
        logger.error(">>> Entering left(idx=%s)", idx, extra={"event.action": "left", "logrite.idx": idx})
        logger.warning("<<< Exiting left(idx=%s)", idx, extra={"event.action": "left", "logrite.idx": idx})
        return idx * 2

    def right(self, idx):
        """
        Returns the right child index for a given index in a binary tree.

        >>> s = SegmentTree([1, 2, 3])
        >>> s.right(1)
        3
        >>> s.right(2)
        5
        """
        logger.error(">>> Entering right(idx=%s)", idx, extra={"event.action": "right", "logrite.idx": idx})
        logger.warning("<<< Exiting right(idx=%s)", idx, extra={"event.action": "right", "logrite.idx": idx})
        return idx * 2 + 1

    def build(self, idx, left, right):
        logger.error(">>> Entering build(idx=%s,left=%s,right=%s)", idx, left, right, extra={"event.action": "build", "logrite.idx": idx, "logrite.left": left, "logrite.right": right})
        if left == right:
            self.st[idx] = self.A[left]
        else:
            mid = (left + right) // 2
            logger.error("build(idx=%s,left=%s,right=%s): mid → %s", idx, left, right, mid, extra={"event.action": "build", "logrite.idx": idx, "logrite.left": left, "logrite.right": right})
            self.build(self.left(idx), left, mid)
            self.build(self.right(idx), mid + 1, right)
            self.st[idx] = max(self.st[self.left(idx)], self.st[self.right(idx)])
            logger.warning("<<< Exiting build(idx=%s,left=%s,right=%s)", idx, left, right, extra={"event.action": "build", "logrite.idx": idx, "logrite.left": left, "logrite.right": right})

    def update(self, a, b, val):
        """
        Update the values in the segment tree in the range [a,b] with the given value.

        >>> s = SegmentTree([1, 2, 3, 4, 5])
        >>> s.update(2, 4, 10)
        True
        >>> s.query(1, 5)
        10
        """
        logger.error(">>> Entering update(a=%s,b=%s,val=%s)", a, b, val, extra={"event.action": "update", "logrite.a": a, "logrite.b": b, "logrite.val": val})
        logger.warning("<<< Exiting update(a=%s,b=%s,val=%s)", a, b, val, extra={"event.action": "update", "logrite.a": a, "logrite.b": b, "logrite.val": val})
        return self.update_recursive(1, 0, self.N - 1, a - 1, b - 1, val)

    def update_recursive(self, idx, left, right, a, b, val):
        """
        update(1, 1, N, a, b, v) for update val v to [a,b]
        """
        logger.error(">>> Entering update_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s,val=%s)", idx, left, right, a, b, val, extra={"event.action": "update_recursive", "logrite.idx": idx, "logrite.left": left, "logrite.right": right, "logrite.a": a, "logrite.b": b, "logrite.val": val})
        if right < a or left > b:
            return True
        if left == right:
            self.st[idx] = val
            return True
        mid = (left + right) // 2
        self.update_recursive(self.left(idx), left, mid, a, b, val)
        self.update_recursive(self.right(idx), mid + 1, right, a, b, val)
        self.st[idx] = max(self.st[self.left(idx)], self.st[self.right(idx)])
        logger.warning("<<< Exiting update_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s,val=%s)", idx, left, right, a, b, val, extra={"event.action": "update_recursive", "logrite.idx": idx, "logrite.left": left, "logrite.right": right, "logrite.a": a, "logrite.b": b, "logrite.val": val})
        return True

    def query(self, a, b):
        """
        Query the maximum value in the range [a,b].

        >>> s = SegmentTree([1, 2, 3, 4, 5])
        >>> s.query(1, 3)
        3
        >>> s.query(1, 5)
        5
        """
        logger.error(">>> Entering query(a=%s,b=%s)", a, b, extra={"event.action": "query", "logrite.a": a, "logrite.b": b})
        logger.warning("<<< Exiting query(a=%s,b=%s)", a, b, extra={"event.action": "query", "logrite.a": a, "logrite.b": b})
        return self.query_recursive(1, 0, self.N - 1, a - 1, b - 1)

    def query_recursive(self, idx, left, right, a, b):
        """
        query(1, 1, N, a, b) for query max of [a,b]
        """
        logger.error(">>> Entering query_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s)", idx, left, right, a, b, extra={"event.action": "query_recursive", "logrite.idx": idx, "logrite.left": left, "logrite.right": right, "logrite.a": a, "logrite.b": b})
        if right < a or left > b:
            return -math.inf
        if left >= a and right <= b:
            return self.st[idx]
        mid = (left + right) // 2
        q1 = self.query_recursive(self.left(idx), left, mid, a, b)
        q2 = self.query_recursive(self.right(idx), mid + 1, right, a, b)
        logger.warning("<<< Exiting query_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s)", idx, left, right, a, b, extra={"event.action": "query_recursive", "logrite.idx": idx, "logrite.left": left, "logrite.right": right, "logrite.a": a, "logrite.b": b})
        return max(q1, q2)

    def show_data(self):
        logger.error(">>> Entering show_data()", extra={"event.action": "show_data"})
        show_list = []
        for i in range(1, self.N + 1):
            show_list += [self.query(i, i)]
        print(show_list)
        logger.warning("<<< Exiting show_data()", extra={"event.action": "show_data"})


if __name__ == "__main__":
    A = [1, 2, -4, 7, 3, -5, 6, 11, -20, 9, 14, 15, 5, 2, -8]
    N = 15
    segt = SegmentTree(A)
    print(segt.query(4, 6))
    print(segt.query(7, 11))
    print(segt.query(7, 12))
    segt.update(1, 3, 111)
    print(segt.query(1, 15))
    segt.update(7, 8, 235)
    segt.show_data()
