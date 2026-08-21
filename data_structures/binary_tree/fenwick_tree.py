from copy import deepcopy
import logging
logger = logging.getLogger(__name__)


class FenwickTree:
    """
    Fenwick Tree

    More info: https://en.wikipedia.org/wiki/Fenwick_tree
    """

    def __init__(self, arr: list[int] | None = None, size: int | None = None) -> None:
        """
        Constructor for the Fenwick tree

        Parameters:
            arr (list): list of elements to initialize the tree with (optional)
            size (int): size of the Fenwick tree (if arr is None)
        """
        logger.debug(">>> Entering __init__(arr=%s,size=%s)", arr, size)

        if arr is None and size is not None:
            self.size = size
            logger.debug("__init__(self=%s,arr=%s,size=%s): self.size → %s", self, arr, size, self.size)
            self.tree = [0] * size
            logger.debug("__init__(self=%s,arr=%s,size=%s): self.tree → %s", self, arr, size, self.tree)
        elif arr is not None:
            self.init(arr)
        else:
            logger.debug("<<< Exiting __init__(arr=%s,size=%s)", arr, size)
            raise ValueError("Either arr or size must be specified")

    def init(self, arr: list[int]) -> None:
        """
        Initialize the Fenwick tree with arr in O(N)

        Parameters:
            arr (list): list of elements to initialize the tree with

        Returns:
            None

        >>> a = [1, 2, 3, 4, 5]
        >>> f1 = FenwickTree(a)
        >>> f2 = FenwickTree(size=len(a))
        >>> for index, value in enumerate(a):
        ...     f2.add(index, value)
        >>> f1.tree == f2.tree
        True
        """
        logger.debug(">>> Entering init(arr=%s)", arr)
        logger.debug("init(arr=%s): size → %s", arr, size)
        self.size = len(arr)
        self.tree = deepcopy(arr)
        logger.debug("init(arr=%s): self.tree → %s", arr, self.tree)
        for i in range(1, self.size):
            j = self.next_(i)
            if j < self.size:
                self.tree[j] += self.tree[i]
                logger.debug("<<< Exiting init(arr=%s)", arr)

    def get_array(self) -> list[int]:
        """
        Get the Normal Array of the Fenwick tree in O(N)

        Returns:
            list: Normal Array of the Fenwick tree

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> f.get_array() == a
        True
        """
        logger.debug(">>> Entering get_array()")
        arr = self.tree[:]
        logger.debug("get_array(self=%s): arr → %s", self, arr)
        for i in range(self.size - 1, 0, -1):
            j = self.next_(i)
            if j < self.size:
                arr[j] -= arr[i]
        logger.debug("<<< Exiting get_array()")
        return arr

    @staticmethod
    def next_(index: int) -> int:
        logger.debug(">>> Entering next_(index=%s)", index)
        logger.debug("<<< Exiting next_(index=%s)", index)
        return index + (index & (-index))

    @staticmethod
    def prev(index: int) -> int:
        logger.debug(">>> Entering prev(index=%s)", index)
        logger.debug("<<< Exiting prev(index=%s)", index)
        return index - (index & (-index))

    def add(self, index: int, value: int) -> None:
        """
        Add a value to index in O(lg N)

        Parameters:
            index (int): index to add value to
            value (int): value to add to index

        Returns:
            None

        >>> f = FenwickTree([1, 2, 3, 4, 5])
        >>> f.add(0, 1)
        >>> f.add(1, 2)
        >>> f.add(2, 3)
        >>> f.add(3, 4)
        >>> f.add(4, 5)
        >>> f.get_array()
        [2, 4, 6, 8, 10]
        """
        logger.debug(">>> Entering add(index=%s,value=%s)", index, value)
        if index == 0:
            self.tree[0] += value
            logger.debug("<<< Exiting add(index=%s,value=%s)", index, value)
            return
        while index < self.size:
            self.tree[index] += value
            index = self.next_(index)

    def update(self, index: int, value: int) -> None:
        """
        Set the value of index in O(lg N)

        Parameters:
            index (int): index to set value to
            value (int): value to set in index

        Returns:
            None

        >>> f = FenwickTree([5, 4, 3, 2, 1])
        >>> f.update(0, 1)
        >>> f.update(1, 2)
        >>> f.update(2, 3)
        >>> f.update(3, 4)
        >>> f.update(4, 5)
        >>> f.get_array()
        [1, 2, 3, 4, 5]
        """
        logger.debug(">>> Entering update(index=%s,value=%s)", index, value)
        self.add(index, value - self.get(index))
        logger.debug("<<< Exiting update(index=%s,value=%s)", index, value)

    def prefix(self, right: int) -> int:
        """
        Prefix sum of all elements in [0, right) in O(lg N)

        Parameters:
            right (int): right bound of the query (exclusive)

        Returns:
            int: sum of all elements in [0, right)

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     res = res and f.prefix(i) == sum(a[:i])
        >>> res
        True
        """
        logger.debug(">>> Entering prefix(right=%s)", right)
        if right == 0:
            return 0
        result = self.tree[0]
        right -= 1  # make right inclusive
        while right > 0:
            result += self.tree[right]
            right = self.prev(right)
        logger.debug("<<< Exiting prefix(right=%s)", right)
        return result

    def query(self, left: int, right: int) -> int:
        """
        Query the sum of all elements in [left, right) in O(lg N)

        Parameters:
            left (int): left bound of the query (inclusive)
            right (int): right bound of the query (exclusive)

        Returns:
            int: sum of all elements in [left, right)

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     for j in range(i + 1, len(a)):
        ...         res = res and f.query(i, j) == sum(a[i:j])
        >>> res
        True
        """
        logger.debug(">>> Entering query(left=%s,right=%s)", left, right)
        logger.debug("<<< Exiting query(left=%s,right=%s)", left, right)
        return self.prefix(right) - self.prefix(left)

    def get(self, index: int) -> int:
        """
        Get value at index in O(lg N)

        Parameters:
            index (int): index to get the value

        Returns:
            int: Value of element at index

        >>> a = [i for i in range(128)]
        >>> f = FenwickTree(a)
        >>> res = True
        >>> for i in range(len(a)):
        ...     res = res and f.get(i) == a[i]
        >>> res
        True
        """
        logger.debug(">>> Entering get(index=%s)", index)
        logger.debug("<<< Exiting get(index=%s)", index)
        return self.query(index, index + 1)

    def rank_query(self, value: int) -> int:
        """
        Find the largest index with prefix(i) <= value in O(lg N)
        NOTE: Requires that all values are non-negative!

        Parameters:
            value (int): value to find the largest index of

        Returns:
            -1: if value is smaller than all elements in prefix sum
            int: largest index with prefix(i) <= value

        >>> f = FenwickTree([1, 2, 0, 3, 0, 5])
        >>> f.rank_query(0)
        -1
        >>> f.rank_query(2)
        0
        >>> f.rank_query(1)
        0
        >>> f.rank_query(3)
        2
        >>> f.rank_query(5)
        2
        >>> f.rank_query(6)
        4
        >>> f.rank_query(11)
        5
        """
        logger.debug(">>> Entering rank_query(value=%s)", value)
        value -= self.tree[0]
        if value < 0:
            return -1

        j = 1  # Largest power of 2 <= size
        while j * 2 < self.size:
            j *= 2

        i = 0

        while j > 0:
            if i + j < self.size and self.tree[i + j] <= value:
                value -= self.tree[i + j]
                i += j
            j //= 2
        logger.debug("<<< Exiting rank_query(value=%s)", value)
        return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
