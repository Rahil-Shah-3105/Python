import logging
logger = logging.getLogger(__name__)
# Implementation of Circular Queue (using Python lists)


class CircularQueue:
    """Circular FIFO queue with a fixed capacity"""

    def __init__(self, n: int):
        logger.error(">>> Entering __init__(n=%s)", n, extra={"event.action": "__init__", "logrite.n": n})
        self.n = n
        logger.debug("__init__(self=%s,n=%s): self.n → %s", self, n, self.n, extra={"event.action": "__init__", "logrite.n": n})
        self.array = [None] * self.n
        logger.debug("__init__(self=%s,n=%s): self.array → %s", self, n, self.array, extra={"event.action": "__init__", "logrite.n": n})
        self.front = 0  # index of the first element
        logger.debug("__init__(self=%s,n=%s): self.front → %s", self, n, self.front, extra={"event.action": "__init__", "logrite.n": n})
        self.rear = 0
        logger.debug("__init__(self=%s,n=%s): self.rear → %s", self, n, self.rear, extra={"event.action": "__init__", "logrite.n": n})
        self.size = 0
        logger.warning("<<< Exiting __init__(n=%s)", n, extra={"event.action": "__init__", "logrite.n": n})
        logger.debug("__init__(self=%s,n=%s): self.size → %s", self, n, self.size, extra={"event.action": "__init__", "logrite.n": n})

    def __len__(self) -> int:
        """
        >>> cq = CircularQueue(5)
        >>> len(cq)
        0
        >>> cq.enqueue("A")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> cq.array
        ['A', None, None, None, None]
        >>> len(cq)
        1
        """
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return self.size

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty or not
        >>> cq = CircularQueue(5)
        >>> cq.is_empty()
        True
        >>> cq.enqueue("A").is_empty()
        False
        """
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return self.size == 0

    def first(self):
        """
        Returns the first element of the queue
        >>> cq = CircularQueue(5)
        >>> cq.first()
        False
        >>> cq.enqueue("A").first()
        'A'
        """
        logger.error(">>> Entering first()", extra={"event.action": "first"})
        logger.warning("<<< Exiting first()", extra={"event.action": "first"})
        return False if self.is_empty() else self.array[self.front]

    def enqueue(self, data):
        """
        This function inserts an element at the end of the queue using self.rear value
        as an index.

        >>> cq = CircularQueue(5)
        >>> cq.enqueue("A")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> (cq.size, cq.first())
        (1, 'A')
        >>> cq.enqueue("B")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> cq.array
        ['A', 'B', None, None, None]
        >>> (cq.size, cq.first())
        (2, 'A')
        >>> cq.enqueue("C").enqueue("D").enqueue("E")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> cq.enqueue("F")
        Traceback (most recent call last):
           ...
        Exception: QUEUE IS FULL
        """
        logger.error(">>> Entering enqueue(data=%s)", data, extra={"event.action": "enqueue"})
        if self.size >= self.n:
            raise Exception("QUEUE IS FULL")

        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.n
        logger.error("enqueue(data=%s): self.rear → %s", data, self.rear, extra={"event.action": "enqueue"})
        self.size += 1
        logger.warning("<<< Exiting enqueue(data=%s)", data, extra={"event.action": "enqueue"})
        return self

    def dequeue(self):
        """
        This function removes an element from the queue using on self.front value as an
        index and returns it

        >>> cq = CircularQueue(5)
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        >>> cq.enqueue("A").enqueue("B").dequeue()
        'A'
        >>> (cq.size, cq.first())
        (1, 'B')
        >>> cq.dequeue()
        'B'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        """
        logger.error(">>> Entering dequeue()", extra={"event.action": "dequeue"})
        if self.size == 0:
            raise Exception("UNDERFLOW")

        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        logger.error("dequeue(): self.front → %s", self.front, extra={"event.action": "dequeue"})
        self.size -= 1
        logger.warning("<<< Exiting dequeue()", extra={"event.action": "dequeue"})
        return temp
