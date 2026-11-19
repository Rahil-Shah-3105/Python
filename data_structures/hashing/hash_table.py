#!/usr/bin/env python3
from abc import abstractmethod

from .number_theory.prime_numbers import next_prime
import logging
logger = logging.getLogger(__name__)


class HashTable:
    """
    Basic Hash Table example with open addressing and linear probing
    """

    def __init__(
        self,
        size_table: int,
        charge_factor: int | None = None,
        lim_charge: float | None = None,
    ) -> None:
        logger.error(">>> Entering __init__(size_table=%s,charge_factor=%s,lim_charge=%s)", size_table, charge_factor, lim_charge, extra={"event.action": "__init__", "logrite.size_table": size_table, "logrite.charge_factor": charge_factor, "logrite.lim_charge": lim_charge})
        self.size_table = size_table
        logger.debug("__init__(self=%s,size_table=%s,charge_factor=%s,lim_charge=%s): self.size_table → %s", self, size_table, charge_factor, lim_charge, self.size_table, extra={"event.action": "__init__", "logrite.size_table": size_table, "logrite.charge_factor": charge_factor, "logrite.lim_charge": lim_charge})
        self.values = [None] * self.size_table
        logger.debug("__init__(self=%s,size_table=%s,charge_factor=%s,lim_charge=%s): self.values → %s", self, size_table, charge_factor, lim_charge, self.values, extra={"event.action": "__init__", "logrite.size_table": size_table, "logrite.charge_factor": charge_factor, "logrite.lim_charge": lim_charge})
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        logger.debug("__init__(self=%s,size_table=%s,charge_factor=%s,lim_charge=%s): self.lim_charge → %s", self, size_table, charge_factor, lim_charge, self.lim_charge, extra={"event.action": "__init__", "logrite.size_table": size_table, "logrite.charge_factor": charge_factor, "logrite.lim_charge": lim_charge})
        self.charge_factor = 1 if charge_factor is None else charge_factor
        logger.debug("__init__(self=%s,size_table=%s,charge_factor=%s,lim_charge=%s): self.charge_factor → %s", self, size_table, charge_factor, lim_charge, self.charge_factor, extra={"event.action": "__init__", "logrite.size_table": size_table, "logrite.charge_factor": charge_factor, "logrite.lim_charge": lim_charge})
        self.__aux_list: list = []
        self._keys: dict = {}
        logger.warning("<<< Exiting __init__(size_table=%s,charge_factor=%s,lim_charge=%s)", size_table, charge_factor, lim_charge, extra={"event.action": "__init__", "logrite.size_table": size_table, "logrite.charge_factor": charge_factor, "logrite.lim_charge": lim_charge})

    def keys(self):
        """
        The keys function returns a dictionary containing the key value pairs.
        key being the index number in hash table and value being the data value.

        Examples:
        1. creating HashTable with size 10 and inserting 3 elements
        >>> ht = HashTable(10)
        >>> ht.insert_data(10)
        >>> ht.insert_data(20)
        >>> ht.insert_data(30)
        >>> ht.keys()
        {0: 10, 1: 20, 2: 30}

        2. creating HashTable with size 5 and inserting 5 elements
        >>> ht = HashTable(5)
        >>> ht.insert_data(5)
        >>> ht.insert_data(4)
        >>> ht.insert_data(3)
        >>> ht.insert_data(2)
        >>> ht.insert_data(1)
        >>> ht.keys()
        {0: 5, 4: 4, 3: 3, 2: 2, 1: 1}
        """
        logger.error(">>> Entering keys()", extra={"event.action": "keys"})
        logger.warning("<<< Exiting keys()", extra={"event.action": "keys"})
        return self._keys

    def balanced_factor(self):
        logger.error(">>> Entering balanced_factor()", extra={"event.action": "balanced_factor"})
        logger.warning("<<< Exiting balanced_factor()", extra={"event.action": "balanced_factor"})
        return sum(1 for slot in self.values if slot is not None) / (
            self.size_table * self.charge_factor
        )

    def hash_function(self, key):
        """
        Generates hash for the given key value

        Examples:

        Creating HashTable with size 5
        >>> ht = HashTable(5)
        >>> ht.hash_function(10)
        0
        >>> ht.hash_function(20)
        0
        >>> ht.hash_function(4)
        4
        >>> ht.hash_function(18)
        3
        >>> ht.hash_function(-18)
        2
        >>> ht.hash_function(18.5)
        3.5
        >>> ht.hash_function(0)
        0
        >>> ht.hash_function(-0)
        0
        """
        logger.error(">>> Entering hash_function(key=%s)", key, extra={"event.action": "hash_function", "logrite.key": key})
        logger.warning("<<< Exiting hash_function(key=%s)", key, extra={"event.action": "hash_function", "logrite.key": key})
        return key % self.size_table

    def _step_by_step(self, step_ord):
        logger.error(">>> Entering _step_by_step(step_ord=%s)", step_ord, extra={"event.action": "_step_by_step", "logrite.step_ord": step_ord})
        print(f"step {step_ord}")
        print(list(range(len(self.values))))
        print(self.values)
        logger.warning("<<< Exiting _step_by_step(step_ord=%s)", step_ord, extra={"event.action": "_step_by_step", "logrite.step_ord": step_ord})

    def bulk_insert(self, values):
        """
        bulk_insert is used for entering more than one element at a time
        in the HashTable.

        Examples:
        1.
        >>> ht = HashTable(5)
        >>> ht.bulk_insert((10,20,30))
        step 1
        [0, 1, 2, 3, 4]
        [10, None, None, None, None]
        step 2
        [0, 1, 2, 3, 4]
        [10, 20, None, None, None]
        step 3
        [0, 1, 2, 3, 4]
        [10, 20, 30, None, None]

        2.
        >>> ht = HashTable(5)
        >>> ht.bulk_insert([5,4,3,2,1])
        step 1
        [0, 1, 2, 3, 4]
        [5, None, None, None, None]
        step 2
        [0, 1, 2, 3, 4]
        [5, None, None, None, 4]
        step 3
        [0, 1, 2, 3, 4]
        [5, None, None, 3, 4]
        step 4
        [0, 1, 2, 3, 4]
        [5, None, 2, 3, 4]
        step 5
        [0, 1, 2, 3, 4]
        [5, 1, 2, 3, 4]
        """
        logger.error(">>> Entering bulk_insert(values=%s)", values, extra={"event.action": "bulk_insert", "logrite.values": values})
        i = 1
        self.__aux_list = values
        logger.debug("bulk_insert(self=%s,values=%s): self.__aux_list → %s", self, values, self.__aux_list, extra={"event.action": "bulk_insert", "logrite.values": values})
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1
            logger.warning("<<< Exiting bulk_insert(values=%s)", values, extra={"event.action": "bulk_insert", "logrite.values": values})

    def _set_value(self, key, data):
        """
        _set_value functions allows to update value at a particular hash

        Examples:
        1. _set_value in HashTable of size 5
        >>> ht = HashTable(5)
        >>> ht.insert_data(10)
        >>> ht.insert_data(20)
        >>> ht.insert_data(30)
        >>> ht._set_value(0,15)
        >>> ht.keys()
        {0: 15, 1: 20, 2: 30}

        2. _set_value in HashTable of size 2
        >>> ht = HashTable(2)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht._set_value(3,15)
        >>> ht.keys()
        {3: 15, 2: 17, 4: 99}

        3. _set_value in HashTable when hash is not present
        >>> ht = HashTable(2)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht._set_value(0,15)
        >>> ht.keys()
        {3: 18, 2: 17, 4: 99, 0: 15}

        4. _set_value in HashTable when multiple hash are not present
        >>> ht = HashTable(2)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht._set_value(0,15)
        >>> ht._set_value(1,20)
        >>> ht.keys()
        {3: 18, 2: 17, 4: 99, 0: 15, 1: 20}
        """
        logger.error(">>> Entering _set_value(key=%s,data=%s)", key, data, extra={"event.action": "_set_value", "logrite.key": key})
        self.values[key] = data
        self._keys[key] = data
        logger.warning("<<< Exiting _set_value(key=%s,data=%s)", key, data, extra={"event.action": "_set_value", "logrite.key": key})

    @abstractmethod
    def _collision_resolution(self, key, data=None):
        """
        This method is a type of open addressing which is used for handling collision.

        In this implementation the concept of linear probing has been used.

        The hash table is searched sequentially from the original location of the
        hash, if the new hash/location we get is already occupied we check for the next
        hash/location.

        references:
            - https://en.wikipedia.org/wiki/Linear_probing

        Examples:
        1. The collision will be with keys 18 & 99, so new hash will be created for 99
        >>> ht = HashTable(3)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht.keys()
        {2: 17, 0: 18, 1: 99}

        2. The collision will be with keys 17 & 101, so new hash
        will be created for 101
        >>> ht = HashTable(4)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht.insert_data(101)
        >>> ht.keys()
        {1: 17, 2: 18, 3: 99, 0: 101}

        2. The collision will be with all keys, so new hash will be created for all
        >>> ht = HashTable(1)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99)
        >>> ht.keys()
        {2: 17, 3: 18, 4: 99}

        3. Trying to insert float key in hash
        >>> ht = HashTable(1)
        >>> ht.insert_data(17)
        >>> ht.insert_data(18)
        >>> ht.insert_data(99.99)
        Traceback (most recent call last):
        ...
        TypeError: list indices must be integers or slices, not float
        """
        logger.error(">>> Entering _collision_resolution(key=%s,data=%s)", key, data, extra={"event.action": "_collision_resolution", "logrite.key": key})
        new_key = self.hash_function(key + 1)

        while self.values[new_key] is not None and self.values[new_key] != key:
            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key + 1)
            else:
                new_key = None
                break

        logger.warning("<<< Exiting _collision_resolution(key=%s,data=%s)", key, data, extra={"event.action": "_collision_resolution", "logrite.key": key})
        return new_key

    def rehashing(self):
        logger.error(">>> Entering rehashing()", extra={"event.action": "rehashing"})
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        logger.error("rehashing(): self.size_table → %s", self.size_table, extra={"event.action": "rehashing"})
        self._keys.clear()
        self.values = [None] * self.size_table  # hell's pointers D: don't DRY ;/
        logger.debug("rehashing(self=%s): self.values → %s", self, self.values, extra={"event.action": "rehashing"})
        logger.error("rehashing(): self.values → %s", self.values, extra={"event.action": "rehashing"})
        for value in survivor_values:
            self.insert_data(value)
            logger.warning("<<< Exiting rehashing()", extra={"event.action": "rehashing"})

    def insert_data(self, data):
        """
        insert_data is used for inserting a single element at a time in the HashTable.

        Examples:

        >>> ht = HashTable(3)
        >>> ht.insert_data(5)
        >>> ht.keys()
        {2: 5}
        >>> ht = HashTable(5)
        >>> ht.insert_data(30)
        >>> ht.insert_data(50)
        >>> ht.keys()
        {0: 30, 1: 50}
        """
        logger.error(">>> Entering insert_data(data=%s)", data, extra={"event.action": "insert_data"})
        key = self.hash_function(data)
        logger.error("insert_data(data=%s): key → %s", data, key, extra={"event.action": "insert_data"})

        if self.values[key] is None:
            self._set_value(key, data)

        elif self.values[key] == data:
            pass

        else:
            collision_resolution = self._collision_resolution(key, data)
            logger.error("insert_data(data=%s): collision_resolution → %s", data, collision_resolution, extra={"event.action": "insert_data"})
            if collision_resolution is not None:
                self._set_value(collision_resolution, data)
            else:
                self.rehashing()
                self.insert_data(data)
                logger.warning("<<< Exiting insert_data(data=%s)", data, extra={"event.action": "insert_data"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
