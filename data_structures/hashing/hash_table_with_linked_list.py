from collections import deque

from .hash_table import HashTable
import logging
logger = logging.getLogger(__name__)


class HashTableWithLinkedList(HashTable):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def _set_value(self, key, data):
        logger.error(">>> Entering _set_value(key=%s,data=%s)", key, data, extra={"event.action": "_set_value", "logrite.key": key})
        self.values[key] = deque() if self.values[key] is None else self.values[key]
        self.values[key].appendleft(data)
        self._keys[key] = self.values[key]
        logger.warning("<<< Exiting _set_value(key=%s,data=%s)", key, data, extra={"event.action": "_set_value", "logrite.key": key})

    def balanced_factor(self):
        logger.error(">>> Entering balanced_factor()", extra={"event.action": "balanced_factor"})
        logger.warning("<<< Exiting balanced_factor()", extra={"event.action": "balanced_factor"})
        return (
            sum(self.charge_factor - len(slot) for slot in self.values)
            / self.size_table
            * self.charge_factor
        )

    def _collision_resolution(self, key, data=None):
        logger.error(">>> Entering _collision_resolution(key=%s,data=%s)", key, data, extra={"event.action": "_collision_resolution", "logrite.key": key})
        if not (
            len(self.values[key]) == self.charge_factor and self.values.count(None) == 0
        ):
            return key
        logger.warning("<<< Exiting _collision_resolution(key=%s,data=%s)", key, data, extra={"event.action": "_collision_resolution", "logrite.key": key})
        return super()._collision_resolution(key, data)
