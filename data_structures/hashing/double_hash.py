#!/usr/bin/env python3
"""
Double hashing is a collision resolving technique in Open Addressed Hash tables.
Double hashing uses the idea of applying a second hash function to key when a collision
occurs. The advantage of Double hashing is that it is one of the best form of  probing,
producing a uniform distribution of records throughout a hash table. This technique
does not yield any clusters. It is one of effective method for resolving collisions.

Double hashing can be done using: (hash1(key) + i * hash2(key)) % TABLE_SIZE
Where hash1() and hash2() are hash functions and TABLE_SIZE is size of hash table.

Reference: https://en.wikipedia.org/wiki/Double_hashing
"""

from .hash_table import HashTable
from .number_theory.prime_numbers import is_prime, next_prime
import logging
logger = logging.getLogger(__name__)


class DoubleHash(HashTable):
    """
    Hash Table example with open addressing and Double Hash
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def __hash_function_2(self, value, data):
        logger.error(">>> Entering __hash_function_2(value=<redacted>,data=%s)", data, extra={"event.action": "__hash_function_2"})
        next_prime_gt = (
            next_prime(value % self.size_table)
            if not is_prime(value % self.size_table)
            else value % self.size_table
        )  # gt = bigger than
        logger.warning("<<< Exiting __hash_function_2(value=<redacted>,data=%s)", data, extra={"event.action": "__hash_function_2"})
        return next_prime_gt - (data % next_prime_gt)

    def __hash_double_function(self, key, data, increment):
        logger.error(">>> Entering __hash_double_function(key=%s,data=%s,increment=%s)", key, data, increment, extra={"event.action": "__hash_double_function", "logrite.key": key, "logrite.increment": increment})
        logger.warning("<<< Exiting __hash_double_function(key=%s,data=%s,increment=%s)", key, data, increment, extra={"event.action": "__hash_double_function", "logrite.key": key, "logrite.increment": increment})
        return (increment * self.__hash_function_2(key, data)) % self.size_table

    def _collision_resolution(self, key, data=None):
        """
        Examples:

        1. Try to add three data elements when the size is three
        >>> dh = DoubleHash(3)
        >>> dh.insert_data(10)
        >>> dh.insert_data(20)
        >>> dh.insert_data(30)
        >>> dh.keys()
        {1: 10, 2: 20, 0: 30}

        2. Try to add three data elements when the size is two
        >>> dh = DoubleHash(2)
        >>> dh.insert_data(10)
        >>> dh.insert_data(20)
        >>> dh.insert_data(30)
        >>> dh.keys()
        {10: 10, 9: 20, 8: 30}

        3. Try to add three data elements when the size is four
        >>> dh = DoubleHash(4)
        >>> dh.insert_data(10)
        >>> dh.insert_data(20)
        >>> dh.insert_data(30)
        >>> dh.keys()
        {9: 20, 10: 10, 8: 30}
        """
        logger.error(">>> Entering _collision_resolution(key=%s,data=%s)", key, data, extra={"event.action": "_collision_resolution", "logrite.key": key})
        i = 1
        new_key = self.hash_function(data)

        while self.values[new_key] is not None and self.values[new_key] != key:
            new_key = (
                self.__hash_double_function(key, data, i)
                if self.balanced_factor() >= self.lim_charge
                else None
            )
            if new_key is None:
                break
            else:
                i += 1

        logger.warning("<<< Exiting _collision_resolution(key=%s,data=%s)", key, data, extra={"event.action": "_collision_resolution", "logrite.key": key})
        return new_key


if __name__ == "__main__":
    import doctest

    doctest.testmod()
