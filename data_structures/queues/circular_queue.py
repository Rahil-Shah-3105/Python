import logging
logger = logging.getLogger(__name__)
# Implementation of Circular Queue (using Python lists)


class CircularQueue:
    """Circular FIFO queue with a fixed capacity"""

    def __init__(self, n: int):
        logger.debug(">>> Entering __init__(n=%s)", n)
        self.n = n
        logger.debug("__init__(self=%s,n=%s): self.n → %s", self, n, self.n)
        self.array = [None] * self.n
        logger.debug("__init__(self=%s,n=%s): self.array → %s", self, n, self.array)
        self.front = 0  # index of the first element
        logger.debug("__init__(self=%s,n=%s): self.front → %s", self, n, self.front)
        self.rear = 0
        logger.debug("__init__(self=%s,n=%s): self.rear → %s", self, n, self.rear)
        self.size = 0
        logger.debug("__init__(self=%s,n=%s): self.size → %s", self, n, self.size)
        logger.debug("<<< Exiting __init__(n=%s)", n)

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
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
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
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
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
        logger.debug(">>> Entering first()")
        logger.debug("<<< Exiting first()")
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
        logger.debug(">>> Entering enqueue(data=%s)", data)
        if self.size >= self.n:
            raise Exception("QUEUE IS FULL")

        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.n
        logger.debug("enqueue(data=%s): self.rear → %s", data, self.rear)
        self.size += 1
        logger.debug("<<< Exiting enqueue(data=%s)", data)
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
        logger.debug(">>> Entering dequeue()")
        if self.size == 0:
            raise Exception("UNDERFLOW")

        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        logger.debug("dequeue(): self.front → %s", self.front)
        self.size -= 1
        logger.debug("<<< Exiting dequeue()")
        return temp
