"""Queue represented by a pseudo stack (represented by a list with pop and append)"""

from typing import Any
import logging
logger = logging.getLogger(__name__)


class Queue:
    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.stack = []
        logger.debug("__init__(self=%s): self.stack → %s", self, self.stack)
        self.length = 0
        logger.debug("__init__(self=%s): self.length → %s", self, self.length)
        logger.debug("<<< Exiting __init__()")

    def __str__(self):
        logger.debug(">>> Entering __str__()")
        printed = "<" + str(self.stack)[1:-1] + ">"
        logger.debug("__str__(self=%s): printed → %s", self, printed)
        logger.debug("__str__(): printed → %s", printed)
        logger.debug("<<< Exiting __str__()")
        return printed

    """Enqueues {@code item}
    @param item
        item to enqueue"""

    def put(self, item: Any) -> None:
        logger.debug(">>> Entering put(item=%s)", item)
        logger.debug("put(self=%s,item=%s): self.length → %s", self, item, self.length)
        self.stack.append(item)
        logger.debug("<<< Exiting put(item=%s)", item)
        self.length = self.length + 1

    """Dequeues {@code item}
    @requirement: |self.length| > 0
    @return dequeued
        item that was dequeued"""

    def get(self) -> Any:
        logger.debug(">>> Entering get()")
        self.rotate(1)
        dequeued = self.stack[self.length - 1]
        logger.debug("get(self=%s): dequeued → %s", self, dequeued)
        self.stack = self.stack[:-1]
        logger.debug("get(self=%s): self.stack → %s", self, self.stack)
        self.rotate(self.length - 1)
        self.length = self.length - 1
        logger.debug("get(self=%s): self.length → %s", self, self.length)
        logger.debug("<<< Exiting get()")
        return dequeued

    """Rotates the queue {@code rotation} times
    @param rotation
        number of times to rotate queue"""

    def rotate(self, rotation: int) -> None:
        logger.debug(">>> Entering rotate(rotation=%s)", rotation)
        for _ in range(rotation):
            temp = self.stack[0]
            self.stack = self.stack[1:]
            logger.debug("rotate(self=%s,rotation=%s): self.stack → %s", self, rotation, self.stack)
            logger.debug("rotate(self=%s,rotation=%s): self.length → %s", self, rotation, self.length)
            self.put(temp)
            logger.debug("<<< Exiting rotate(rotation=%s)", rotation)
            self.length = self.length - 1

    """Reports item at the front of self
    @return item at front of self.stack"""

    def front(self) -> Any:
        logger.debug(">>> Entering front()")
        front = self.get()
        logger.debug("front(): front → %s", front)
        logger.debug("front(self=%s): front → %s", self, front)
        self.put(front)
        self.rotate(self.length - 1)
        logger.debug("<<< Exiting front()")
        return front

    """Returns the length of this.stack"""

    def size(self) -> int:
        logger.debug(">>> Entering size()")
        logger.debug("<<< Exiting size()")
        return self.length
