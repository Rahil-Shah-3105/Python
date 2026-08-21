import math
import logging
logger = logging.getLogger(__name__)


class SegmentTree:
    def __init__(self, a):
        logger.debug(">>> Entering __init__(a=%s)", a)
        self.A = a
        logger.debug("__init__(self=%s,a=%s): self.A → %s", self, a, self.A)
        self.N = len(self.A)
        logger.debug("__init__(a=%s): self.N → %s", a, self.N)
        self.st = [0] * (
            4 * self.N
        )  # approximate the overall size of segment tree with array N
        if self.N:
            self.build(1, 0, self.N - 1)
            logger.debug("<<< Exiting __init__(a=%s)", a)

    def left(self, idx):
        """
        Returns the left child index for a given index in a binary tree.

        >>> s = SegmentTree([1, 2, 3])
        >>> s.left(1)
        2
        >>> s.left(2)
        4
        """
        logger.debug(">>> Entering left(idx=%s)", idx)
        logger.debug("<<< Exiting left(idx=%s)", idx)
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
        logger.debug(">>> Entering right(idx=%s)", idx)
        logger.debug("<<< Exiting right(idx=%s)", idx)
        return idx * 2 + 1

    def build(self, idx, left, right):
        logger.debug(">>> Entering build(idx=%s,left=%s,right=%s)", idx, left, right)
        if left == right:
            self.st[idx] = self.A[left]
        else:
            mid = (left + right) // 2
            logger.debug("build(self=%s,idx=%s,left=%s,right=%s): mid → %s", self, idx, left, right, mid)
            logger.debug("build(idx=%s,left=%s,right=%s): mid → %s", idx, left, right, mid)
            self.build(self.left(idx), left, mid)
            self.build(self.right(idx), mid + 1, right)
            self.st[idx] = max(self.st[self.left(idx)], self.st[self.right(idx)])
            logger.debug("<<< Exiting build(idx=%s,left=%s,right=%s)", idx, left, right)

    def update(self, a, b, val):
        """
        Update the values in the segment tree in the range [a,b] with the given value.

        >>> s = SegmentTree([1, 2, 3, 4, 5])
        >>> s.update(2, 4, 10)
        True
        >>> s.query(1, 5)
        10
        """
        logger.debug(">>> Entering update(a=%s,b=%s,val=%s)", a, b, val)
        logger.debug("<<< Exiting update(a=%s,b=%s,val=%s)", a, b, val)
        return self.update_recursive(1, 0, self.N - 1, a - 1, b - 1, val)

    def update_recursive(self, idx, left, right, a, b, val):
        """
        update(1, 1, N, a, b, v) for update val v to [a,b]
        """
        logger.debug(">>> Entering update_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s,val=%s)", idx, left, right, a, b, val)
        if right < a or left > b:
            return True
        if left == right:
            self.st[idx] = val
            return True
        mid = (left + right) // 2
        logger.debug("update_recursive(self=%s,idx=%s,left=%s,right=%s,a=%s,b=%s,val=%s): mid → %s", self, idx, left, right, a, b, val, mid)
        self.update_recursive(self.left(idx), left, mid, a, b, val)
        self.update_recursive(self.right(idx), mid + 1, right, a, b, val)
        self.st[idx] = max(self.st[self.left(idx)], self.st[self.right(idx)])
        logger.debug("<<< Exiting update_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s,val=%s)", idx, left, right, a, b, val)
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
        logger.debug(">>> Entering query(a=%s,b=%s)", a, b)
        logger.debug("<<< Exiting query(a=%s,b=%s)", a, b)
        return self.query_recursive(1, 0, self.N - 1, a - 1, b - 1)

    def query_recursive(self, idx, left, right, a, b):
        """
        query(1, 1, N, a, b) for query max of [a,b]
        """
        logger.debug(">>> Entering query_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s)", idx, left, right, a, b)
        if right < a or left > b:
            return -math.inf
        if left >= a and right <= b:
            return self.st[idx]
        mid = (left + right) // 2
        logger.debug("query_recursive(self=%s,idx=%s,left=%s,right=%s,a=%s,b=%s): mid → %s", self, idx, left, right, a, b, mid)
        q1 = self.query_recursive(self.left(idx), left, mid, a, b)
        q2 = self.query_recursive(self.right(idx), mid + 1, right, a, b)
        logger.debug("<<< Exiting query_recursive(idx=%s,left=%s,right=%s,a=%s,b=%s)", idx, left, right, a, b)
        return max(q1, q2)

    def show_data(self):
        logger.debug(">>> Entering show_data()")
        show_list = []
        logger.debug("show_data(self=%s): show_list → %s", self, show_list)
        for i in range(1, self.N + 1):
            show_list += [self.query(i, i)]
        print(show_list)
        logger.debug("<<< Exiting show_data()")


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
