from collections import deque

from .hash_table import HashTable
import logging
logger = logging.getLogger(__name__)


class HashTableWithLinkedList(HashTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.debug(">>> Entering __init__()")
        logger.debug("<<< Exiting __init__()")

    def _set_value(self, key, data):
        logger.debug(">>> Entering _set_value(key=%s,data=%s)", key, data)
        self.values[key] = deque() if self.values[key] is None else self.values[key]
        self.values[key].appendleft(data)
        self._keys[key] = self.values[key]
        logger.debug("<<< Exiting _set_value(key=%s,data=%s)", key, data)

    def balanced_factor(self):
        logger.debug(">>> Entering balanced_factor()")
        logger.debug("<<< Exiting balanced_factor()")
        return (
            sum(self.charge_factor - len(slot) for slot in self.values)
            / self.size_table
            * self.charge_factor
        )

    def _collision_resolution(self, key, data=None):
        logger.debug(">>> Entering _collision_resolution(key=%s,data=%s)", key, data)
        if not (
            len(self.values[key]) == self.charge_factor and self.values.count(None) == 0
        ):
            return key
            logger.debug("<<< Exiting _collision_resolution(key=%s,data=%s)", key, data)
        return super()._collision_resolution(key, data)
