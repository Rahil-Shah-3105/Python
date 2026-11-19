"""
Pure Python implementations of a Fixed Priority Queue and an Element Priority Queue
using Python lists.
"""
import logging
logger = logging.getLogger(__name__)


class OverFlowError(Exception):
    pass


class UnderFlowError(Exception):
    pass


class FixedPriorityQueue:
    """
    Tasks can be added to a Priority Queue at any time and in any order but when Tasks
    are removed then the Task with the highest priority is removed in FIFO order.  In
    code we will use three levels of priority with priority zero Tasks being the most
    urgent (high priority) and priority 2 tasks being the least urgent.

    Examples
    >>> fpq = FixedPriorityQueue()
    >>> fpq.enqueue(0, 10)
    >>> fpq.enqueue(1, 70)
    >>> fpq.enqueue(0, 100)
    >>> fpq.enqueue(2, 1)
    >>> fpq.enqueue(2, 5)
    >>> fpq.enqueue(1, 7)
    >>> fpq.enqueue(2, 4)
    >>> fpq.enqueue(1, 64)
    >>> fpq.enqueue(0, 128)
    >>> print(fpq)
    Priority 0: [10, 100, 128]
    Priority 1: [70, 7, 64]
    Priority 2: [1, 5, 4]
    >>> fpq.dequeue()
    10
    >>> fpq.dequeue()
    100
    >>> fpq.dequeue()
    128
    >>> fpq.dequeue()
    70
    >>> fpq.dequeue()
    7
    >>> print(fpq)
    Priority 0: []
    Priority 1: [64]
    Priority 2: [1, 5, 4]
    >>> fpq.dequeue()
    64
    >>> fpq.dequeue()
    1
    >>> fpq.dequeue()
    5
    >>> fpq.dequeue()
    4
    >>> fpq.dequeue()
    Traceback (most recent call last):
        ...
    data_structures.queues.priority_queue_using_list.UnderFlowError: All queues are empty
    >>> print(fpq)
    Priority 0: []
    Priority 1: []
    Priority 2: []
    """  # noqa: E501

    def __init__(self):
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.queues = [
            [],
            [],
            [],
        ]
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.queues → %s", self, self.queues, extra={"event.action": "__init__"})

    def enqueue(self, priority: int, data: int) -> None:
        """
        Add an element to a queue based on its priority.
        If the priority is invalid ValueError is raised.
        If the queue is full an OverFlowError is raised.
        """
        logger.error(">>> Entering enqueue(priority=%s,data=%s)", priority, data, extra={"event.action": "enqueue", "logrite.priority": priority})
        try:
            if len(self.queues[priority]) >= 100:
                raise OverflowError("Maximum queue size is 100")
            self.queues[priority].append(data)
        except IndexError:
            logger.error("Exception in enqueue(priority=%s,data=%s)", priority, data, exc_info=True, extra={"event.action": "enqueue", "event.category": "process", "logrite.priority": priority})
            logger.warning("<<< Exiting enqueue(priority=%s,data=%s)", priority, data, extra={"event.action": "enqueue", "logrite.priority": priority})
            raise ValueError("Valid priorities are 0, 1, and 2")

    def dequeue(self) -> int:
        """
        Return the highest priority element in FIFO order.
        If the queue is empty then an under flow exception is raised.
        """
        logger.error(">>> Entering dequeue()", extra={"event.action": "dequeue"})
        for queue in self.queues:
            if queue:
                return queue.pop(0)
        logger.warning("<<< Exiting dequeue()", extra={"event.action": "dequeue"})
        raise UnderFlowError("All queues are empty")

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return "\n".join(f"Priority {i}: {q}" for i, q in enumerate(self.queues))


class ElementPriorityQueue:
    """
    Element Priority Queue is the same as Fixed Priority Queue except that the value of
    the element itself is the priority. The rules for priorities are the same the as
    Fixed Priority Queue.

    >>> epq = ElementPriorityQueue()
    >>> epq.enqueue(10)
    >>> epq.enqueue(70)
    >>> epq.enqueue(4)
    >>> epq.enqueue(1)
    >>> epq.enqueue(5)
    >>> epq.enqueue(7)
    >>> epq.enqueue(4)
    >>> epq.enqueue(64)
    >>> epq.enqueue(128)
    >>> print(epq)
    [10, 70, 4, 1, 5, 7, 4, 64, 128]
    >>> epq.dequeue()
    1
    >>> epq.dequeue()
    4
    >>> epq.dequeue()
    4
    >>> epq.dequeue()
    5
    >>> epq.dequeue()
    7
    >>> epq.dequeue()
    10
    >>> print(epq)
    [70, 64, 128]
    >>> epq.dequeue()
    64
    >>> epq.dequeue()
    70
    >>> epq.dequeue()
    128
    >>> epq.dequeue()
    Traceback (most recent call last):
        ...
    data_structures.queues.priority_queue_using_list.UnderFlowError: The queue is empty
    >>> print(epq)
    []
    """

    def __init__(self):
        self.queue = []
        logger.debug("__init__(self=%s): self.queue → %s", self, self.queue, extra={"event.action": "__init__"})

    def enqueue(self, data: int) -> None:
        """
        This function enters the element into the queue
        If the queue is full an Exception is raised saying Over Flow!
        """
        logger.error(">>> Entering enqueue(data=%s)", data, extra={"event.action": "enqueue"})
        if len(self.queue) == 100:
            raise OverFlowError("Maximum queue size is 100")
        self.queue.append(data)
        logger.warning("<<< Exiting enqueue(data=%s)", data, extra={"event.action": "enqueue"})

    def dequeue(self) -> int:
        """
        Return the highest priority element in FIFO order.
        If the queue is empty then an under flow exception is raised.
        """
        if not self.queue:
            raise UnderFlowError("The queue is empty")
        else:
            data = min(self.queue)
            logger.error("dequeue(): data → %s", data, extra={"event.action": "dequeue"})
            self.queue.remove(data)
            return data

    def __str__(self) -> str:
        """
        Prints all the elements within the Element Priority Queue
        """
        return str(self.queue)


def fixed_priority_queue():
    logger.error(">>> Entering fixed_priority_queue()", extra={"event.action": "fixed_priority_queue"})
    fpq = FixedPriorityQueue()
    logger.error("fixed_priority_queue(): fpq → %s", fpq, extra={"event.action": "fixed_priority_queue"})
    fpq.enqueue(0, 10)
    fpq.enqueue(1, 70)
    fpq.enqueue(0, 100)
    fpq.enqueue(2, 1)
    fpq.enqueue(2, 5)
    fpq.enqueue(1, 7)
    fpq.enqueue(2, 4)
    fpq.enqueue(1, 64)
    fpq.enqueue(0, 128)
    print(fpq)
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq)
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    print(fpq.dequeue())
    logger.warning("<<< Exiting fixed_priority_queue()", extra={"event.action": "fixed_priority_queue"})


def element_priority_queue():
    logger.error(">>> Entering element_priority_queue()", extra={"event.action": "element_priority_queue"})
    epq = ElementPriorityQueue()
    logger.error("element_priority_queue(): epq → %s", epq, extra={"event.action": "element_priority_queue"})
    epq.enqueue(10)
    epq.enqueue(70)
    epq.enqueue(100)
    epq.enqueue(1)
    epq.enqueue(5)
    epq.enqueue(7)
    epq.enqueue(4)
    epq.enqueue(64)
    epq.enqueue(128)
    print(epq)
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq)
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    print(epq.dequeue())
    logger.warning("<<< Exiting element_priority_queue()", extra={"event.action": "element_priority_queue"})


if __name__ == "__main__":
    fixed_priority_queue()
    element_priority_queue()
