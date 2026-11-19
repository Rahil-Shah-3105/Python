"""
A number container system that uses binary search to delete and insert values into
arrays with O(log n) write times and O(1) read times.

This container system holds integers at indexes.

Further explained in this leetcode problem
> https://leetcode.com/problems/minimum-cost-tree-from-leaf-values
"""
import logging
logger = logging.getLogger(__name__)


class NumberContainer:
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        # numbermap keys are the number and its values are lists of indexes sorted
        # in ascending order
        self.numbermap: dict[int, list[int]] = {}
        # indexmap keys are an index and it's values are the number at that index
        self.indexmap: dict[int, int] = {}
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def binary_search_delete(self, array: list | str | range, item: int) -> list[int]:
        """
        Removes the item from the sorted array and returns
        the new array.

        >>> NumberContainer().binary_search_delete([1,2,3], 2)
        [1, 3]
        >>> NumberContainer().binary_search_delete([0, 0, 0], 0)
        [0, 0]
        >>> NumberContainer().binary_search_delete([-1, -1, -1], -1)
        [-1, -1]
        >>> NumberContainer().binary_search_delete([-1, 0], 0)
        [-1]
        >>> NumberContainer().binary_search_delete([-1, 0], -1)
        [0]
        >>> NumberContainer().binary_search_delete(range(7), 3)
        [0, 1, 2, 4, 5, 6]
        >>> NumberContainer().binary_search_delete([1.1, 2.2, 3.3], 2.2)
        [1.1, 3.3]
        >>> NumberContainer().binary_search_delete("abcde", "c")
        ['a', 'b', 'd', 'e']
        >>> NumberContainer().binary_search_delete([0, -1, 2, 4], 0)
        Traceback (most recent call last):
            ...
        ValueError: Either the item is not in the array or the array was unsorted
        >>> NumberContainer().binary_search_delete([2, 0, 4, -1, 11], -1)
        Traceback (most recent call last):
            ...
        ValueError: Either the item is not in the array or the array was unsorted
        >>> NumberContainer().binary_search_delete(125, 1)
        Traceback (most recent call last):
            ...
        TypeError: binary_search_delete() only accepts either a list, range or str
        """
        logger.error(">>> Entering binary_search_delete(array=%s,item=%s)", array, item, extra={"event.action": "binary_search_delete", "logrite.array": array, "logrite.item": item})
        if isinstance(array, (range, str)):
            array = list(array)
        elif not isinstance(array, list):
            logger.error("binary_search_delete(array=%s,item=%s): array → %s", array, item, array, extra={"event.action": "binary_search_delete", "logrite.array": array, "logrite.item": item})
            raise TypeError(
                "binary_search_delete() only accepts either a list, range or str"
            )

        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            logger.error("binary_search_delete(array=%s,item=%s): mid → %s", array, item, mid, extra={"event.action": "binary_search_delete", "logrite.array": array, "logrite.item": item})
            if array[mid] == item:
                array.pop(mid)
                return array
            elif array[mid] < item:
                logger.warning("<<< Exiting binary_search_delete(array=%s,item=%s)", array, item, extra={"event.action": "binary_search_delete", "logrite.array": array, "logrite.item": item})
                low = mid + 1
            else:
                high = mid - 1
        raise ValueError(
            "Either the item is not in the array or the array was unsorted"
        )

    def binary_search_insert(self, array: list | str | range, index: int) -> list[int]:
        """
        Inserts the index into the sorted array
        at the correct position.

        >>> NumberContainer().binary_search_insert([1,2,3], 2)
        [1, 2, 2, 3]
        >>> NumberContainer().binary_search_insert([0,1,3], 2)
        [0, 1, 2, 3]
        >>> NumberContainer().binary_search_insert([-5, -3, 0, 0, 11, 103], 51)
        [-5, -3, 0, 0, 11, 51, 103]
        >>> NumberContainer().binary_search_insert([-5, -3, 0, 0, 11, 100, 103], 101)
        [-5, -3, 0, 0, 11, 100, 101, 103]
        >>> NumberContainer().binary_search_insert(range(10), 4)
        [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
        >>> NumberContainer().binary_search_insert("abd", "c")
        ['a', 'b', 'c', 'd']
        >>> NumberContainer().binary_search_insert(131, 23)
        Traceback (most recent call last):
            ...
        TypeError: binary_search_insert() only accepts either a list, range or str
        """
        logger.error(">>> Entering binary_search_insert(array=%s,index=%s)", array, index, extra={"event.action": "binary_search_insert", "logrite.array": array, "logrite.index": index})
        if isinstance(array, (range, str)):
            array = list(array)
        elif not isinstance(array, list):
            logger.error("binary_search_insert(array=%s,index=%s): array → %s", array, index, array, extra={"event.action": "binary_search_insert", "logrite.array": array, "logrite.index": index})
            raise TypeError(
                "binary_search_insert() only accepts either a list, range or str"
            )

        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            logger.error("binary_search_insert(array=%s,index=%s): mid → %s", array, index, mid, extra={"event.action": "binary_search_insert", "logrite.array": array, "logrite.index": index})
            if array[mid] == index:
                # If the item already exists in the array,
                # insert it after the existing item
                array.insert(mid + 1, index)
                return array
            elif array[mid] < index:
                low = mid + 1
            else:
                high = mid - 1

        # If the item doesn't exist in the array, insert it at the appropriate position
        array.insert(low, index)
        logger.warning("<<< Exiting binary_search_insert(array=%s,index=%s)", array, index, extra={"event.action": "binary_search_insert", "logrite.array": array, "logrite.index": index})
        return array

    def change(self, index: int, number: int) -> None:
        """
        Changes (sets) the index as number

        >>> cont = NumberContainer()
        >>> cont.change(0, 10)
        >>> cont.change(0, 20)
        >>> cont.change(-13, 20)
        >>> cont.change(-100030, 20032903290)
        """
        logger.error(">>> Entering change(index=%s,number=%s)", index, number, extra={"event.action": "change", "logrite.index": index, "logrite.number": number})
        # Remove previous index
        if index in self.indexmap:
            n = self.indexmap[index]
            if len(self.numbermap[n]) == 1:
                del self.numbermap[n]
            else:
                self.numbermap[n] = self.binary_search_delete(self.numbermap[n], index)

        # Set new index
        self.indexmap[index] = number

        # Number not seen before or empty so insert number value
        if number not in self.numbermap:
            self.numbermap[number] = [index]

        # Here we need to perform a binary search insertion in order to insert
        # The item in the correct place
        else:
            self.numbermap[number] = self.binary_search_insert(
                self.numbermap[number], index
            )
            logger.warning("<<< Exiting change(index=%s,number=%s)", index, number, extra={"event.action": "change", "logrite.index": index, "logrite.number": number})

    def find(self, number: int) -> int:
        """
        Returns the smallest index where the number is.

        >>> cont = NumberContainer()
        >>> cont.find(10)
        -1
        >>> cont.change(0, 10)
        >>> cont.find(10)
        0
        >>> cont.change(0, 20)
        >>> cont.find(10)
        -1
        >>> cont.find(20)
        0
        """
        logger.error(">>> Entering find(number=%s)", number, extra={"event.action": "find", "logrite.number": number})
        # Simply return the 0th index (smallest) of the indexes found (or -1)
        logger.warning("<<< Exiting find(number=%s)", number, extra={"event.action": "find", "logrite.number": number})
        return self.numbermap.get(number, [-1])[0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
