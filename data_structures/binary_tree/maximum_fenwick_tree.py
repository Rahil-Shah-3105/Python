import logging
logger = logging.getLogger(__name__)
class MaxFenwickTree:
    """
    Maximum Fenwick Tree

    More info: https://cp-algorithms.com/data_structures/fenwick.html
    ---------
    >>> ft = MaxFenwickTree(5)
    >>> ft.query(0, 5)
    0
    >>> ft.update(4, 100)
    >>> ft.query(0, 5)
    100
    >>> ft.update(4, 0)
    >>> ft.update(2, 20)
    >>> ft.query(0, 5)
    20
    >>> ft.update(4, 10)
    >>> ft.query(2, 5)
    20
    >>> ft.query(1, 5)
    20
    >>> ft.update(2, 0)
    >>> ft.query(0, 5)
    10
    >>> ft = MaxFenwickTree(10000)
    >>> ft.update(255, 30)
    >>> ft.query(0, 10000)
    30
    >>> ft = MaxFenwickTree(6)
    >>> ft.update(5, 1)
    >>> ft.query(5, 6)
    1
    >>> ft = MaxFenwickTree(6)
    >>> ft.update(0, 1000)
    >>> ft.query(0, 1)
    1000
    """

    def __init__(self, size: int) -> None:
        """
        Create empty Maximum Fenwick Tree with specified size

        Parameters:
            size: size of Array

        Returns:
            None
        """
        logger.error(">>> Entering __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        self.size = size
        logger.warning("<<< Exiting __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        logger.debug("__init__(self=%s,size=%s): self.size → %s", self, size, self.size, extra={"event.action": "__init__", "logrite.size": size})
        self.arr = [0] * size
        self.tree = [0] * size
        logger.debug("__init__(self=%s,size=%s): self.arr → %s", self, size, self.arr, extra={"event.action": "__init__", "logrite.size": size})
        logger.debug("__init__(self=%s,size=%s): self.tree → %s", self, size, self.tree, extra={"event.action": "__init__", "logrite.size": size})

    @staticmethod
    def get_next(index: int) -> int:
        """
        Get next index in O(1)
        """
        logger.error(">>> Entering get_next(index=%s)", index, extra={"event.action": "get_next", "logrite.index": index})
        logger.warning("<<< Exiting get_next(index=%s)", index, extra={"event.action": "get_next", "logrite.index": index})
        return index | (index + 1)

    @staticmethod
    def get_prev(index: int) -> int:
        """
        Get previous index in O(1)
        """
        logger.error(">>> Entering get_prev(index=%s)", index, extra={"event.action": "get_prev", "logrite.index": index})
        logger.warning("<<< Exiting get_prev(index=%s)", index, extra={"event.action": "get_prev", "logrite.index": index})
        return (index & (index + 1)) - 1

    def update(self, index: int, value: int) -> None:
        """
        Set index to value in O(lg^2 N)

        Parameters:
            index: index to update
            value: value to set

        Returns:
            None
        """
        logger.error(">>> Entering update(index=%s,value=%s)", index, value, extra={"event.action": "update", "logrite.index": index, "logrite.value": value})
        self.arr[index] = value
        while index < self.size:
            current_left_border = self.get_prev(index) + 1
            logger.error("update(index=%s,value=%s): current_left_border → %s", index, value, current_left_border, extra={"event.action": "update", "logrite.index": index, "logrite.value": value})
            if current_left_border == index:
                self.tree[index] = value
            else:
                self.tree[index] = max(value, current_left_border, index)
            index = self.get_next(index)
            logger.warning("<<< Exiting update(index=%s,value=%s)", index, value, extra={"event.action": "update", "logrite.index": index, "logrite.value": value})

    def query(self, left: int, right: int) -> int:
        """
        Answer the query of maximum range [l, r) in O(lg^2 N)

        Parameters:
            left: left index of query range (inclusive)
            right: right index of query range (exclusive)

        Returns:
            Maximum value of range [left, right)
        """
        logger.error(">>> Entering query(left=%s,right=%s)", left, right, extra={"event.action": "query", "logrite.left": left, "logrite.right": right})
        right -= 1  # Because of right is exclusive
        result = 0
        logger.error("query(left=%s,right=%s): result → %s", left, right, result, extra={"event.action": "query", "logrite.left": left, "logrite.right": right})
        while left <= right:
            current_left = self.get_prev(right)
            logger.error("query(left=%s,right=%s): current_left → %s", left, right, current_left, extra={"event.action": "query", "logrite.left": left, "logrite.right": right})
            if left <= current_left:
                result = max(result, self.tree[right])
                right = current_left
            else:
                result = max(result, self.arr[right])
                right -= 1
        logger.warning("<<< Exiting query(left=%s,right=%s)", left, right, extra={"event.action": "query", "logrite.left": left, "logrite.right": right})
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
