"""Queue represented by a pseudo stack (represented by a list with pop and append)"""

from typing import Any
import logging
logger = logging.getLogger(__name__)


class Queue:
    def __init__(self):
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.stack = []
        logger.debug("__init__(self=%s): self.stack → %s", self, self.stack, extra={"event.action": "__init__"})
        self.length = 0
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.length → %s", self, self.length, extra={"event.action": "__init__"})

    def __str__(self):
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        printed = "<" + str(self.stack)[1:-1] + ">"
        logger.error("__str__(): printed → %s", printed, extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return printed

    """Enqueues {@code item}
    @param item
        item to enqueue"""

    def put(self, item: Any) -> None:
        logger.error(">>> Entering put(item=%s)", item, extra={"event.action": "put", "logrite.item": item})
        self.stack.append(item)
        logger.warning("<<< Exiting put(item=%s)", item, extra={"event.action": "put", "logrite.item": item})
        self.length = self.length + 1
        logger.debug("put(self=%s,item=%s): self.length → %s", self, item, self.length, extra={"event.action": "put", "logrite.item": item})

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""

    def get(self) -> Any:
        logger.error(">>> Entering get()", extra={"event.action": "get"})
        self.rotate(1)
        dequeued = self.stack[self.length - 1]
        self.stack = self.stack[:-1]
        logger.debug("get(self=%s): self.stack → %s", self, self.stack, extra={"event.action": "get"})
        self.rotate(self.length - 1)
        self.length = self.length - 1
        logger.debug("get(self=%s): self.length → %s", self, self.length, extra={"event.action": "get"})
        logger.warning("<<< Exiting get()", extra={"event.action": "get"})
        return dequeued

    """Rotates the queue {@code rotation} times
    @param rotation
        number of times to rotate queue"""

    def rotate(self, rotation: int) -> None:
        logger.error(">>> Entering rotate(rotation=%s)", rotation, extra={"event.action": "rotate", "logrite.rotation": rotation})
        for _ in range(rotation):
            temp = self.stack[0]
            self.stack = self.stack[1:]
            logger.debug("rotate(self=%s,rotation=%s): self.stack → %s", self, rotation, self.stack, extra={"event.action": "rotate", "logrite.rotation": rotation})
            self.put(temp)
            logger.warning("<<< Exiting rotate(rotation=%s)", rotation, extra={"event.action": "rotate", "logrite.rotation": rotation})
            self.length = self.length - 1
            logger.debug("rotate(self=%s,rotation=%s): self.length → %s", self, rotation, self.length, extra={"event.action": "rotate", "logrite.rotation": rotation})

    """Reports item at the front of self
    @return item at front of self.stack"""

    def front(self) -> Any:
        logger.error(">>> Entering front()", extra={"event.action": "front"})
        front = self.get()
        logger.error("front(): front → %s", front, extra={"event.action": "front"})
        self.put(front)
        self.rotate(self.length - 1)
        logger.warning("<<< Exiting front()", extra={"event.action": "front"})
        return front

    """Returns the length of this.stack"""

    def size(self) -> int:
        logger.error(">>> Entering size()", extra={"event.action": "size"})
        logger.warning("<<< Exiting size()", extra={"event.action": "size"})
        return self.length
