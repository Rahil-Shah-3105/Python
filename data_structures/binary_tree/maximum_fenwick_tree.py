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
        logger.debug(">>> Entering __init__(size=%s)", size)
        self.size = size
        logger.debug("__init__(self=%s,size=%s): self.size → %s", self, size, self.size)
        logger.debug("<<< Exiting __init__(size=%s)", size)
        self.arr = [0] * size
        logger.debug("__init__(self=%s,size=%s): self.arr → %s", self, size, self.arr)
        self.tree = [0] * size
        logger.debug("__init__(self=%s,size=%s): self.tree → %s", self, size, self.tree)

    @staticmethod
    def get_next(index: int) -> int:
        """
        Get next index in O(1)
        """
        logger.debug(">>> Entering get_next(index=%s)", index)
        logger.debug("<<< Exiting get_next(index=%s)", index)
        return index | (index + 1)

    @staticmethod
    def get_prev(index: int) -> int:
        """
        Get previous index in O(1)
        """
        logger.debug(">>> Entering get_prev(index=%s)", index)
        logger.debug("<<< Exiting get_prev(index=%s)", index)
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
        logger.debug(">>> Entering update(index=%s,value=%s)", index, value)
        self.arr[index] = value
        while index < self.size:
            current_left_border = self.get_prev(index) + 1
            logger.debug("update(index=%s,value=%s): current_left_border → %s", index, value, current_left_border)
            if current_left_border == index:
                self.tree[index] = value
            else:
                self.tree[index] = max(value, current_left_border, index)
            index = self.get_next(index)
            logger.debug("<<< Exiting update(index=%s,value=%s)", index, value)

    def query(self, left: int, right: int) -> int:
        """
        Answer the query of maximum range [l, r) in O(lg^2 N)

        Parameters:
            left: left index of query range (inclusive)
            right: right index of query range (exclusive)

        Returns:
            Maximum value of range [left, right)
        """
        logger.debug(">>> Entering query(left=%s,right=%s)", left, right)
        right -= 1  # Because of right is exclusive
        result = 0
        logger.debug("query(left=%s,right=%s): result → %s", left, right, result)
        logger.debug("query(left=%s,right=%s): current_left → %s", left, right, current_left)
        logger.debug("query(self=%s,left=%s,right=%s): current_left → %s", self, left, right, current_left)
        while left <= right:
            current_left = self.get_prev(right)
            if left <= current_left:
                result = max(result, self.tree[right])
                right = current_left
            else:
                result = max(result, self.arr[right])
                right -= 1
        logger.debug("<<< Exiting query(left=%s,right=%s)", left, right)
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
